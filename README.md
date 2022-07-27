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
docker run -t -d --name tello-container --net=host --ipc=host -v `pwd`:/usr/src/app \
-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix tello && docker exec -it tello-container bash
```

After the second command has run, you should be in the container's root environment. 

The container created is persistent, so it can be exited and re-entered as needed. 
Exit with ctrl-D or `exit`, enter with the command `docker exec -it tello-container bash`.

The container created also attaches this repo as a volume, meaning you can add files to this
repo and access them from inside the container. Whatever the program writes to the application folder,
you will be able to access from outside the docker container. This will be useful in getting the 
software that has been written to work correctly in this container.


If you go to the python CLI from the container root environment, you should be able to 
control the drone using tellopy commands.
An example session:

```py
>>> import tellopy
>>> from tester import handleFileReceived
>>> drone = tellopy.Tello()
>>> drone.connect()
>>> drone.wait_for_connection(30.0)
>>> drone.takeoff()
>>> drone.take_picture()
>>> drone.subscribe(drone.EVENT_FILE_RECEIVED, handleFileReceived)
>>> drone.land()
>>> drone.quit()
```
Note that the above has no sleep commands, so it's best to wait for a response before 
running the next command. After running the `connect()` command, you should see your 
Tello's light start flashing green (red, if you're low on battery).

Some issues that still need to be addressed, in order of operation:
1. **ensuring that this setup works on everyone's machines.** There's great enough variance
  among our OSes that I'm expecting some sort of snag. Best to find that sooner rather than later.
  *If you have any issue getting the container to work on your machine when following the above 
  directions alone, report it ASAP.* Others might be able to assist with finding solutions, and I 
  may want to add a note about it to the documentation.
2. **getting video forwarding to work from inside the Docker container.** I'm close to finishing this - 
  I've successfully executed [this](https://gist.github.com/sorny/969fe55d85c9b0035b0109a31cbcb088) 
  tutorial. Barrier is currently difficulty in using openCV to display the binary image output that the 
  tellopy library provides when running e.g. the `take_picture()` command, on a docker container or locally.
  If somebody provides me with simple test code that I can run ad hoc on my local machine, 
  I can probably get this working very quickly. After confirming that this method works for tello output,
  I would move on to [securing the setup](http://wiki.ros.org/docker/Tutorials/GUI#Using_X_server). As
  above, if for some reason some part of this doesn't work for someone's setup, better to find that ASAP.
3. **Implementing John's code inside the container**. Once we're sure everything else works, we can
  commit to using this environment for development.



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
