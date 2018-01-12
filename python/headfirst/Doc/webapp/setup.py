from distutils.core import setup

setup(
	name='test_setting',
	py_modules=['athletemodel','start'],
	packages=['myapp'],
	package_data={'myapp':['*.txt']}
)