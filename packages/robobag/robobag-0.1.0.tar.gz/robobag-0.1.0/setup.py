from setuptools import find_packages, setup

setup(
    name='robobag',
    version='0.1.0',
    description='',
    url='',
    author_email='no-reply@gmail.com',
    keywords=[],
    install_requires=[
        'protobuf==3.19.1',
        'pyarrow==6.0.1',
        'opencv-python==4.5.5.64',
        'click==8.0.3',
        'tqdm==4.62.3',
        'av==9.2.0',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'robobag = robobag.cli:cli'
        ]
    },
)
