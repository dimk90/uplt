"""
Utility functions to detect the current environment: jupyter, marimo, etc.
"""


def is_jupyter() -> bool:
    """
    Check if the current environment is a Jupyter notebook.
    """
    try:
        from IPython.core.getipython import get_ipython

        shell = get_ipython().__class__.__name__

        if shell == 'ZMQInteractiveShell':
            # Jupyter notebook or qtconsole
            return True

    except Exception:
        pass

    return False


def is_marimo() -> bool:
    """
    Check if the current environment is a Marimo notebook.
    """
    try:
        import marimo
        return marimo.running_in_notebook()
    except Exception:
        pass
    return False
