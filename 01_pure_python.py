from skimage import data, filters
import napari
import numpy as np


def threshold(
    data: np.ndarray,
    sigma: float = 0.5,
    threshold: float = 0.3,
) -> np.ndarray:
    """Apply a gaussian filter and threshold to image data."""
    norm = (data - np.min(data)) / np.max(data)
    # a small gaussian blur helps with getting rid of lots of noise (important in 3D for holes)
    blur = filters.gaussian(norm, sigma=sigma)
    blobs = blur >= threshold

    return blobs


if __name__ == "__main__":
    viewer = napari.Viewer()
    image = data.cells3d()[30, 1]  # 2d
    image_layer = viewer.add_image(image)

    blobs = threshold(image_layer.data, sigma=1, threshold=0.5)
    blobs_layer = viewer.add_labels(blobs)

    napari.run()
