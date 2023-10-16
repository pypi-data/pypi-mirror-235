import typing as t

from docker.types import Mount
from loguru import logger

from odooghost.container import Container

from .base import BaseService

if t.TYPE_CHECKING:
    from odooghost import config


class PostgresService(BaseService):
    def __init__(self, stack_config: "config.StackConfig") -> None:
        super().__init__(name="db", stack_config=stack_config)

    def _get_environment(self) -> t.Dict[str, t.Any]:
        return dict(
            POSTGRES_DB=self.config.db,
            POSTGRES_USER=self.config.user or "odoo",
            POSTGRES_PASSWORD=self.config.password or "odoo",
        )

    def ensure_base_image(self, do_pull: bool = False) -> None:
        if self.config.type == "remote":
            logger.warning("Skip postgres image as it's remote type")
        return super().ensure_base_image(do_pull)

    def create_container(self) -> Container:
        return super().create_container(
            mounts=[
                Mount(
                    source=self.volume_name,
                    target="/var/lib/postgresql/data",
                    type="volume",
                )
            ],
        )

    @property
    def config(self) -> "config.PostgresStackConfig":
        return super().config

    @property
    def is_remote(self) -> bool:
        return self.config.type == "remote"

    @property
    def base_image_tag(self) -> str:
        return f"postgres:{self.config.version}"

    @property
    def has_custom_image(self) -> bool:
        return False
