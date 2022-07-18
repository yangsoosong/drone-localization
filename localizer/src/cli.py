import argparse
import time

import av
import cv2
import numpy
import tellopy
import click

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
    ctx.obj['drone'] = tellopy.Tello()
    try:
        ctx.obj['drone'].connect()
        ctx.obj['drone'].wait_for_connection(60.0)
    except Exception as ex:
        print(ex)
        ctx.obj['drone'].quit()
        return None

@main.command()
@click.option('--direction', nargs=1, type=click.Choice(["forward", "back", "left", "right", "up", "down"], case_sensitive=False), prompt=True)
@click.pass_context
def move(ctx, direction):
    if ctx.obj['DRY_RUN']:
        print(f'>> move {direction} <<')
        return
    if direction == 'forward':
        ctx.obj['drone'].forward(0.5)
    elif direction == 'back':
        ctx.obj['drone'].back(0.5)
    elif direction == 'left':
        ctx.obj['drone'].left(0.5)
    elif direction == 'right':
        ctx.obj['drone'].right(0.5)
    elif direction == 'up':
        ctx.obj['drone'].up(0.5)
    elif direction == 'down':
        ctx.obj['drone'].down(0.5)

@main.command()
@click.option('--direction', nargs=1, type=click.Choice(["clockwise", "counter"], case_sensitive=False), prompt=True)
@click.pass_context
def rotate(ctx, direction):
    if ctx.obj['DRY_RUN']:
        print(f'>> rotate {direction} <<')
        return
    if direction == 'clockwise':
        ctx.obj['drone'].clockwise(90)
    else:
        ctx.obj['drone'].counter_clockwise(90)

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
    ctx.obj['drone'].subscribe(ctx.obj['drone'].EVENT_FLIGHT_DATA, lambda event, sender, data, **args: print('flight data: %s: %s' % (event.name, str(data))))

@main.command()
@click.pass_context
def stream(ctx):
    from .detection import detect_objects
    if ctx.obj['DRY_RUN']:
        print('>> stream <<')
        return
    retry = 3
    container = None
    while container is None and 0 < retry:
        retry -= 1
        try:
            container = av.open(ctx.obj['drone'].get_video_stream())
        except av.AVError as ave:
            print(ave)
            print('retry...')

    # skip first 300 frames
    frame_skip = 300
    while True:
        for frame in container.decode(video=0):
            if 0 < frame_skip:
                frame_skip = frame_skip - 1
                continue
            start_time = time.time()
            image = cv2.cvtColor(numpy.array(frame.to_image()), cv2.COLOR_RGB2BGR)
            print(f'detecting objects in frame')
            annotated_image, detections = detect_objects(image)
            print(f'detections: {detections}')
            cv2.imshow("", annotated_image)     
            cv2.waitKey(1)
            if frame.time_base < 1.0/60:
                time_base = 1.0/60
            else:
                time_base = frame.time_base
            frame_skip = int((time.time() - start_time)/time_base)

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