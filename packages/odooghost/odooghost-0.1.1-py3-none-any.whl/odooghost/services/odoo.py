import shutil
import typing as t

from docker.types import Mount
from loguru import logger

from odooghost import addons, renderer
from odooghost.container import Container

from .base import BaseService

if t.TYPE_CHECKING:
    from odooghost import config


class OdooService(BaseService):
    def __init__(self, stack_config: "config.StackConfig") -> None:
        super().__init__(name="odoo", stack_config=stack_config)
        self._addons = addons.AddonsManager(addons_config=self.config.addons)

    def _prepare_build_context(self) -> None:
        super()._prepare_build_context()
        if self._addons.has_copy_addons:
            copy_addons_path = self.build_context_path / "addons"
            copy_addons_path.mkdir()
            for addons_path in self._addons.get_copy_addons():
                src_path = addons_path.path
                dst_path = copy_addons_path / addons_path.name_hash
                logger.debug(f"Copying {src_path.as_posix()} to {dst_path.as_posix()}")
                shutil.copytree(
                    src=src_path,
                    dst=dst_path,
                )
        if self.config.dependencies.python and self.config.dependencies.python.files:
            requirments_path = self.build_context_path / "requirments"
            requirments_path.mkdir()
            for requirments_file in self.config.dependencies.python.files:
                dst_path = (
                    requirments_path
                    / self.config.dependencies.python.get_file_hash(requirments_file)
                )
                logger.debug(
                    f"Copying {requirments_file.as_posix()} to {dst_path.as_posix()}"
                )
                shutil.copyfile(
                    src=requirments_file,
                    dst=dst_path,
                )
        with open((self.build_context_path / "Dockerfile").as_posix(), "w") as stream:
            logger.debug("Rendering Dockerfile ...")
            stream.write(
                renderer.render_dockerfile(
                    odoo_version=self.config.version,
                    dependencies=self.config.dependencies,
                    copy_addons=self._addons.has_copy_addons
                    and list(self._addons.get_copy_addons())
                    or None,
                    mount_addons=self._addons.has_mount_addons,
                )
            )

    def _get_cmdline(self) -> str:
        cmdline = ""
        if (
            self.config.cmdline.startswith("odoo")
            or self.config.cmdline.startswith("--")
            or self.config.cmdline.startswith("-")
        ):
            cmdline = self.config.cmdline
        else:
            return self.config.cmdline
        return f"{cmdline} --addons-path={self._addons.get_addons_path()}"

    def _get_mounts(self) -> t.List[Mount]:
        mounts = [
            Mount(
                source=self.volume_name,
                target="/var/lib/odoo",
                type="volume",
            )
        ]
        for addons_path in self._addons.get_mount_addons():
            mounts.append(
                Mount(
                    source=addons_path.path.as_posix(),
                    target=addons_path.container_posix_path,
                    type="bind",
                )
            )
        return mounts

    def _get_environment(self) -> dict[str, any]:
        db_service = self.stack_config.services.db
        return dict(
            HOST=db_service.host
            or self.stack_config.get_service_hostname(service="db"),
            USER=db_service.user or "odoo",
            password=db_service.password or "odoo",
        )

    def create_container(self) -> Container:
        # TODO create get container create options method
        return super().create_container(
            command=self._get_cmdline(),
            mounts=self._get_mounts(),
            tty=True,
        )

    def create(self, force: bool, do_pull: bool, ensure_addons: bool) -> None:
        if ensure_addons:
            self._addons.ensure()
        return super().create(force=force, do_pull=do_pull)

    @property
    def config(self) -> "config.OdooStackConfig":
        return super().config

    @property
    def base_image_tag(self) -> str:
        return f"odoo:{self.config.version}"

    @property
    def image_tag(self) -> str:
        return f"odooghost_{self.stack_name}:{self.config.version}".lower()

    @property
    def has_custom_image(self) -> bool:
        return True
