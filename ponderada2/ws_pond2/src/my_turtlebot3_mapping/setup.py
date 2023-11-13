from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_turtlebot3_mapping'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jeanlucasrothsteinmachado',
    maintainer_email='jean.machado@sou.inteli.edu.br',
    description='Mapping and navigation package',
    license='CC0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'navigation_points=my_turtlebot3_mapping.navigation_points:main'
        ],
    },
)
