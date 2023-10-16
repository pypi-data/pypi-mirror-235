# ruff: noqa: F401
try:
    from importlib_metadata import version
except ImportError:
    from importlib.metadata import version  # type: ignore


from sihl.sihl_model import SihlModel
from sihl.torchvision_backbone import TorchvisionBackbone, ALL_LEVEL_NAMES

TORCHVISION_BACKBONE_NAMES = list(ALL_LEVEL_NAMES.keys())

__version__ = version("sihl")

try:
    from sihl.timm_backbone import TimmBackbone
except ImportError:
    pass

try:
    from sihl.lightning_module import LightningModule
except ImportError:
    pass
