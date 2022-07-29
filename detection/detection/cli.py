import click


@click.group()
def main():
    pass

@main.command()
def download():
    from .detection import load_model_network
    load_model_network()
