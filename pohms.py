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
def detect(path):
    '''
        Detect whether an image or a group of images are resistors or not.
    '''

    # setting cpu as default for inference
    defaults.device = torch.device('cpu')

    # load model
    learner = load_learner(path='.', file='resnet34_0.pkl')

    # open image
    img = open_image(path)

    # inference
    pred_class, pred_idx, outputs = learner.predict(img)

    click.echo(f'prediction: {pred_class} ')
    click.echo(f'prediction idx: {pred_idx} ')
    click.echo(f'outputs: {outputs}')
