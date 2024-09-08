from typer import Typer
from accountant.types import Currency, Download

app = Typer(name="quotation")


@app.command()
def create(
    name: str,
    email: str,
    currency: Currency,
    download: Download = Download.PDF,
) -> None:
    """Create a quotation.

    By default, `accountant` comes with a default template for the quotation.
    """

    if download == Download.PDF:
        print("Creating PDF...")


@app.command()
def list() -> None:
    """Show the list of created quotations.

    When Accountant Pro is enabled, it will also show a URL to the Accountant platform.
    """
