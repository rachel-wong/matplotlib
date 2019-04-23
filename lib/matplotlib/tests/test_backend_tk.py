import pytest
import numpy as np
from matplotlib import (
    collections, path, pyplot as plt, transforms as mtransforms, rcParams)
from matplotlib.testing.decorators import image_comparison

@pytest.fixture(autouse=True)
def mpl_test_settings(tk_module, mpl_test_settings):
    """
    Ensure tk_module fixture is *first* fixture.

    We override the `mpl_test_settings` fixture and depend on the `qt_module`
    fixture first. It is very important that it is first, because it skips
    tests when Tk is not available, and if not, then the main
    `mpl_test_settings` fixture will try to switch backends before the skip can
    be triggered.
    """
    pass


@pytest.fixture
def tk_module(request):
    backend, = request.node.get_closest_marker('backend').args
    if backend != "TkAgg":
        raise ValueError('Backend marker has unknown value: ' + backend)
    return


@pytest.mark.backend('TkAgg')
@image_comparison(baseline_images=['test_changetitle'],
                  extensions=['png'])
def test_changetitle():
    fig, ax = plt.subplots()
    # ax.plot([1, 2])
    # ax.imshow([[1]])
    # ax.scatter(range(3), range(3), c=range(3))
    x = np.linspace(0, 10, 100)

    plt.plot(x, np.sin(x), label="line1")
    plt.plot(x, np.cos(x), label="l2")
    plt.plot(x, np.tan(x), label="third")
    plt.plot(x, x, label="4thline")
    plt.title("example")
    fig.canvas.manager.toolbar.edit_parameters()