"""
    changes layer visibility without adding to the undo stack
    Copyright (C) 2022  LunarKreatures

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# For autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *
else:
    from krita import *
from .kritaUtils import getSelectedLayers,refreshProjection

class SneakyVisibility(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    # Krita.instance() exists, so do any setup work
    def setup(self):
        pass

    # called after setup(self)
    def createActions(self, window):
        action = window.createAction("toggleSneakyLayerVisibility", "Changes layer visibility of selected layers", "layer")
        action.triggered.connect(self.toggleSneakyLayerVisibility)
        pass

    def toggleSneakyLayerVisibility(self):
        # we grab selected layers so we can change multiple layers at once
        selectedLayers = getSelectedLayers()
        # If somehow no layer is selected just return
        if len(selectedLayers) == 0:
            return
        
        for layer in selectedLayers:
            # setVisible changes are not added to the undoStack 
            # (if this is a bug please krita devs dont fix it! 
            # if people want to add to the undo stack they can already trigger the action)
            layer.setVisible(not layer.visible())
        # changing the visibility alone doesnt update the projection so we need to refresh
        refreshProjection()
        pass
        