# napari fundamentals tutorial

This tutorial goes over the fundamentals of using napari for the interactive analysis of imaging data.
It covers how to use layers, how to quickly generate interactive GUI elements for your processing functions, and how to integrate more complex features such as mouse callbacks.

By the end, we will package everything into a working plugin that can be easily shared on PyPI and the [napari-hub](https://napari-hub.org/).

<img width="1275" height="808" alt="image" src="https://github.com/user-attachments/assets/c7d6f8ad-d79c-468c-960a-fb60efd17829" />


## Installation instruction

In this tutorial we assume usage of [`uv`](https://docs.astral.sh/uv/) for environment management. 
If you prefer to use `conda` or `pip`, then you may use our [installation instruction](https://napari.org/stable/tutorials/fundamentals/installation.html#napari-installation) 

To setup your workspace:

1. Install `uv` (here instruction https://docs.astral.sh/uv/#installation) 
2. Clone (`git clone https://github.com/brisvag/napari-tutorial-euroscipy2025.git`) or [download](https://github.com/brisvag/napari-tutorial-euroscipy2025/archive/refs/heads/main.zip) the repository
3. Go into the project directory
4. Execute `uv sync`
5. Check if everything works by executing `uv run napari`. If the application starts your environment is ready!

You may activate the environment by typing 
* [Linux/MacOs] `source .venv/bin/activate`
* [Windows] `venv\Scripts\activate.bat` (or `venv\Scripts\Activate.ps1` if using PowerShell)

To deactivate, simply execute `deactivate`.

### jupyter notebook

If you want to try out the jupyter notebook, you also need to install jupyterlab:

```sh
uv pip install jupyterlab
```

and then run it with

```sh
jupyter lab napari_from_notebook.ipynb
```
