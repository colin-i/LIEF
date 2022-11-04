
#lief requires MIN_SETUPTOOLS_VERSION = "31.0.0"
#we don't have that on xenial, but lief is not required there, but can't trick the builder to skip lief
#	solution: build a dummy lief


pkname='lief'

ver='1.0.0'

from setuptools import setup
setup(name=pkname,
	version=ver,
	packages=[pkname],
	#
	entry_points = {
		'console_scripts': [pkname+'='+pkname+'.main:main']
	}
)
