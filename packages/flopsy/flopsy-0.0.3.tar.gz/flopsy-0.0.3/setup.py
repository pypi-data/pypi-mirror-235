

# build with 'python ./setup.py install'
from distutils.core import setup

VERSION = "0.0.3"

setup(
    name = 'flopsy',
    version = VERSION,
    license = 'MIT',
    description = 'Redux-inspired state management',
    author = 'Bill Gribble',
    author_email = 'grib@billgribble.com',
    url = 'https://github.com/bgribble/flopsy',
    download_url = 'https://github.com/bgribble/flopsy/archive/refs/tags/0.0.3.tar.gz',
    keywords = ['state-management', 'redux', 'saga'],
    install_requires = [
        'pyopengl', 'glfw', 'imgui[glfw]',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
    ],
)
