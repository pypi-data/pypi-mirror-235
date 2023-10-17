# Simple Python plot

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3106/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Code Coverage](https://codecov.io/gh/a-t-0/snn/branch/main/graph/badge.svg)](https://codecov.io/gh/a-t-0/snnalgorithms)

Call this pip package to easily create:
 - a boxplot
 - a multi-line plot
 - a latex table

## Example Boxplot
```py
python -m simplt --box-plot
```
Which is the same as running:
```py
from simplt.boxplot.boxplot import create_box_plot
import numpy as np

extensions=[
    ".png",
],
filename="example_box",
output_dir="output",

# Fixing random state for reproducibility
np.random.seed(7)

# Generate dummy data.
first = [39, 44, 50, 50, 58, 63]
second = [80, 100, 100, 120]

# Add a name for each boxplot for in the legend, and y values.
y_series = {"data_1": first, "data_2": second}

create_box_plot(
    extensions=extensions,
    filename=filename,
    legendPosition=0,
    output_dir=output_dir,
    x_axis_label="x-axis label [units]",
    y_axis_label="y-axis label [units]",
    y_series=y_series,
)
```

And creates:

<img src="https://github.com/a-t-0/simplt/blob/main/output/example_box.png" width="640" height="480" />

## Example Multi-Line Plot
```py
python -m simplt --line-plot
```
Which is the same as running:
```py
from simplt.line_plot.line_plot import line_plot
import numpy as np

extensions=[
    ".png",
],
filename="example_line",
output_dir="output",

multiple_y_series = np.zeros((2, 2), dtype=int)
# actually fill with data
multiple_y_series[0] = [1, 2]
lineLabels = [
    "first-line",
    "second_line",
]  # add a label for each dataseries
single_x_series = [3, 5]

plot_multiple_lines(
    extensions=extensions,
    filename=filename,
    label=lineLabels,
    legendPosition=0,
    output_dir=output_dir,
    x=single_x_series,
    x_axis_label="x-axis label [units]",
    y_axis_label="y-axis label [units]",
    y_series=multiple_y_series,
)
```

And creates a (colorblind-friendly) lineplot:

<img src="https://github.com/a-t-0/simplt/blob/main/output/example_line.png" width="640" height="480" />

## Example Multi-Group Scatter Plot
```py
python -m simplt --dot-plot
```
Which is the same as running:
```py
from simplt.dotted_plot.dotted_plot import plot_multiple_dotted_groups
import numpy as np

single_x_series = [3., 5.]
multiple_y_series:Dict[int,Dict[float,List[float]]] = {}

# actually fill with data
multiple_y_series[0]={}
multiple_y_series[0][single_x_series[0]] = [1., 2., 5.]
multiple_y_series[0][single_x_series[1]] = [0., 6.]

multiple_y_series[1]={}
multiple_y_series[1][single_x_series[0]] = [3., 4.]
multiple_y_series[1][single_x_series[1]] = [1., 5.]



groupLabels = [
    "first_group",
    "second_group",
]  # add a label for each dataseries

print(multiple_y_series)
plot_multiple_dotted_groups(
    extensions=extensions,
    filename=filename,
    label=groupLabels,
    legendPosition=0,
    output_dir=output_dir,
    x_axis_label="x-axis label [units]",
    y_axis_label="y-axis label [units]",
    y_series=multiple_y_series,
)
```

And creates a (colorblind-friendly) dotplot:

<img src="https://github.com/a-t-0/simplt/blob/main/output/example_dots.png" width="640" height="480" />


## For Developers
Below are pip-package publication instructions.
### Releasing pip package update

To udate the Python pip package, one can first satisfy the following requirements:

```bash
pip install --upgrade pip setuptools wheel
pip install twine
```

Followed by updating the package with:

```bash
python3 setup.py sdist bdist_wheel
python -m twine upload dist/\*
```

### Developer pip install
Build the pip package with:

```bash
pip install --upgrade pip setuptools wheel
pip install twine
```

Install the pip package locally with:

```bash
rm -r dist
rm -r build
python3 setup.py sdist bdist_wheel
pip install -e .
```

Upload the pip package to the world with:

```bash
rm -r dist
rm -r build
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/\*
```


<!-- Un-wrapped URL's (Badges and Hyperlinks) -->
