import click

@click.group()
def cli():
    pass

@click.command()
def start():
    """Start your vm"""
    # Implementation for starting the VM
    click.echo("Starting your VM...")

@click.command()
def stop():
    """Stop your vm"""
    # Implementation for stopping the VM
    click.echo("Stopping your VM...")

@click.command()
def connect():
    """Connect to your vm in vscode inside your ~/code/tomasromeiro/folder"""
    # Implementation for connecting to the VM
    click.echo("Connecting to your VM...")

# Add the commands to the CLI group
cli.add_command(start)
cli.add_command(stop)
cli.add_command(connect)

if __name__ == '__main__':
    cli()
