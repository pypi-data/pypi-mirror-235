
import click
from tm_sl.com import *

from tm_sl.sl import groups

@click.group('group')
@click.pass_context
def group(ctx):
    '''
    Manage groups.
    '''
    pass


@group.command('list')
@click.argument('org', required=True)
@click.pass_context
def list_groups(ctx, org):
    """
    List all groups within the specified organization. 
    It retrieves all the groups in an organization and pretty prints them to the console.

    Example:
    ```shell
        $ tm-sl group list tidemark-dev
        [
            "admins",
            "members",
            "py_test_dev",
            "py_test_run",
            "python_test_group",
            "t_baseline_devs",
            "t_baseline_run"
        ]
    ```
    """
    c_json(groups.get_all_groups( ctx.obj['manager'], org))  # Call the core logic function