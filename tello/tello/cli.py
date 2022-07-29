import time

import av
import cv2
import numpy
import click

from .tello import Tello

tello_info = {}

@click.group()
@click.option('--dry-run/--live', default=False)
@click.pass_context
def main(ctx, dry_run):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj['DRY_RUN'] = dry_run
    if ctx.obj['DRY_RUN']:
        print('>> dry run mode <<')
        return
    print('initializing tello connection')
    ctx.obj['drone'] = Tello()

@main.command()
@click.option('--direction', nargs=1, type=click.Choice(["forward", "back", "left", "right", "up", "down"], case_sensitive=False), prompt=True)
@click.pass_context
def move(ctx, direction):
    if ctx.obj['DRY_RUN']:
        print(f'>> move {direction} <<')
        return
    ctx.obj['drone'].move(direction)

@main.command()
@click.option('--direction', nargs=1, type=click.Choice(["clockwise", "counter"], case_sensitive=False), prompt=True)
@click.pass_context
def rotate(ctx, direction):
    if ctx.obj['DRY_RUN']:
        print(f'>> rotate {direction} <<')
        return
    ctx.obj['drone'].rotate(direction)

@main.command()
@click.pass_context
def takeoff(ctx):
    if ctx.obj['DRY_RUN']:
        print('>> takeoff <<')
        return
    ctx.obj['drone'].takeoff()

@main.command()
@click.pass_context
def land(ctx):
    if ctx.obj['DRY_RUN']:
        print('>> land <<')
        return
    ctx.obj['drone'].land()

@main.command()
@click.pass_context
def query(ctx):
    if ctx.obj['DRY_RUN']:
        print('>> query <<')
        return
    print(ctx.obj['drone'].query())

@main.command()
@click.pass_context
def stream(ctx):
    if ctx.obj['DRY_RUN']:
        print('>> stream <<')
        return
    for frame in ctx.obj['drone'].get_video_frames():
        cv2.imshow("", frame)     
        cv2.waitKey(1)

@main.command()
@click.pass_context
def interactive(ctx):
    ctx.invoke(stream)
    while True:
        command = click.prompt('command > ', type=str)
        if command == 'move':
            direction = click.prompt('| direction > ', type=click.Choice(["forward", "back", "left", "right", "up", "down"], case_sensitive=False))
            ctx.invoke(move, direction=direction)
        elif command == 'rotate':
            direction = click.prompt('| direction > ', type=click.Choice(["clockwise", "counter"], case_sensitive=False))
            ctx.invoke(rotate, direction=direction)
        elif command == 'takeoff':
            ctx.invoke(takeoff)
        elif command == 'land':
            ctx.invoke(land)
        elif command == 'exit':
            break
        ctx.invoke(query)
        