import typer
from sona.worker.commands import app as worker_app
from sona.http.commands import app as http_app

app = typer.Typer()
app.add_typer(worker_app, name="worker")
app.add_typer(http_app, name="http")