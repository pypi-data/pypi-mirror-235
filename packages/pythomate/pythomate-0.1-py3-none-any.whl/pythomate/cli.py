import click


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.pass_context
@click.version_option()
def cli(ctx):
  """
    Funções Iniciais
  """
