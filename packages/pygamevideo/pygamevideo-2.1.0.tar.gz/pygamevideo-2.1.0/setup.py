from setuptools import setup, find_packages
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_data(path):
    return os.path.join(_ROOT, path)

setup(
    name="pygamevideo",
    py_modules = ["pygamevideo"],
    include_package_data=True,
    version="2.1.0",
    author="Kadir Aksoy",
    description="Video player for Pygame.",
    url="https://github.com/kadir014/pygamevideo",
    project_urls={
    'Documentation': 'https://github.com/kadir014/pygame-video#api-reference',
    },
    keywords='python pygame video mp4 media',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[
          "pygame-ce",
          "numpy",
          "opencv-python",
          "ffpyplayer"
      ],
)
