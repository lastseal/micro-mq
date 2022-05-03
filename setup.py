from setuptools import setup

setup(
    name="micro-mq",
    version="1.0.0",
    description="",
    author="Lastseal",
    author_email="hello@lastseal.com",
    url="https://www.lastseal.com",
    packages=['micro'],
    install_requires=[ 
        i.strip() for i in open("requirements.txt").readlines() 
    ]
)
