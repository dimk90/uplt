import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell
def _():
    import uplt
    return (uplt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Test Notebook Detection""")
    return


@app.cell
def _():
    from uplt import detect
    return (detect,)


@app.cell
def _(detect):
    detect.is_marimo()
    return


@app.cell
def _(detect):
    detect.is_jupyter()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Data""")
    return


@app.cell
def _(np):
    x = np.linspace(0, np.pi*4, num=100)
    y1 = np.sin(x)
    y2 = np.sin(x - np.pi/4)
    y3 = np.sin(x - 2*np.pi/4)
    y4 = np.sin(x - 3*np.pi/4)
    return x, y1, y2, y3, y4


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Matplotlib""")
    return


@app.cell
def _(mo, uplt, x, y1, y2, y3, y4):
    mpl_fig = (
        uplt.figure('mpl')
        .plot(x, y1, name='data #1')
        .plot(x, y2, name='data #2')
        .plot(x, y3, name='data #3')
        .plot(x, y4, name='data #4')
        .xlabel('X')
        .ylabel('Y')
        .legend()
    )

    mo.md(f'**Matplotlib Image**: {mo.as_html(mpl_fig.show())}').center()
    return


@app.cell
def _(uplt, x, y1, y2, y3, y4):
    (
        uplt.figure('mpl')
        .plot(x, y1, name='data #1')
        .plot(x, y2, name='data #2')
        .plot(x, y3, name='data #3')
        .plot(x, y4, name='data #4')
        .xlabel('X')
        .ylabel('Y')
        .legend()
    ).show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Plotly""")
    return


@app.cell
def _(mo, uplt, x, y1, y2, y3, y4):
    plt_fig = (
        uplt.figure('plotly')
        .plot(x, y1, name='data #1')
        .plot(x, y2, name='data #2')
        .plot(x, y3, name='data #3')
        .plot(x, y4, name='data #4')
        .xlabel('X')
        .ylabel('Y')
        .legend()
    )

    mo.md(f'**Plotly Image**: {mo.as_html(plt_fig.show())}').center()
    return


@app.cell
def _(uplt, x, y1, y2, y3, y4):
    (
        uplt.figure('plotly')
        .plot(x, y1, name='data #1')
        .plot(x, y2, name='data #2')
        .plot(x, y3, name='data #3')
        .plot(x, y4, name='data #4')
        .xlabel('X')
        .ylabel('Y')
        .legend()
    ).show()
    return


if __name__ == "__main__":
    app.run()
