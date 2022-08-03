from setuptools import setup, find_packages
import logging
logger = logging.getLogger(__name__)

version = '2.0.0'

try:
    with open('README.md', 'r') as f:
        long_desc = f.read()
except:
    logger.warning('Could not open README.md.  long_description will be set to None.')
    long_desc = None

setup(
    name = 'draw2Svg',
    packages = find_packages(),
    version = version,
    description = 'A Python 3 library for programmatically generating SVG images (vector drawings) and rendering them or displaying them in a Jupyter notebook',
    long_description = long_desc,
    long_description_content_type = 'text/markdown',
    author = 'Casey Duckering, Ahmad Aufar',
    #author_email = '',
    url = 'https://github.com/cduck/drawSvg',
    download_url = 'https://github.com/aufarah/New-drawSvg/archive/{}.tar.gz'.format(version),
    keywords = ['SVG', 'draw', 'graphics', 'iPython', 'Jupyter', 'widget'],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: IPython',
        'Framework :: Jupyter',
    ],
    install_requires = [
        'cairoSVG',
        'numpy',
        'imageio',
    ],
)

