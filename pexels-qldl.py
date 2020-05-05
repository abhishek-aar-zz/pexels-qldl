import click
import os,sys
from WS_Pexels import *

@click.command()
@click.option('--query', prompt='Search what? ',
              help='Query of the request')
def download(query):
    PS = pexelScraper()
    PS.queryRequest(query)
if __name__ == '__main__':
    download()