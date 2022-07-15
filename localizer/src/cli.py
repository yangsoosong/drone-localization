import argparse

from .tello import Tello


def main():
    drone = Tello('', 8889)
    parser = argparse.ArgumentParser(description="Tello CLI")
    subparsers = parser.add_subparsers(help='sub-command help')

    move = subparsers.add_parser('move', help='move help')
    move.add_argument("direction", action="store", type=str, choices=["forward", "back", "left", "right", "up", "down"])

    rotate = subparsers.add_parser('rotate', help='a help')
    rotate.add_argument("direction", action="store", type=str, choices=["clockwise", "counter"])

    takeoff = subparsers.add_parser('takeoff', help='takeoff help')

    land = subparsers.add_parser('land', help='land help')

    get_info = subparsers.add_parser('get_info', help='get_info help')

    args = parser.parse_args()

    if args.command == 'move':
        drone.move(args.direction, 1)
    elif args.command == 'rotate':
        if args.direction == 'clockwise':
            drone.rotate_cw(90)
        else:
            drone.rotate_ccw(90)
    elif args.command == 'takeoff':
        drone.takeoff()
    elif args.command == 'land':
        drone.land()
    elif args.command == 'get_info':
        print(f'Height: {drone.get_height()}')
        print(f'Battery: {drone.get_battery()}')
        print(f'Flight Time: {drone.get_flight_time()}')
        print(f'Speed: {drone.get_speed()}')
