#!/usr/bin/env python3

import napari
from napari.utils._units import get_unit_registry

img_name = 'napari_fundamentals.tiff'

viewer = napari.Viewer()
viewer.open(img_name, scale=(100, 1, 1), interpolation3d='nearest')
viewer.dims.point = (0, 0, 0)
get_unit_registry().define('happiness = 1')
viewer.scale_bar.unit = 'happiness'
viewer.scale_bar.position = "bottom_left"
viewer.reset_view()
napari.run()
