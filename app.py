import click
import redis

r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

def get_greeting(name):
    return f'Hello, {name}!'

def add_key_value_pair(key, value):
    r.set(key, value)

def get_value(key):
    return r.get(key)

def remove_key_value(key):
    value = get_value(key)
    r.delete(key)
    return value

@click.command()
@click.option('--name', prompt='Your name', help='Your name')
def greet(name):
    """This script greets you by name."""
    iam = get_greeting(name)
    click.echo(f'Hello, {iam}!')

@click.command()
@click.option('--key', prompt='key:', help='key')
@click.option('--value', prompt='value:', help='value')
def add(key, value):
    """add key-value pair."""
    add_key_value_pair(key, value)
    click.echo(f'added ({key}, {value})')

@click.command()
@click.option('--key', prompt='key:', help='key')
def get(key):
    """get value."""
    value = get_value(key)
    click.echo(f'found ({key}, {value})')

@click.command()
@click.option('--key', prompt='key:', help='key')
def remove(key):
    """remove value."""
    value = remove_key_value(key)
    click.echo(f'removed ({key}, {value})')

@click.group()
def red():
    pass

red.add_command(greet)
red.add_command(add)
red.add_command(get)
red.add_command(remove)

if __name__ == '__main__':
    red()
