import marimo

__generated_with = "0.18.3"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Gallery
    """)
    return


@app.cell
def _():
    import uplt
    return (uplt,)


@app.cell(hide_code=True)
def _():
    import numpy as np
    return (np,)


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _():
    from pathlib import Path
    return (Path,)


@app.cell(hide_code=True)
def _(mo):
    engine = mo.ui.dropdown(options=['matplot', 'plotly'],
                            value='matplot',
                            allow_select_none=False,
                            label='Engine:')
    engine
    return (engine,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # plot
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2d
    """)
    return


@app.cell
def _(engine, np, uplt):
    _x_ = np.linspace(0, np.pi*4, num=100)
    _y1_ = np.sin(_x_)
    _y2_ = np.sin(_x_ - np.pi/4)
    _y3_ = np.sin(_x_ - 2*np.pi/4)
    _y4_ = np.sin(_x_ - 3*np.pi/4)

    (
    uplt.figure(engine.value)
        .plot(_x_, _y1_, name='data #1')
        .plot(_x_, _y2_, name='data #2')
        .plot(_x_, _y3_, name='data #3')
        .plot(_x_, _y4_, name='data #4')
        .xlabel('X')
        .ylabel('Y')
        .legend()
        .show()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3d
    """)
    return


@app.cell
def _(engine, np, uplt):
    _x_ = np.linspace(0, np.pi*4, num=100)
    _y1_ = np.sin(_x_)
    _y2_ = np.sin(_x_ - np.pi/4)

    (
    uplt.figure(engine.value)
        .plot(x=_y1_, y=_y2_, z=_x_, name='data #1')
        .plot(x=_y1_, y=_y2_, z=_x_+2, name='data #2')
        .plot(x=_y1_, y=_y2_, z=_x_+4, name='data #1')
        .legend()
        .show()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # scatter
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2d
    """)
    return


@app.cell
def _(engine, np, uplt):
    _x_ = np.random.uniform(size=100)
    _y_ = np.random.uniform(size=100)


    uplt.figure(engine.value).scatter(_x_, _y_).show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2d - Color per Point
    """)
    return


@app.cell
def _(engine, np, uplt):
    _x_ = np.random.uniform(size=100)
    _y_ = np.random.uniform(size=100)
    # random color per point
    _rgb_colors_ = np.random.uniform(low=0.1, high=0.8, size=[100, 3])


    uplt.figure(engine.value).scatter(_x_, _y_, color=uplt.color.rgb_to_str(_rgb_colors_)).show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3d
    """)
    return


@app.cell
def _(engine, np, uplt):
    _z_ = np.linspace(0, np.pi*4, num=100)
    _x_ = np.sin(_z_)
    _y_ = np.sin(_z_ - np.pi/4)

    (
    uplt.figure(engine.value)
        .scatter(_x_, _y_, _z_, name='data #1')
        .scatter(_x_, _y_, _x_-5, name='data #2')
        .legend()
        .show()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3d - Color per Point
    """)
    return


@app.cell
def _(engine, np, uplt):
    _z_ = np.linspace(0, np.pi*4, num=100)
    _x_ = np.sin(_z_)
    _y_ = np.sin(_z_ - np.pi/4)

    _rgb_colors_ = np.random.uniform(low=0.1, high=0.9, size=[100, 3])


    uplt.figure(engine.value).scatter(_x_, _y_, _z_, color=uplt.color.rgb_to_str(_rgb_colors_)).show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # surface3d
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Uniform Grid
    """)
    return


@app.cell
def _(engine, np, uplt):
    _x_ = np.arange(0, 5, 0.25)
    _y_ = np.arange(-5, 5, 0.25)
    _X_, _Y_ = np.meshgrid(_x_, _y_)
    _Z_ = np.sin(np.sqrt(_X_**2 + _Y_**2))

    (
    uplt.figure(engine.value, aspect_ratio=0.7)
        .surface3d(_x_, _y_, _Z_,   name='data #1', colormap='twilight')
        .surface3d(_x_, _y_, _Z_*6, name='data #2', show_colormap=True)
        .xlabel('X Axis')
        .ylabel('Y Axis')
        .zlabel('Z Axis')
        .legend()
        .show()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Non-uniform Grid
    """)
    return


@app.cell
def _(engine, uplt):
    # non-uniform grid (array of points)
    _x_ = [ 0, 1, 2, 0, 2, 1, 0, 1, 2 ]
    _y_ = [ 0, 1, 2, 2, 0, 0, 1, 2, 1 ]
    # values
    _z_ = [ 1, 1, 1, 1, 1, 0, 0, 0, 0 ]

    (
    uplt.figure(engine.value)
        .surface3d(_x_, _y_, _z_, name='data #1', colormap='hsv', opacity=0.5, show_colormap=True)
        .surface3d(_x_, _y_, _z_, name='data #2',  interpolation='linear', show_colormap=True)
        .xlabel('X Axis')
        .ylabel('Y Axis')
        .zlabel('Z Axis')
        .legend()
        .show()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # bar
    """)
    return


@app.cell
def _(engine, np, uplt):
    _y1_ = np.arange(5) + 1


    uplt.figure(engine.value).bar(_y1_, color='r').show()
    return


