"""Tello control methods."""

import time

import av
import cv2
import numpy
import tellopy


class Tello:
    """Tello drone class.

    Attributes
    ----------
    drone : tellopy Tello class
    flight_info : dict

    Methods
    -------
    _set_tello_flight_info(data)
    move(direction)
    rotate(direction)
    takeoff()
    land()
    query()
    get_video_frames()
    """

    def __init__(self):
        self.drone = tellopy.Tello()
        try:
            self.drone.connect()
            self.drone.wait_for_connection(60.0)
        except Exception as ex:
            print(ex)
            self.drone.quit()
        self.flight_info = {}
        self.drone.subscribe(self.drone.EVENT_FLIGHT_DATA, (
                                    lambda event,
                                    sender,
                                    data,
                                    **args: self._set_tello_flight_info(data)
                                    ))

    def _set_tello_flight_info(self, data):
        """
        Return dict of tellopy.Tello.flight_info attribute values collected over
        the course of flight time. List of attributes available at
        github.com/hanyazou/TelloPy/blob/develop-0.7.0/tellopy/_internal/protocol.py.
        """
        flight_data_attrs = [a for a in dir(data) if not a.startswith('__') and not callable(getattr(data, a))]
        for key in flight_data_attrs:
            if key not in self.flight_info:
                self.flight_info[key] = []
            self.flight_info[key].append(getattr(data, key))

    def move(self, direction):
        """
        Simplified interface for drone movement, built on tellopy.Tello
        movement methods.
        """
        if direction == 'forward':
            self.drone.forward(0.5)
        elif direction == 'back':
            self.drone.back(0.5)
        elif direction == 'left':
            self.drone.left(0.5)
        elif direction == 'right':
            self.drone.right(0.5)
        elif direction == 'up':
            self.drone.up(0.5)
        elif direction == 'down':
            self.drone.down(0.5)

    def rotate(self, direction):
        """
        Simplified interface for drone rotation, built on tellopy.Tello
        clockwise and counterclockwise methods.
        """
        if direction == 'clockwise':
            self.drone.clockwise(90)
        else:
            self.drone.counter_clockwise(90)

    def takeoff(self):
        """port to Tellopy takeoff method"""
        self.drone.takeoff()

    def land(self):
        """port to Tellopy land method"""
        self.drone.land()

    def query(self):
        """Return dict of latest value for every key in flight_info."""
        latest_status = {}
        for key in self.flight_info:
            latest_status[key] = self.flight_info[key][-1]
        return latest_status

    def get_video_frames(self):
        """collect frames from drone video stream."""
        retry = 3
        container = None
        while container is None and retry > 0:
            retry -= 1
            try:
                container = av.open(self.drone.get_video_stream())
            except av.AVError as ave:
                print(ave)
                print('retry...')

        # skip first 300 frames
        frame_skip = 300
        while True:
            for frame in container.decode(video=0):
                if frame_skip > 0:
                    frame_skip = frame_skip - 1
                    continue
                start_time = time.time()
                yield cv2.cvtColor(numpy.array(frame.to_image()), cv2.COLOR_RGB2BGR)
                if frame.time_base < 1.0/60:
                    time_base = 1.0/60
                else:
                    time_base = frame.time_base
                frame_skip = int((time.time() - start_time)/time_base)
