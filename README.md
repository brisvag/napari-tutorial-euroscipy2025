# napari fundamentals tutorial

This tutorial goes over the fundamentals of using napari for the interactive analysis of imaging data.
It covers how to use layers, how to quickly generate interactive GUI elements for your processing functions, and how to integrate more complex features such as mouse callbacks.

By the end, we will package everything into a working plugin that can be easily shared on PyPI and the [napari-hub](https://napari-hub.org/).

<img width="1275" height="808" alt="image" src="https://github.com/user-attachments/assets/c7d6f8ad-d79c-468c-960a-fb60efd17829" />


## Installation instruction

In this tutorial we assume usage of [`uv`](https://docs.astral.sh/uv/) for environment management. 
If you prefer to use `conda` or `pip`, then you may use our [installation instructions](https://napari.org/stable/tutorials/fundamentals/installation.html#napari-installation) 

To setup your workspace:

1. Install `uv` (here instruction https://docs.astral.sh/uv/#installation) 
2. Clone (`git clone https://github.com/brisvag/napari-tutorial-euroscipy2025.git`) or [download](https://github.com/brisvag/napari-tutorial-euroscipy2025/archive/refs/heads/main.zip) the repository
3. Go into the project directory
4. Execute `uv sync`
5. Check if everything works by executing `uv run napari`. If the application starts your environment is ready!

You may activate the environment by typing (this is not necessary when running commands via `uv run ...`)
* [Linux/MacOs] `source .venv/bin/activate`
* [Windows] `venv\Scripts\activate.bat` (or `venv\Scripts\Activate.ps1` if using PowerShell)

To deactivate, simply execute `deactivate`.

## Tutorial

The tutorial is structured in a few self-contained python script (named `01_*` to `08_*`) showcasing a typical explorative process where we build a custom napari plugin, with the goal of interactively performing and optimizing a segmentation procedure on some imaging data.

We start from a simple but non-interactive pure python function, and we integrate it step by step with napari, converting it to a GUI widget, customizing it, and adding extra steps.

We end up with two widgets that allow us to interactively find and apply the best parameters for cell segmentation on our sample data.

Finally, we use the [napari plugin template](https://github.com/napari/napari-plugin-template#napari-plugin-template) to convert our code into a plugin, ready to publish on PyPI and share with the community (for a sneak-peek of the final product, see [this repo](https://github.com/brisvag/napari-tutorial-euroscipy2025-plugin)).

## See also

### napari from Jupyter notebook

If you want to try out napari from a jupyter notebook, you also need to install jupyterlab:

```sh
uv sync --group jupyter
```

and then run it with

```sh
uv run jupyter lab napari_from_notebook.ipynb
```

### napari-animation

To test out the [napari-animation](https://github.com/napari/napari-animation) plugin, sync with 

```sh
uv sync --group animation
```

### Useful links

- [Getting started with napari](https://napari.org/stable/tutorials/start_index.html)
- [Examples gallery](https://www.napari-hub.org/)
- [Magicgui](https://pyapp-kit.github.io/magicgui/)
- [Using and creating plugins](https://napari.org/stable/plugins/index.html) and the [napari hub](https://www.napari-hub.org/)
- [Contributing to napari](https://napari.org/stable/developers/index.html)
- We are always active on the [zulip chat](https://www.napari-hub.org/) for questions and advice!
