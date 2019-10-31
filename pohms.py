import os
from pathlib import Path
import click
from fastai.vision import defaults, torch, open_image, load_learner


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
@click.option(
    '--model',
    help='Path of pytorch model to use',
    default='export.pkl',
    type=click.Path()
)
@click.option(
    '--img-cat-bin',
    help='Bin location to display image on the commandline',
    default=Path.home() / '.iterm2' / 'imgcat',
    type=click.Path()
)
def detect(path, model, img_cat_bin):
    '''
        Detect whether an image or a group of images are resistors or not.
    '''

    # setting cpu as default for inference
    defaults.device = torch.device('cpu')

    try:
        # load model
        learner = load_learner(path='.', file=model)

        # open image
        img = open_image(path)

    except FileNotFoundError as e:
        click.echo(e, err=True)
        return

    click.echo('Starting prediction for:')

    # display image on the shell using imgcat from iterm2
    os.system(f'{img_cat_bin} {path}')

    # inference
    pred_class, pred_index, probs = learner.predict(img)

    click.echo(f'Data classes: {learner.data.classes} ')
    click.echo(f'prediction: {pred_class} ')
    click.echo(f'prediction index: {pred_index} ')
    click.echo(f'Probabilities: {probs}')
