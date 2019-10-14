import click


@click.group()
def main_cli():
    '''
        Pohms - Resistor or not resistor image detector
    '''
    pass


@main_cli.command()
@click.option(
    '--path',
    help='Image or folder location',
    required=True,
    type=click.Path()
)
def detect(path):
    '''
        Detect whether an image or a group of images are resistors or not.
    '''

    click.echo('Hello there!')
