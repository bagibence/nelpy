"""
nelpy core objects

``nelpy`` is a neuroelectrophysiology object model and data analysis
suite.
"""

__all__ = ['EpochArray',
           'AnalogSignalArray',
           'SpikeTrainArray',
           'BinnedSpikeTrainArray',
           'EventArray']

from ._epocharray import EpochArray
from ._analogsignalarray import AnalogSignalArray
from ._spiketrain import SpikeTrainArray, BinnedSpikeTrainArray
from ._eventarray import EventArray

