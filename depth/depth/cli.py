import click


@click.group()
def main():
    pass

@main.command()
def download():
    from .depth import load_model_network, load_transforms_network
    load_model_network()
    load_transforms_network()
