from unittest.mock import Mock

import pytest

from anyscale.client.openapi_client.models import (
    ListMachinesResponse,
    MachineAllocationState,
    MachineConnectionState,
    MachineInfo,
)
from frontend.cli.anyscale.controllers.machines_controller import MachinesController


@pytest.mark.parametrize("cloud_id", ["cld_123"])
def test_list_machines(mock_auth_api_client, cloud_id: str) -> None:
    response = ListMachinesResponse(
        machines=[
            MachineInfo(
                machine_id="m-123",
                hostname="dummy",
                machine_shape="lambda-a100-80g",
                connection_state=MachineConnectionState.CONNECTED,
                allocation_state=MachineAllocationState.AVAILABLE,
                cluster_id="",
                node_id="",
            )
        ]
    )

    api_response = Mock()
    api_response.result = response

    machines_controller = MachinesController()
    machines_controller.api_client.list_machines_api_v2_machines_get = Mock(
        return_value=api_response
    )
    output = machines_controller.list_machines(cloud_id=cloud_id)
    assert output == response
