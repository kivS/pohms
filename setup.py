from setuptools import setup

setup(
    name='pOhms',
    version='2019.0.1.0',
    author='Vik Borges',
    author_email='v1k@protonmail.com',
    py_modules=['pohms'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pohms=pohms:main_cli
    '''
)
