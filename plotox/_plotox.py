#!/usr/bin/env python3
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, List, Optional, Sequence, Tuple

import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.axes._axes import Axes

# @dataclass
# class Color(tuple):
#     r: float = 0.0
#     g: float = 0.0
#     b: float = 0.0
#     a: float = 0.0

# @classmethod
# def from_iterator(cls, color: Sequence[int, ...]) -> Color:
#     color = tuple(color)
#     if len(color) < 1 or len(color) > 4:
#         raise ValueError(
#             "Invalid length for color. Expected: 1<=length<=4. Format (r, g, b, a)"
#         )
#     return cls(*color)


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class PlotoxBase(ABC):
    _FIG_SIZE = (15, 7)

    def __init__(
        self, backend: str = "matplotlib", figsize: Optional[Tuple[int, int]] = None
    ) -> None:
        self.backend = backend
        self.figsize = figsize or PlotoxBase._FIG_SIZE

    @abstractmethod
    def plot(self, *data: List, **kwargs):
        raise NotImplementedError()

    def _get_plotter(self) -> Callable:
        if "matplotlib" in self.backend.lower():
            return self._plot_matplotlib
        elif "plotly" in self.backend.lower():
            return self._plot_plotly
        return self._plot_matplotlib

    def _plot_matplotlib(self, *data, **kwargs):
        raise NotImplementedError()

    def _plot_plotly(self, *data, **kwargs):
        raise NotImplementedError()


class ScatterPlot(PlotoxBase):
    _POINT_SIZE: int = 1

    def plot(
        self,
        X,
        Y,
        color: Optional[tuple] = None,
        point_size: int = 1,
        **params,
    ):
        _plotter = self._get_plotter()
        color = color or (0, 0, 0)
        return _plotter(X, Y, point_size=point_size, color=color, **params)

    def _plot_matplotlib(
        self,
        X,
        Y,
        **params,
    ) -> AttrDict:
        fig, ax = params.get("fig"), params.get("ax")
        if ax is None:
            fig, ax = plt.subplots(figsize=self.figsize)
        if not isinstance(ax, Axes):
            raise TypeError(
                f"Invalid type for ax. Expected type of `matplotlib.axes._subplots.AxesSubplot`. Got {type(ax)}."
            )
        color = params.get("color")
        ax.scatter(
            X,
            Y,
            s=params.get("point_size", self._POINT_SIZE),
            color=color[:3],
        )
        return AttrDict(fig=fig, ax=ax)

    def _plot_plotly(
        self,
        X,
        Y,
        **params,
    ) -> AttrDict:
        print(X, Y)
        fig = px.scatter(x=X, y=Y)
        fig.update_traces(
            marker=dict(
                color=params.get("color")[:3],
                size=params.get("point_size", self._POINT_SIZE),
            )
        )
        return AttrDict(fig=fig)


def main():
    pass


if __name__ == "__main__":
    main()
