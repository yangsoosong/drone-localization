import argparse

import tellopy


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
