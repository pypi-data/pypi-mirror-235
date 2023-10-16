import click
from .auth import get_auth_token
from .util import BE_HOST, FE_HOST
import requests


@click.group()
def run():
    pass


@click.command()
@click.argument("suiteid")
@click.option("--use_sample_output", "-u", is_flag=True)
def start(suiteid: str, use_sample_output: bool):
    response = requests.post(
        url=f"{BE_HOST}/start_run/",
        headers={"Authorization": get_auth_token()},
        json={"test_suite_id": suiteid, "use_sample_output": use_sample_output},
    )
    if response.status_code == 200:
        run_id = response.json()["run_id"]
        # TODO:
        click.secho("Successfully started run.", fg="green")
        click.secho(f"{FE_HOST}/results?run_id={run_id}", bold=True)
    else:
        click.secho("Could not start run", fg="red")


run.add_command(start)
