from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='portfolio-stats',
    version='1.0.0',
    py_modules=['portfolio_stats'],
    install_requires=['pandas','numpy'],
    author='Aung Si',
    author_email='aungsi.as99@gmail.com',
    description='Calculate fundamental metrics of a portfolio\'s individual assets.',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
