"""""" # start delvewheel patch
def _delvewheel_patch_1_5_1():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'sasktran2.libs'))
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-sasktran2-0.0.1')
        if os.path.isfile(load_order_filepath):
            with open(os.path.join(libs_dir, '.load-order-sasktran2-0.0.1')) as file:
                load_order = file.read().split()
            for lib in load_order:
                lib_path = os.path.join(os.path.join(libs_dir, lib))
                if os.path.isfile(lib_path) and not ctypes.windll.kernel32.LoadLibraryExW(ctypes.c_wchar_p(lib_path), None, 0x00000008):
                    raise OSError('Error loading {}; {}'.format(lib, ctypes.FormatError()))


_delvewheel_patch_1_5_1()
del _delvewheel_patch_1_5_1
# end delvewheel patch

from ._version import __version__
from ._core import Config
from ._core import InterpolationMethod, GeometryType, MultipleScatterSource
from ._core import Geometry1D
from ._core import ViewingGeometry
from ._core import TangentAltitudeSolar, GroundViewingSolar
from ._core import Surface

from ._core import AtmosphereStorageStokes_1, AtmosphereStorageStokes_3
from ._core import AtmosphereStokes_1, AtmosphereStokes_3
from .atmosphere import Atmosphere

from ._core import OutputIdealStokes_1, OutputIdealStokes_3
from .output import Output, OutputIdeal

from ._core import EngineStokes_1, EngineStokes_3
from .engine import Engine

from . import appconfig, optical, constituent, climatology, test_util
