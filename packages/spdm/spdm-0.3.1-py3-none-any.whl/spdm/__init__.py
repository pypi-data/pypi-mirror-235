__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from importlib.metadata import version, PackageNotFoundError

from .__version__ import __version__
