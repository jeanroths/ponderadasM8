from setuptools import find_packages, setup

package_name = 'my_chatbot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jeanlucasrothsteinmachado',
    maintainer_email='jean.machado@sou.inteli.edu.br',
    description='pacote chatbot',
    license='CC0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'chatnode = my_chatbot.chatnode:main'
        ],
    },
)
