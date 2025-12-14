# Plugin System


## Plugin Usage


The plugin system allows extending `uplt` for visualizing custom objects.
For example, the `DataFrame` plugin enables this code:
```python
import uplt
import pandas as pd


car_crashes = pd.read_csv(
    'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/car_crashes.csv'
)

fig = uplt.figure()
fig.plot(car_crashes[['total', 'speeding', 'alcohol', 'no_previous']])
fig.show()
```
<picture align="left">
    <img src='https://media.githubusercontent.com/media/dimk90/uplt/refs/heads/main/gallery/asset/plugin.png' width='480'>
</picture>


## Plugin Implementation


To implement the plugin, you can follow this structure:
```python
import numpy as np
import pandas as pd

import uplt.plugin as plugin


class DataFramePlugin(plugin.IPlotPlugin):

    def extract_data(self, obj: pd.DataFrame) -> list[plugin.PlotData]:
        data = []
        for name in obj.columns:
            if not np.issubdtype(obj.dtypes[name], np.number): continue
            y = obj[name].values
            x = np.arange(len(y))
            data.append(plugin.PlotData(x=x, y=y, name=name.replace('_', ' ').title()))
        return data


# Register the plugin for DataFrame objects
plugin.register(pd.DataFrame, handler=DataFramePlugin())
```


## Advanced Plugin Example

While `extract_data` handles the raw values, the `update_style` method gives you fine-grained control over how those values are presented. This allows for dynamic behavior based on the plotting context (e.g. the current data index, total number of datasets, or user-provided arguments).
The example below demonstrates a smart legend implementation. When a user creates a plot with a specific uniform color (e.g. `color='green'`), it is redundant to list every column in the legend individually. Instead, this plugin:
- Detects "Single Color Mode": Checks if a color argument is present.
- Merges Labels: Joins all column names into a single string (stored in `self._joined_name`).
- Cleans the Legend: Hides the legend entries for all lines except the last one, creating a cleaner, unified label for the entire group.

```python
class DataFramePluginAdvanced(plugin.IPlotPlugin):
    """
    DataFrame plugin with advanced style processing
    """

    def __init__(self):
        # Joint name for all data in DataFrame
        self._joined_name = None


    def extract_data(self, obj: pd.DataFrame) -> list[plugin.PlotData]:
        data = []
        joined_name = []
        for name in obj.columns:
            if not np.issubdtype(obj.dtypes[name], np.number):
                continue
            y = np.asarray(obj[name].values)
            x = np.arange(len(y))
            name = name.replace('_', ' ').title()
            joined_name.append(name)
            data.append(plugin.PlotData(x=x, y=y, name=name))
        self._joined_name = ' | '.join(joined_name)
        return data


    def update_style(self, plot_type : plugin.PlotType,
                           data_index: int,
                           data_count: int,
                           data_name : str | None,
                           group_name: str | None,
                           **kwargs) -> dict:
        name = kwargs.get('name', None)
        if name is not None:
            return kwargs

        kwargs['name'] = data_name

        if kwargs.get('color', None) is not None:
            # Single color mode:
            #   - the one legend entry will be shown for all datasets.
            #    (no reason to have multiple entries with a single color)
            #   - all names for the data will be combined into one.
            if data_index == data_count - 1:
                # Set the combined name for the last dataset only
                kwargs['name'] = self._joined_name
            else:
                kwargs['name'] = None
            # Combine everything into the same legend group (plotly)
            kwargs['legend_group'] = self._joined_name

        return kwargs


# Register plugin
plugin.register(pd.DataFrame, handler=DataFramePluginAdvanced())


# Visualize DataFrame in single color mode
fig.plot(car_crashes[['total', 'speeding', 'alcohol', 'no_previous']], color='green')
```
