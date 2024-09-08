import typer
from accountant.commands.invoice import app as invoice_app
from accountant.commands.quotation import app as quotation_app

app = typer.Typer()
app.add_typer(invoice_app)
app.add_typer(quotation_app)


@app.command()
def login() -> None:
    """Login into Accountant."""
    raise RuntimeError("In progress...")
