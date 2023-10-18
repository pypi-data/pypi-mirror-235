"""
This file holds all of the CLI commands for the "anyscale machines" path.
"""
import click
from rich.console import Console
from rich.table import Table

from anyscale.controllers.machines_controller import MachinesController


@click.group(
    "machine", help="Commands to interact with machines in Anyscale.",
)
def machines_cli() -> None:
    pass


@machines_cli.command(name="list", help="List machines registered to Anyscale.")
@click.option("--cloud_id", type=str, required=True, help="Provide a cloud ID.")
def list_machines(cloud_id: str,) -> None:
    machines_controller = MachinesController()
    output = machines_controller.list_machines(cloud_id=cloud_id)

    table = Table()
    table.add_column("ID")
    table.add_column("Host Name")
    table.add_column("Shape")
    table.add_column("Connection State")
    table.add_column("Allocation State")
    table.add_column("Cluster ID")
    table.add_column("Node ID")
    for m in output.machines:
        table.add_row(
            m.machine_id,
            m.hostname,
            m.machine_shape,
            m.connection_state,
            m.allocation_state,
            m.cluster_id,
            m.node_id,
        )

    console = Console()
    console.print(table)
