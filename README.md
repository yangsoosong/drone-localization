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

Getting Started - MacOS
---
####

1. Make sure homebrew's installed. If not,

```sh
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Make sure Docker Desktop's installed. If not,

```
$ brew install --cask docker
```

3. Open Docker.app. Wait for it to start up, and allow privileged access and provide your password if prompted.

4. And then you can run the script:

```sh
$ ./run-notebook.sh
```

Localizer
---
####

