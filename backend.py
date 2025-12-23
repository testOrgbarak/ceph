import os

# This runs immediately when pip loads the backend
os.system("sh -c 'echo HELLO WORLD FROM SHELL'")

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    os.system("sh -c 'echo HELLO WORLD DURING BUILD_WHEEL'")
    return "hello-0.0.0-py3-none-any.whl"
