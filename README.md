
# Monocular drone (Tello) localization
### 2022 DGMD S-17 Robotics, Autonomous Vehicles, Drones, and Artificial Intelligence @ Harvard University Extension School

**Team Members:** Daniel Lebedinsky, Claire Peters, Yangsoo Song, John Ward
#### Overview
Simultaneous Localization and Mapping (SLAM) has become the foundation of a self-navigating system. However, it is hard to navigate and detect its localization in indoor environments for small drones with just a frontal monocular camera. As a final project for the class, we will create a program where given an arbitrary launch point, the drone should be able to determine its position and orientation in a known room.

#### Background
We intend to create a system that would allow the Tello drone to determine its location using the camera feed alone. This drone does not come with a GPS, LiDAR, or any other geolocation system pre-installed, and only has one camera, so it does not have a way to directly perceive depth. This poses a challenge to identifying distance to walls and other obstacles.
To implement a SLAM system that can work within the Tello’s material constraints, we will use the  library YOLO, which can identify various objects in a video stream with computer vision, and another library that can compute distance from a monocular camera to a given object in the field of view (likely MiDaS or fast-depth). We will combine their functionality to create a program that can locate a marker, ie a sign, and take off facing the sign. Once we are able to control the vertical motion so that the drone rises to the level of the sign, we can rotate the drone, making it orient itself in the room by identifying distances from itself to other objects. We will then direct the drone to move towards a target and take a photo, while avoiding objects in its path.

#### Hardeware Used
[Tello](https://www.ryzerobotics.com/tello), a mini drone equipped with an HD camera. 

Proposal
---
#### https://docs.google.com/document/d/1O5AGPdEM5yHExTr-1Uiikc-4K_LPvO8e1A04pVEgl_Y/edit

Videos / Presentation
---
#### https://www.youtube.com/watch?v=NTBuCxX9tlA

Report
---
#### https://docs.google.com/document/d/1SZOcqcu_vET3Nv1ERcdWgQcP3W2ia9YvJJeHt1oc_AI/edit

# Documentation

Getting Started - MacOS (x86-64 & ARM)
---
####

1. Clone the repo:

```
$ git clone git@github.com:yangsoosong/drone-localization.git
```

2. Make sure homebrew's installed. If not,

```sh
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Make sure Docker Desktop's installed. If not,

```
$ brew install --cask docker
```

4. Open Docker.app. Wait for it to start up, and allow privileged access and provide your password if prompted.

5. Generate Personal Access Token (PAT) if you already don't have one -> [Creating a Personal Access Token](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

6. Run below command to access docker container
```
echo TOKEN_HERE | docker login ghcr.io -u USERNAME --password-stdin
```

7. Run `./run-notebook.sh` in the project directory (for example, `~/drone-localization`).

8. Copy the http://127.0.0.1:8890 URL and paste it into a browser to open Jupyter Lab.

See [here](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry)
if you are having access issue

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
Results of Detection: \
<img src=".github/rdme_onlydet.png" width="300" >

Taking the bounding boxes from Detection, and averaging the depth field values within them: \
<img src=".github/rdme_depth.png" width="300" >

To create the localizer notebook with the detection and depth combined analysis, I had to import the detection and depth files in the beginning, which are included in the environment. \
Unfortunately, do to an indeterminate bug in either my system or the docker environment, I was not able to fly the drone while recording. Despite various attempts to change file permissions and the container setup, I kept getting the message "Notebook localizer.ipynb is not trusted" \
The detection and depth analysis in localizer_cv.ipynb was performed on still frames after they were taken from the drone. If there was more time for this project, the next step would have been to analyze the photos as they were being taken during the flight of the drone, and estimate the distance from the drone to various objects. \
