import json
from pathlib import Path

import click
import rich
from rich.console import Console
from rich.markdown import Markdown

my_data_json_path = Path(__file__).parent / "my_data.json"
my_data_md_path = Path(__file__).parent / "my_data.md"


@click.command()
def cli_main():
    click.secho("HI", fg="blue", bold=True)
    click.secho(f"{my_data_json_path=}", fg="magenta", bold=True)
    click.secho(f"{my_data_json_path.exists()=}", fg="magenta", bold=True)
    click.secho(f"{my_data_md_path=}", fg="magenta", bold=True)
    click.secho(f"{my_data_md_path.exists()=}", fg="magenta", bold=True)
    with my_data_json_path.open("rt") as f:
        json_data = json.load(f)
    rich.print(json_data)

    with my_data_md_path.open("rt") as f:
        md_data = f.read()

    console = Console()
    md = Markdown(md_data)
    console.print(md)

    click.secho("BYE", fg="blue", bold=True)
