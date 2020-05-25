#!/usr/bin/python
# coding=utf-8

import click
import os

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name', default='')
def install(name):
    '''
    install dependency from meta/main.yml in local folder
    '''
    if os.system("ansible-galaxy --version > /dev/null ") != 1:
        click.echo(click.style(
          'Ansible-galaxy not found!\
          You can manualy set path to ansible-galaxy bin,\
          use GALAXY_PATH env, or galaxy_path config options',
          fg='red'),
        err=True)

if __name__ == '__main__':
    cli()
