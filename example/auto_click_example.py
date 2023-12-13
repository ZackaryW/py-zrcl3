import os
import sys
import click_shell
import click
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from zrcl3.auto_click import create_click_module # noqa
from zrcl3.auto_click.ctx import AutoClickCtx # noqa

dir_path = os.path.dirname(os.path.realpath(__file__))

res = create_click_module(AutoClickCtx(), os.path.join(dir_path, "auto_click_set"))

ctx = click.Context(res)
shell = click_shell.make_click_shell(ctx)
shell.cmdloop()

