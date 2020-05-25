#!/usr/bin/python
# coding=utf-8

import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name', default='')
def install(name):
    '''
    install dependency from meta/main.yml in local folder
    '''
    print('hey you')


if __name__ == '__main__':
    cli()
