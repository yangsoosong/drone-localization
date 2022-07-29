# poetry env remove 3.9
# poetry env remove 3.10
# poetry cache clear --all pypi -n
# rm -rf localizer/localizer.egg-info
# rm -rf localizer/src/__pycache__
# rm -rf poetry.lock

# rm -rf env
python3 -m venv env
source env/bin/activate

pip install --upgrade pip
pip install wheel
pip install jupyterlab

export ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future

pip install ./tello --pre
pip install ./depth --pre
pip install ./detection --pre
