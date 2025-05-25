import typer
from typing import List

app = typer.Typer()

@app.command()
def test_command(
    ids: List[int] = typer.Option(..., help="IDs", multiple=True)
):
    typer.echo(f"IDs recibidos: {ids}")

if __name__ == "__main__":
    app()