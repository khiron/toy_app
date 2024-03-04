import textwrap
from cogent3.app.composable import define_app

@define_app
def indent_print(txt: str) -> str:
    """some docstring"""
    return textwrap.indent(txt, prefix="  ")
