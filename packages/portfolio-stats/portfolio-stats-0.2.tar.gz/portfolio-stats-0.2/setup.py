from setuptools import setup

setup(
    name='portfolio-stats',
    version='0.2',
    py_modules=['portfolio_stats'],
    install_requires=[
        'pandas',
        'numpy'
    ],
    author='Aung Si',
    author_email='aungsi.as99@gmail.com',
    description='Calculate fundamental metrics of a portfolio\'s individual assets.'
)
