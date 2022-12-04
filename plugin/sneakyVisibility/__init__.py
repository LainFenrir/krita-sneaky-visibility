# For autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *

from .sneakyVisibility import SneakyVisibility


Krita.instance().addExtension(SneakyVisibility(Krita.instance()))
