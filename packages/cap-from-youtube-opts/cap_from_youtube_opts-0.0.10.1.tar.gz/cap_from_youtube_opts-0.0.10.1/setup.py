from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='cap_from_youtube_opts',
    version='0.0.10.1',
    license='MIT',
    description='Get an OpenCV video capture from an YouTube video URL + ydl_opts',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ogre0382',
    url='https://github.com/ogre0382/cap_from_youtube_opts',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'yt_dlp',
    ],
)
