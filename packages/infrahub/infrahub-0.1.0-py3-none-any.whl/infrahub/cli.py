import typer
import uvicorn

app = typer.Typer()

@app.command()
def start(
    listen: str = typer.Option("127.0.0.1", help="Address used to listen for new request."),
    port: int = typer.Option(8000, help="Port used to listen for new request."),
):
    uvicorn.run(
        "infrahub.main:app",
        host=listen,
        port=port,
        log_level="info",
        reload=True,
    )
