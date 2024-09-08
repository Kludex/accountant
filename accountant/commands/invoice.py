from typing import Annotated
import datetime
from typer import Typer, Option, Argument
from accountant.types import Currency, Download, Language

app = Typer(name="invoice")


@app.command()
def create(
    name: str | None = None,
    email: str | None = None,
    currency: Currency | None = None,
    date: Annotated[datetime.date | None, Argument()] = None,
    from_quotation: bool = False,
    download: Download = Download.PDF,
    language: Language = Language.EN,
) -> None:
    """Create an invoice.

    By default, `accountant` comes with a default template for the quotation.
    """
    date = date or datetime.date.today()
    if from_quotation:
        print("Creating invoice from quotation")
    if download == Download.PDF:
        print("Creating PDF...")


@app.command()
def list(
    unpaid: Annotated[bool, Option()] = True,
    paid: Annotated[bool, Option()] = True,
) -> None: ...
