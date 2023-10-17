import click
from tm_sl.sl import groups, projects, tasks  # Import your core logic functions
from tm_sl.sl.manager import SnapLogicManager  # Import the SnapLogicManager from where it's defined


class Connection:
    def __init__(self):
        # Initialize your connection here
        self.manager = SnapLogicManager()

@click.group()
@click.pass_context
def cli(ctx):
    """Your CLI application"""
    ctx.obj = Connection()  # Create and attach the Connection object to the context

@cli.command()
@click.pass_context
def list_groups(ctx):
    """List all groups."""
    click.echo(f"Using connection: {ctx.obj.connection}")
    groups.get_all_groups()  # Call the core logic function

@cli.command()
@click.pass_context
def list_projects(ctx):
    """List all projects."""
    click.echo(f"Using connection: {ctx.obj.connection}")
    projects.get_all_projects() # Call the core logic function

# Add more commands as needed

if __name__ == "__main__":
    cli()