@app.cell
def _(engine, np, uplt):
    _y1_ = np.arange(5) + 1
    _y2_ = _y1_[::-1]
    _x_ = [ 'A', 'B', 'C', 'AABB', 'D' ]


    (
    uplt.figure(engine.value)
        .bar(_x_, _y1_, name='T1')
        .bar(_x_, _y2_, name='T2')
        .bar(_x_, [1, 1, 1, 1, 1], opacity=0.5, name='T3')
        .ylim(0, 8)
        .hline(3, color='r', line_style='--')
        .legend()
        .show()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # hline & vline
    """)
    return


@app.cell
def _(engine, np, uplt):
    _x_ = np.linspace(0, 8*np.pi, num=200)
    _y_ = np.cos(_x_)

    (
    uplt.figure(engine.value)
        .plot(_x_, _y_, name='cos')

        .ylim(-2, 2)
        .xlim(-2*np.pi)

        .hline(y=0.5, x_min=10, x_max=15, line_style='--')
        .hline(y=-0.3, line_style='--')

        .vline(x=np.pi+np.pi/2, y_min=-0.5, y_max=0.5, line_style='--')
        .vline(x=4*np.pi, line_style='--')

        .xlabel('X Axis')
        .ylabel('Y Axis')

        .legend()
        .show()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # log-scale
    """)
    return


@app.cell
def _(engine, np, uplt):
    _x_ = np.linspace(0, 100000, num=1000)
    _y_ = np.sqrt(_x_)


    (
    uplt.figure(engine.value)
        .plot(_x_, _y_, name='sqrt(x)')
        .xscale('log', base=10)
        .yscale('log', base=10)
        .hline(y=100, line_style='--', color='r')
        .vline(x=10000, line_style='--', color='r')
        .xlim(100)
        .ylim(10)
        .legend()
        .show()
    )
    return


@app.cell
def _(engine, np, uplt):
    _x_ = np.linspace(0, 100000, num=1000)
    _y_ = np.sqrt(_x_)


    (
    uplt.figure(engine.value)
        .plot(_x_, _y_, name='sqrt(x)')
        .xscale('log', base=2)
        .xlim(2)
        .hline(y=150, line_style='--', color='r')
        .legend()
        .show()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # legend
    """)
    return


@app.cell
def _(engine, np, uplt):
    _x_ = np.arange(8)
    _y_ = np.arange(8)


    (
    uplt.figure(engine.value)
        .scatter(_x_, _y_, marker_style='.', marker_size=1, name='data #1', legend_group='Small')
        .scatter(_x_, _y_+1, marker_style='s', marker_size=6, name='data #2', legend_group='Small')
        .scatter(_x_, _y_-1, marker_style='v', marker_size=10, name='data #3', legend_group='Small')
        .scatter(_x_, _y_+3, marker_style='x', marker_size=25, name='data #4', legend_group='Big')
        .plot(_x_, _y_-3, marker_style='o', marker_size=25, name='data #5', legend_group='Big')
        .legend(True, equal_marker_size=True)
        .show()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # heatmap
    """)
    return


@app.cell
def _(engine, mo, np, uplt):
    # Generate heatmap for visualization
    _range_ = np.linspace(-10, 10, num=101, endpoint=True)
    _xx_, _yy_ = np.meshgrid(_range_, _range_, indexing='xy')
    _z_ = _xx_**3 + _yy_**3


    mo.vstack([
        mo.hstack([ mo.md('## Vertical Colorbar'), mo.md('## Horizontal Colorbar') ],  justify='space-around'),

        mo.hstack([
            uplt.figure(engine.value, width=400, aspect_ratio=0.8).heatmap(_z_, colorbar='vertical').show(),
            uplt.figure(engine.value, width=500, aspect_ratio=0.8).heatmap(_z_, colorbar='horizontal').show(),
        ])
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # imshow
    """)
    return


@app.cell(hide_code=True)
def _():
    from PIL import Image
    return (Image,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Color Image
    """)
    return


@app.cell
def _(Image, Path, engine, np, uplt):
    _image_ = Image.open(Path(__file__).parent.parent / 'logo.png')
    _image_ = np.array(_image_)


    uplt.figure(engine.value, width=250).imshow(_image_).show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grayscale Image
    """)
    return


@app.cell
def _(Image, Path, engine, uplt):
    _image_ = Image.open(Path(__file__).parent.parent / 'logo.png').convert('L')


    uplt.figure(engine.value, width=250).imshow(_image_).show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # plugin
    """)
    return


@app.cell
def _(np):
    import pandas as pd
    import uplt.plugin as plugin


    class DataFramePlugin(plugin.IPlotPlugin):
        """
        DataFrame minimalistic plugin (only data extraction)
        """

        def extract_data(self, obj: pd.DataFrame) -> list[plugin.PlotData]:
            data = []
            for name in obj.columns:
                if not np.issubdtype(obj.dtypes[name], np.number):
                    continue
                y = np.asarray(obj[name].values)
                x = np.arange(len(y))
                name = name.replace('_', ' ').title()
                data.append(plugin.PlotData(x=x, y=y, name=name))
            return data


    # register plugin
    plugin.register(pd.DataFrame, handler=DataFramePlugin())
    return (pd,)


@app.cell
def _(engine, pd, uplt):
    _car_crashes_ = pd.read_csv(
        'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/car_crashes.csv'
    )

    (
    uplt.figure(engine.value)
        .plot(_car_crashes_[['total', 'speeding', 'alcohol', 'no_previous']])
        .legend().show()
    )
    return


if __name__ == "__main__":
    app.run()
