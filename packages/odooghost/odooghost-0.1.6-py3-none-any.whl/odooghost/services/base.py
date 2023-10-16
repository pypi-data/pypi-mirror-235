import abc
import shutil
import sys
import typing as t
from contextlib import contextmanager
from pathlib import Path

from docker.errors import APIError, ImageNotFound, NotFound
from loguru import logger
from pydantic import BaseModel

from odooghost import constant, exceptions, utils
from odooghost.container import Container
from odooghost.context import ctx
from odooghost.types import Filters, Labels
from odooghost.utils.misc import labels_as_list

if t.TYPE_CHECKING:
    from odooghost.config import StackConfig


class BaseService(abc.ABC):
    def __init__(self, name: str, stack_config: "StackConfig") -> None:
        self.name = name
        self.stack_config = stack_config
        self.stack_name = stack_config.name

    def _prepare_build_context(self) -> None:
        """
        Prepare build context for service image build
        """
        logger.info(f"Preparing build context for {self.name}")
        self.build_context_path.mkdir(parents=True, exist_ok=True)

    def _clean_build_context(self) -> None:
        """
        Clean service image build context
        """
        shutil.rmtree(self.build_context_path.as_posix())

    @abc.abstractmethod
    def _get_environment(self) -> t.Dict[str, t.Any]:
        """
        Get service environment

        Returns:
            t.Dict[str, t.Any]: service environment
        """
        return {}

    def labels(self) -> Labels:
        """
        Get service labels

        Returns:
            Labels: Docker labels
        """
        return {
            constant.LABEL_NAME: "true",
            constant.LABEL_STACKNAME: self.stack_name,
            constant.LABEL_STACK_SERVICE_TYPE: self.name,
        }

    def ensure_base_image(self, do_pull: bool = False) -> None:
        """
        Ensure service base image exists

        Args:
            do_pull (bool, optional): pull image. Defaults to False.

        Raises:
            exceptions.StackImagePullError: Error when pulling image
            exceptions.StackImageEnsureError: Error with docker client
        """
        logger.info(f"Ensuring image {self.base_image_tag}")
        try:
            ctx.docker.images.get(self.base_image_tag)
            if do_pull:
                ctx.docker.images.pull(self.base_image_tag)
        except ImageNotFound:
            try:
                ctx.docker.images.pull(self.base_image_tag)
            except APIError as err:
                raise exceptions.StackImagePullError(
                    f"Failed to pull image {self.base_image_tag}: {err}"
                )
        except APIError as err:
            raise exceptions.StackImageEnsureError(
                f"Failed to get image {self.base_image_tag}: {err}"
            )

    @contextmanager
    def build_context(self) -> None:
        """
        Build context contextmanager
        It ensure build context is cleaned event if an unknown error occurs
        """
        try:
            self._prepare_build_context()
            yield
        except Exception:
            raise
        finally:
            self._clean_build_context()

    def build_image(self, path: Path, rm: bool = True, no_cache: bool = True) -> str:
        """
        Build service image

        Args:
            path (Path): build context path
            rm (bool, optional): remove intermediate container. Defaults to True.
            no_cache (bool, optional): do not ser build cache. Defaults to True.

        Raises:
            exceptions.StackImageBuildError: When build gail

        Returns:
            str: image identifier
        """
        logger.info(f"Building {self.name} custom image")
        try:
            # TODO this should be moved
            all_events = list(
                utils.progress_stream.stream_output(
                    ctx.docker.api.build(
                        path=path.as_posix(),
                        tag=self.image_tag,
                        rm=False,
                        forcerm=True,
                        nocache=no_cache,
                        labels=self.labels(),
                    ),
                    sys.stdout,
                )
            )
        except exceptions.StreamOutputError:
            raise exceptions.StackImageBuildError(
                f"Failed to build {self.name} image, check dependencies"
            )

        image_id = utils.progress_stream.get_image_id_from_build(all_events)
        if image_id is None:
            raise exceptions.StackImageBuildError(
                f"Failed to build {self.name} image: {all_events[-1] if all_events else 'Unknown'}"
            )
        return image_id

    def drop_image(self) -> None:
        """
        Drop service image
        """
        if self.has_custom_image:
            try:
                ctx.docker.images.remove(image=self.image_tag)
            except NotFound:
                logger.warning(f"Image {self.image_tag} not found !")
            except APIError as err:
                logger.error(f"Failed to drop image {self.image_tag}: {err}")

    def create_volumes(self) -> None:
        """
        Create service volumes

        Raises:
            exceptions.StackVolumeCreateError: When volume creation fail
        """
        try:
            ctx.docker.volumes.create(
                name=self.volume_name,
                driver="local",
                labels=self.labels(),
            )
        except APIError as err:
            raise exceptions.StackVolumeCreateError(
                f"Failed to create {self.name} volume: {err}"
            )

    def drop_volumes(self) -> None:
        """
        Drop service volumes
        """
        try:
            volume = ctx.docker.volumes.get(self.volume_name)
            volume.remove()
        except NotFound:
            logger.warning(f"Volume {self.volume_name} not found !")
        except APIError as err:
            logger.error(f"Failed to drop volume {volume.id}: {err}")

    def containers(
        self,
        filters: t.Optional[Filters] = None,
        labels: t.Optional[Labels] = None,
        stopped: bool = True,
    ) -> t.List[Container]:
        """
        List service containers

        Args:
            filters (t.Optional[Filters], optional): filters. Defaults to None.
            labels (t.Optional[Labels], optional): docker lables. Defaults to None.
            stopped (bool, optional): stopped containers. Defaults to True.

        Returns:
            t.List[Container]: List of containers
        """
        if filters is None:
            filters = {}
        filters.update(
            {
                "label": labels_as_list(self.labels())
                + (labels_as_list(labels) if labels else [])
            }
        )
        return Container.search(filters=filters, stopped=stopped)

    @abc.abstractmethod
    def create_container(self, **options) -> Container:
        """
        Create service container

        Returns:
            Container: Container instance
        """
        default_options = dict(
            name=self.container_name,
            image=self.image_tag if self.has_custom_image else self.base_image_tag,
            hostname=self.container_hostname,
            labels=self.labels(),
            environment=self._get_environment(),
            network=self.stack_config.get_network_name(),
        )
        default_options.update(options)
        return Container.create(**default_options)

    def drop_containers(self, all: bool = True, force: bool = True) -> None:
        """
        Drop service containers

        Args:
            all (bool, optional): Stopped containers. Defaults to True.
            force (bool, optional): Force remove. Defaults to True.
        """
        for container in self.containers(stopped=all):
            try:
                container.remove(force=force)
            except APIError as err:
                logger.error(f"Failed to drop container {container.id}: {err}")

    def get_container(self, raise_not_found: bool = True) -> Container:
        """
        Get service container

        Raises:
            exceptions.StackContainerNotFound: Container not found
            exceptions.StackContainerGetError: Docker client error

        Returns:
            Container: Container instance
        """
        try:
            return Container.from_id(id=self.container_name)
        except NotFound:
            if not raise_not_found:
                return None
            raise exceptions.StackContainerNotFound(
                f"Container {self.container_name} not found !"
            )
        except APIError as err:
            raise exceptions.StackContainerGetError(
                f"Failed to get container {self.container_name} : {err}"
            )

    def start_container(self) -> Container:
        """
        Start service container

        Raises:
            exceptions.StackContainerStartError: Start failed

        Returns:
            Container: Container instance
        """
        container = self.get_container()
        try:
            container.start()
            return container
        except APIError:
            raise exceptions.StackContainerStartError(
                f"Failed to start container {container.id}"
            )

    def build(self, rm: bool = True, no_cache: bool = True) -> None:
        """
        Build service

        Args:
            rm (bool, optional): remove intermediate containers. Defaults to True.
            no_cache (bool, optional): do not use build cache. Defaults to False.
        """
        if not self.has_custom_image:
            return None
        with self.build_context():
            self.build_image(path=self.build_context_path, rm=rm, no_cache=no_cache)

    def create(self, force: bool, do_pull: bool) -> None:
        """
        Create service

        Args:
            force (bool): force recreate dangling container
            do_pull (bool): pull base image
        """
        self.ensure_base_image(do_pull=do_pull)
        self.build()
        self.create_volumes()

        container = self.get_container(raise_not_found=False)
        if container is None:
            self.create_container()
            return

        if force:
            container.remove()
            self.create_container()
            return

        logger.warning(
            f"Service {self.name} container already created ! Use --force option to recreate."
        )

    def drop(self, volumes: bool = True) -> None:
        """
        Drop service

        Args:
            volumes (bool, optional): drop service volumes. Defaults to True.
        """
        self.drop_containers()
        if volumes:
            self.drop_volumes()
        self.drop_image()

    @abc.abstractproperty
    def config(self) -> t.Type[BaseModel]:
        """
        Get service config
        """
        return getattr(self.stack_config.services, self.name)

    @abc.abstractproperty
    def base_image_tag(self) -> str:
        """
        Base service image tag

        Returns:
            str: image tag
        """
        ...

    @property
    def image_tag(self) -> str:
        """
        Service image tag

        Returns:
            str: image tag
        """
        raise NotImplementedError()

    @abc.abstractproperty
    def has_custom_image(self) -> bool:
        """
        Service has custom image

        Returns:
            bool:
        """
        ...

    @property
    def volume_name(self) -> str:
        """
        Service volume name
        """
        return f"odooghost_{self.stack_name}_{self.name}_data"

    @property
    def container_name(self) -> str:
        """
        Service container name
        """
        return f"odooghost_{self.stack_name}_{self.name}"

    @property
    def container_hostname(self) -> str:
        """
        Service container hostname
        """
        return self.stack_config.get_service_hostname(service=self.name)

    @property
    def build_context_path(self) -> Path:
        """
        Service build context path
        """
        return ctx.get_build_context_path() / self.stack_name / self.name
