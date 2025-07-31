from skimage import measure, morphology, data, segmentation, filters
import napari
import numpy as np
from magicgui import magicgui
from scipy import ndimage as ndi


@magicgui(
    auto_call=True,
    sigma={'widget_type': 'FloatSlider', 'min': 0, 'max': 2, 'step': 0.1},
    threshold={'widget_type': 'FloatSlider', 'min': 0, 'max': 1, 'step': 0.05},
    min_hole_size={'widget_type': 'Slider', 'min': 0, 'max': 1000, 'step': 50},
    min_obj_size={'widget_type': 'Slider', 'min': 0, 'max': 1000, 'step': 50},
)
def threshold(
    layer: napari.layers.Image,
    sigma: float = 0.5,
    threshold: float = 0.4,
    min_hole_size: int = 0,
    min_obj_size: int = 0,
) -> list[napari.types.LayerDataTuple]:
    if not layer:
        return
    norm = (layer.data - np.min(layer.data)) / np.max(layer.data)
    # a small gaussian blur helps with getting rid of lots of noise (important in 3D for holes)
    blur = filters.gaussian(norm, sigma=sigma)
    blobs = blur >= threshold
    filled = morphology.remove_small_holes(blobs, min_hole_size)
    cleaned = morphology.remove_small_objects(filled, min_obj_size)
    labels = measure.label(cleaned)

    props = measure.regionprops_table(labels, properties=['label', 'area', 'centroid'])
    centroids = np.array([props[f'centroid-{i}'] for i in range(norm.ndim)]).T
    return [
        (blobs, {'name': 'blobs'}, 'image'),
        (filled, {'name': 'filled'}, 'image'),
        (cleaned, {'name': 'cleaned'}, 'image'),
        (labels, {'name': 'result', 'features': props}, 'labels'),
        (centroids, {'name': 'centroids', 'features': props}, 'points'),
    ]


@magicgui
def watershed(
    markers: napari.layers.Points,
    labels: napari.layers.Labels,
) -> napari.types.LayerDataTuple:
    if not markers or not labels:
        return
    base_labels = labels.data != 0
    distance_field = ndi.distance_transform_edt(base_labels)
    markers_array = np.zeros_like(base_labels, dtype=bool)
    markers_array[tuple(markers.data.astype(int).T)] = True
    markers = ndi.label(markers_array)[0]
    watershedded = segmentation.watershed(-distance_field, markers, mask=base_labels)
    return [
        (watershedded, {'name': 'watershed'}, 'labels'),
    ]


if __name__ == "__main__":
    v = napari.Viewer()
    v.add_image(data.cells3d()[30, 1])  # 2d
    # v.add_image(data.cells3d()[:, 1])  # 3d
    v.grid.enabled = True

    v.window.add_dock_widget(threshold)
    v.window.add_dock_widget(watershed)
    napari.run()

