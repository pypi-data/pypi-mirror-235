from setuptools import setup, find_packages

setup(
  name="mattsollamatools", 
  version="0.0.3", 
  description="Random tools to make building apps with Ollama in Python just a touch easier", 
  packages=find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent"
  ], 
  python_requires=">=3.6"
)