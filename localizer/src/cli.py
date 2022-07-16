import argparse
import time

import av
import cv2
import numpy
import tellopy
from .detection import detect_objects


def main():
    """Drone initiation function for testing.  """

    parser = argparse.ArgumentParser(description="Tello CLI")
    parser.add_argument('command', help='foo help')
    subparsers = parser.add_subparsers(help='sub-command help')

    move = subparsers.add_parser('move', help='move help')
    move.add_argument("direction", action="store", type=str, choices=["forward", "back", "left", "right", "up", "down"])

    rotate = subparsers.add_parser('rotate', help='a help')
    rotate.add_argument("direction", action="store", type=str, choices=["clockwise", "counter"])

    takeoff = subparsers.add_parser('takeoff', help='takeoff help')

    land = subparsers.add_parser('land', help='land help')

    get_info = subparsers.add_parser('get_info', help='get_info help')

    args = parser.parse_args()

    drone = tellopy.Tello()
    try:
        drone.connect()
        drone.wait_for_connection(60.0)
    except Exception as ex:
        print(ex)
        drone.quit()
        return None

    if args.command == 'move':
        drone.getattr(args.direction)(1)
    elif args.command == 'rotate':
        if args.direction == 'clockwise':
            drone.clockwise(90)
        else:
            drone.counter_clockwise(90)
    elif args.command == 'takeoff':
        drone.takeoff()
    elif args.command == 'land':
        drone.land()
    elif args.command == 'get_info':
        drone.subscribe(drone.EVENT_FLIGHT_DATA, lambda event, sender, data, **args: print('flight data: %s: %s' % (event.name, str(data))))
    elif args.command == 'stream':
        retry = 3
        container = None
        while container is None and 0 < retry:
            retry -= 1
            try:
                container = av.open(drone.get_video_stream())
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
                cv2.imshow('Original', image)
                cv2.imshow('Canny', cv2.Canny(image, 100, 200))
                cv2.waitKey(1)
                if frame.time_base < 1.0/60:
                    time_base = 1.0/60
                else:
                    time_base = frame.time_base
                frame_skip = int((time.time() - start_time)/time_base)
    elif args.command == 'detect':
        retry = 3
        container = None
        while container is None and 0 < retry:
            retry -= 1
            try:
                container = av.open(drone.get_video_stream())
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
    drone.quit()