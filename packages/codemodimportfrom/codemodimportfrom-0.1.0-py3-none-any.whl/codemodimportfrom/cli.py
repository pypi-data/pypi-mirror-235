import typer

import codemodimportfrom

cli = typer.Typer()


@cli.command()
def transform_importfrom(
    file_path: str,
    modules: list[str] = typer.Option(default_factory=list),
    allow_list: list[str] = typer.Option(default_factory=list),
    transform_module_imports: bool = False,
):
    if len(allow_list) == 1 and allow_list[0].endswith(".txt"):
        with open(allow_list[0]) as f:
            allow_list = [line.strip() for line in f if line.strip()]

    with open(file_path) as f:
        code = f.read()
    transformed_code = codemodimportfrom.transform_importfrom(
        code=code,
        modules=modules,
        allow_list=allow_list,
        transform_module_imports=transform_module_imports,
    )
    print(transformed_code)


if __name__ == "__main__":
    cli()
