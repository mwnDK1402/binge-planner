import click

@click.command()
@click.argument('episodes', nargs=1)
def cli(episodes):
    print(f'Test: {episodes}')

if __name__ == '__main__':
    cli()