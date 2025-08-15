from skimage import data, filters
import napari
import numpy as np


def threshold(
    layer: napari.layers.Image,
    sigma: float = 0.5,
    threshold: float = 0.3,
) -> list[napari.types.LayerDataTuple]:
    """Apply a gaussian filter and threshold to a napari Image."""
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

    viewer.window.add_function_widget(threshold)

    napari.run()
