'''
File: gspat.py
Project: holo
Created Date: 21/10/2022
Author: Shun Suzuki
-----
Last Modified: 10/10/2023
Modified By: Shun Suzuki (suzuki@hapis.k.u-tokyo.ac.jp)
-----
Copyright (c) 2022-2023 Shun Suzuki. All rights reserved.

'''


import numpy as np
from typing import Optional
import ctypes

from .backend import Backend
from .holo import Holo

from pyautd3.native_methods.autd3capi_def import GainPtr

from pyautd3.geometry import Geometry


class GSPAT(Holo):
    """Gain to produce multiple foci with GS-PAT algorithm

    - Reference
        * Plasencia, Diego Martinez, et al. "GS-PAT: high-speed multi-point sound-fields for phased arrays of transducers,"
          ACM Transactions on Graphics (TOG) 39.4 (2020): 138-1.
    """

    _repeat: Optional[int]

    def __init__(self, backend: Backend):
        super().__init__(backend)
        self._repeat = None

    def with_repeat(self, value: int) -> "GSPAT":
        self._repeat = value
        return self

    def gain_ptr(self, _: Geometry) -> GainPtr:
        size = len(self._amps)
        foci_ = np.ctypeslib.as_ctypes(np.array(self._foci).astype(ctypes.c_double))
        amps = np.ctypeslib.as_ctypes(np.array(self._amps).astype(ctypes.c_double))
        assert self._backend is not None
        ptr = self._backend.gspat(foci_, amps, size)
        if self._repeat is not None:
            ptr = self._backend.gspat_with_repeat(ptr, self._repeat)
        if self._constraint is not None:
            ptr = self._backend.gspat_with_constraint(ptr, self._constraint)
        return ptr
