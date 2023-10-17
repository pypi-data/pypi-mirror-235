import pytest
import abc
import numpy as np
import matplotlib.axes
import matplotlib.artist
import matplotlib.pyplot as plt
import astropy.units as u
import named_arrays as na
import optika.plotting
from . import test_mixins


kwargs_plot_parameterization = [
    dict(),
    dict(color="red"),
]


class AbstractTestPlottable(abc.ABC):
    @pytest.mark.parametrize(
        argnames="ax",
        argvalues=[
            None,
            plt.subplots()[1],
        ],
    )
    @pytest.mark.parametrize(
        argnames="transformation",
        argvalues=test_mixins.transformation_parameterization[:2],
    )
    class TestPlot(abc.ABC):
        def test_plot(
            self,
            a: optika.plotting.Plottable,
            ax: None | matplotlib.axes.Axes | na.ScalarArray,
            transformation: None | na.transformations.AbstractTransformation,
        ):
            result = a.plot(
                ax=ax,
                transformation=transformation,
            )

            if ax is None or ax is np._NoValue:
                ax_normalized = plt.gca()
            else:
                ax_normalized = ax
            ax_normalized = na.as_named_array(ax_normalized)

            for index in ax_normalized.ndindex():
                assert ax_normalized[index].ndarray.has_data()

            assert isinstance(result, (na.AbstractScalar, dict))
