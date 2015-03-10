from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='ProjectCodeforces',

	version='0.1.0',

	description='custom build for sublime to take testcases from codeforces.com and check',
	long_description=long_description,

	# The project's main homepage.
	url='https://github.com/vasanthaganeshk/sublime-plugin-for-codeforces',

	author='Vasantha Ganesh k',
	author_email='vasanthaganesh.k@gmail.com',

	license='GNU-GPL-V3.0',

	classifiers=[

		'Development Status :: 3 - Alpha',

		'Intended Audience :: Developers',
		'Topic :: HTMLParsing Codeforces :: Build Tools',

		'License :: OSI Approved :: GNU-GPL-V3 License',

		'Programming Language :: Python :: 2.7',
	],

	keywords='sublime plugin for codeforces',

	packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
	#packages=find_packages(ProjectCodeforces),

)
