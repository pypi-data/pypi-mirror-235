import enum
import pathlib
import typing
import uuid

import nicegui.ui
import typer
import uvicorn

uvicorn_log_levels = enum.StrEnum(value=r'UvicornLogLevel', names={v: v for v in uvicorn.config.LOG_LEVELS.keys()})
cli = typer.Typer(help="Сдесь может быть ваша реклама", no_args_is_help=True)


@cli.command(no_args_is_help=True, short_help=r'Запуск сервера приложений')
def serve(storage_secret: typing.Annotated[str, typer.Option()],
          limit_concurrency: typing.Annotated[int, typer.Option()] = 10,
          graceful_shutdown: typing.Annotated[int, typer.Option()] = 60,
          env_file: typing.Annotated[pathlib.Path, typer.Option(file_okay=True, exists=False, readable=True)] = pathlib.Path(r'.env'),
          root_path: typing.Annotated[pathlib.Path, typer.Option(exists=False)] = None,
          log_level: uvicorn_log_levels = getattr(uvicorn_log_levels, r'warning'),
          name: str = r'FORTA'):

    nicegui.ui.run(
        env_file=str(env_file.absolute()),
        access_log=True,
        date_header=False,
        forwarded_allow_ips=r'*',
        language=r'ru',
        limit_concurrency=limit_concurrency,
        prod_js=False,
        reload=False,
        server_header=False,
        show=False,
        storage_secret=storage_secret,
        timeout_graceful_shutdown=graceful_shutdown,
        timeout_notify=5,
        title=name,
        use_colors=True,
        uvicorn_logging_level=str(log_level),
        workers=1,
        root_path=str(root_path or r''))


@cli.command(short_help=r'Генерация секретного ключа шифрования данных пользователя')
def generate_secret():
    typer.echo(message=uuid.uuid4().hex, nl=False, color=False)


cli()
