sudo apt update
# sudo apt install -y libgtk2.0-dev pkg-config
sudo apt install ffmpeg libsm6 libxext6  -y
python -m pip install --upgrade pip 
pip install --user -r ./.devcontainer/requirements.txt
