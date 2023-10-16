from setuptools import setup, find_packages

setup(
    name='jblibhack',
    version='1.0.0',
    description='A library for handling Telegram messages',
    author='hacker233',
    author_email='shellcloud18@gmail.com',
    packages=find_packages(),
    install_requires=[
        'telebot',
        'requests',
        # Add any other dependencies here
    ],
)
