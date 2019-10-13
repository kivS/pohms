import click


@click.group()
def main_cli():
    '''
        Pohms - Resistor or not resistor image detector
    '''
    pass


@main_cli.command()
def detect():
    click.echo('Hello there!')


if __name__ == '__main__':
    main_cli()
