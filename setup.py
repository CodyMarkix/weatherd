from setuptools import setup

setup(
	name='weatherd',
	version='0.3',
	description='A basic daemon for fetching data from Open-Meteo',
	author='CodyMarkix',
	author_email='Markix124@protonmail.com',
	packages=['weatherd'],
	install_requires=[
		'requests'
	],
)
