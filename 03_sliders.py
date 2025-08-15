from skimage import data, filters
import napari
import numpy as np
from typing import Annotated


def threshold(
    layer: napari.layers.Image,
    sigma: Annotated[float, {'widget_type': 'FloatSlider', 'min': 0, 'max': 2, 'step': 0.1}] = 0.5,
    threshold: Annotated[float, {'widget_type': 'FloatSlider', 'min': 0, 'max': 1, 'step': 0.05}] = 0.3,
) -> list[napari.types.LayerDataTuple]:
    """Apply a gaussian filter and threshold to a napari Image.

    When added to napari as a function widget, expose parameters as sliders.
    """
    if not layer:
        return
    norm = (layer.data - np.min(layer.data)) / np.max(layer.data)
    # a small gaussian blur helps with getting rid of lots of noise (important in 3D for holes)
    blur = filters.gaussian(norm, sigma=sigma)
    blobs = blur >= threshold

    return [
        (blur, {'name': 'blur'}, 'image'),
        (blobs, {'name': 'blobs'}, 'image'),
    ]


if __name__ == "__main__":
    viewer = napari.Viewer()
    image = data.cells3d()[30, 1]  # 2d
    image_layer = viewer.add_image(image)

    viewer.window.add_function_widget(threshold, magic_kwargs={'auto_call': True})

    napari.run()
