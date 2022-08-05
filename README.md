# drone-localization
DGMD S-17 Final Project
## Monocular drone (Tello) localization
2022 DGMD S-17 Robotics, Autonomous Vehicles, Drones, and Artificial Intelligence @ Harvard University Extension School

**Team Members:** Daniel Lebedinsky, Yangsoo Song, John Ward, Claire Peters


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

# Documentation

Getting started - Linux
---
####
These steps will work for any Linux distribution with systemd.
1. Install Docker Desktop, Earthly, and jupyter lab.
2. In your system terminal, run `sudo usermod -a -G docker $USER`, then reboot.
3. run `sudo systemctl restart docker`, then run `docker ps` to verify that docker is working. You should see a list in all caps starting with "CONTAINER ID".
4. run `earthly +docker && ./run-notebook.sh` in the main branch of the project directory.
5. This will start a length installation process (about 20 minutes). At the end, you may be prompted to reboot. If so, repeat step 3 and run `./run-notebook.sh` in the project directory again.
6. Copy the URL output, paste it into a browser. This will open a jupyter lab.

Detection and Depth Localizer notebook
---
####
To create the localizer notebook with the detection and depth combined analysis, I had to import the detection and depth files in the beginning, which are included in the environment. Unfortunately, do to an indeterminate bug in either my system or the docker environment, I was not able to fly the drone while recording. The detection and depth analysis in localizer_cv.ipynb was performed on still frames after they were taken from the drone. If there was more time for this project, the next step would have been to analyze the photos as they were being taken during the flight of the drone, and estimate the distance from the drone to various objects in its field of vision. 
