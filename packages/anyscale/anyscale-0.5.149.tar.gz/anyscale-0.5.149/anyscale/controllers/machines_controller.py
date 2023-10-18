from typing import Optional

from rich.console import Console

from anyscale.cli_logger import BlockLogger
from anyscale.client.openapi_client.models import ListMachinesResponse
from anyscale.controllers.base_controller import BaseController


class MachinesController(BaseController):
    def __init__(
        self, log: Optional[BlockLogger] = None, initialize_auth_api_client: bool = True
    ):
        if log is None:
            log = BlockLogger()

        super().__init__(initialize_auth_api_client=initialize_auth_api_client)
        self.log = log
        self.console = Console()

    def list_machines(self, cloud_id: str) -> ListMachinesResponse:
        response: ListMachinesResponse = self.api_client.list_machines_api_v2_machines_get(
            cloud_id
        ).result
        return response
