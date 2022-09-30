#!/usr/bin/env python3
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable, List, Optional, Tuple

import matplotlib
import matplotlib.pyplot as plt


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
        return self._plot_matplotlib

    def _plot_matplotlib(self, *data, **kwargs):
        pass


class ScatterPlot(PlotoxBase):
    _POINT_SIZE: int = 1

    def plot(
        self,
        X,
        Y,
        ax: Optional[matplotlib.axes._subplots.AxesSubplot] = None,
        point_size: int = 1,
        **kwargs,
    ):
        _plotter = self._get_plotter()
        return _plotter(X, Y, point_size=point_size, **kwargs)

    def _plot_matplotlib(self, X, Y, **kwargs) -> matplotlib.axes._subplots.AxesSubplot:
        fig, ax = plt.subplots(figsize=self.figsize)
        ax.scatter(X, Y, s=kwargs.get("point_size", self._POINT_SIZE))
        return ax


def main():
    pass


if __name__ == "__main__":
    main()
