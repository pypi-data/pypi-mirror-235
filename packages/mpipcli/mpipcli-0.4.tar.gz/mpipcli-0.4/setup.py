
from setuptools import setup



setup(
    name='mpipcli',
    version='0.4',
    packages=['mpip'],
    entry_points={
        'console_scripts': [
            'mpip = mpip.cli:main',
        ],
    },
    install_requires=[
        'requests'
    ],
)








