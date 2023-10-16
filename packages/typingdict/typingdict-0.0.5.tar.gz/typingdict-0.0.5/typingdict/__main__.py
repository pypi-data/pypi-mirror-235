# import sys
# from pathlib import Path
# import json
# from . import typerify
# from .beautifier import beautify

import json
import sys
from io import TextIOWrapper

import click


@click.command()
@click.argument(
    "input",
    type=click.File("r"),
    required=True,
)
@click.option(
    "--output", "-o", type=click.File("w"), default=None, help="Output file path"
)
def main(input: TextIOWrapper, output: TextIOWrapper):
    from . import typerify
    from .beautifier import beautify

    print = output.write if output else sys.stdout.write

    data = json.load(input)
    code = typerify(data)
    code = beautify(code)
    print(code)


if __name__ == "__main__":
    main()
