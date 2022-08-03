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

1. Clone the repo:

```
$ git clone git@github.com:yangsoosong/drone-localization.git
```

2. Make sure Docker Desktop's installed. If not, see https://docs.docker.com/desktop/install/linux-install/#generic-installation-steps/. In summary:

   1. Use your system's package manager to install docker-desktop
   2. In your terminal, run `sudo usermod -a -G docker $USER`, then reboot.
   3. run `sudo systemctl restart docker`, then run `docker ps` to verify that docker is working. You should see a list in all caps starting with "CONTAINER ID".

3. Run `./run-notebook.sh` in the project directory (for example, `~/drone-localization`).
4. Copy the http://127.0.0.1:8890 URL and paste it into a browser to open Jupyter Lab.

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
5. Run `./run-notebook.sh` in the project directory (for example, `~/drone-localization`).
6. Copy the http://127.0.0.1:8890 URL and paste it into a browser to open Jupyter Lab.

Localizer
---
####

