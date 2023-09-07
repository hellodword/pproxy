import typer
import uvicorn

cli = typer.Typer(name="pproxy API")


@cli.command()
def run(
    port: int = 3000,
    host: str = 'localhost',
    log_level: str = 'debug',
    reload: bool = True,
):  # pragma: no cover
    """Run the API server."""
    uvicorn.run(
        "pproxy.app:app",
        host=host,
        port=port,
        log_level=log_level,
        reload=reload,
    )
