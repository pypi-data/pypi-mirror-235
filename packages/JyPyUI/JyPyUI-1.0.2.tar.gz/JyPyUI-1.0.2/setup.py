from setuptools import setup, find_packages
#pypi-AgEIcHlwaS5vcmcCJGVlYTAxYWFhLTAyZDUtNGUwOC05YzA5LWZhNWU2YzA4ZDgyOAACKlszLCJhY2Y1MGI2NC1iYWY1LTQ1MzctYTdlYS0wMGMwNDE5Nzk4MDMiXQAABiBOq7PPpSI20hOcKOHCItBC5aRoMq7HUMqVO_WQFjPkIA
setup(
    name= 'JyPyUI',
    version= '1.0.2',
    packages= find_packages(),
    install_requires=[
        'pygame',
        'gtts',
        'plyer',
        'pyjnius'
    ],
)