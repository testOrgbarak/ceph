from setuptools import setup
import os

# This runs immediately when setup.py is executed
print("HELLO WORLD FROM setup.py")

# You can also run shell commands
os.system("echo HELLO WORLD FROM SHELL IN setup.py")

setup(
    name="hello-setup",
    version="0.0.1",
    py_modules=["hello"],
)
