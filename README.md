# drone-localization
DGMD S-17 Final Project
## Monocular drone (Tello) localization
2022 DGMD S-17 Robotics, Autonomous Vehicles, Drones, and Artificial Intelligence @ Harvard University Extension School

**Team Members:** Daniel Lebedinsky, Yangsoo Song, John Ward, Claire Peters

Environment setup
---
In this directory, run:
```
docker build -t tello .
docker run -t -d --name tello-container --net=host --ipc=host -v `pwd`:/usr/src/app -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix tello && docker exec -it tello-container bash
```

After the second command has run, you should be in the container's root environment.
From there, if you go to the python CLI, you should be able to control the drone
using tellopy commands. For example:

```py
>>> import tellopy
>>> from tester import handleFileReceived
>>> drone = tellopy.Tello()
>>>  drone.connect()
>>>  drone.wait_for_connection(30.0)
>>>  drone.takeoff()
>>>  drone.take_picture()
>>>  drone.subscribe(drone.EVENT_FILE_RECEIVED, handleFileReceived)
>>>  drone.land()
>>>  drone.quit()
```

Proposal
---
#### https://docs.google.com/document/d/1O5AGPdEM5yHExTr-1Uiikc-4K_LPvO8e1A04pVEgl_Y/edit

Videos
---
####

Presentation
---
####

Report
---
####
