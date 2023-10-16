from setuptools import setup, find_packages
import os
import sys
current_directory = os.getcwd()
sys.path.append(current_directory)
import pdb

dependencies = []

with open("src/requirements.txt", "r", encoding="utf-8") as f:
    dependencies = f.read().splitlines()
# pdb.set_trace()
setup(
    name='PY-4-findex',
    version='0.0.1',
    packages=find_packages(),
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'findex = src.main:main',
        ]
    },
    author='Suhasini, Miloni, Pragya, Supriti, Srinija',
    author_email='sgattu@adobe.com, milonip@adobe.com, pragyag@adobe.com, supritiv@adobe.com, csrinija@adobe.com',
    description='A command line utility to index files based on MIME type',
    url='https://git.corp.adobe.com/supritiv/PY-4-findex',
    license='License',
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)