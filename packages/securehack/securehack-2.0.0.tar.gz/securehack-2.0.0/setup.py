from setuptools import setup, find_packages

setup(
    name='securehack',
    version='2.0.0',
    author='K233',
    author_email='shellcloud18@gmail.com',
    description='Securehack - Telegram Bot for Server Interaction',
    packages=find_packages(),
    install_requires=[
        'telebot',
        'requests'
    ],
)
