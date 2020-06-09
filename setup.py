from setuptools import setup, find_packages

setup(
    name='Binge Planner',
    version='0.1.0dev',
    packages=find_packages(exclude=['tests*']),
    install_requires=['click'],
    entry_points = {
        'console_scripts': [
            'bingeplan=bingeplanner.cli:cli'
        ],
    },
    license='License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    description='Calculate how long a binge watch session will take',
    long_description=open('README.md').read(),
    author='Mathias Wagner Nielsen',
    author_email='mathiasvalentinwagner@gmail.com'
)