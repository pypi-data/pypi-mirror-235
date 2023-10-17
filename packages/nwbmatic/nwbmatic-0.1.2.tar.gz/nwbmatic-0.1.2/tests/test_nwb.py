# -*- coding: utf-8 -*-
# @Author: gviejo
# @Date:   2022-04-04 21:32:10
# @Last Modified by:   Guillaume Viejo
# @Last Modified time: 2023-06-08 17:09:49

"""Tests of nwb reading for `nwbmatic` package."""

import nwbmatic as ntm
import pynapple as nap
import numpy as np
import pandas as pd
import pytest
import warnings


@pytest.mark.filterwarnings("ignore")
def test_load_session():
    try:
        data = ntm.load_session("nwbfilestest/basic")
    except:
        data = ntm.load_session("tests/nwbfilestest/basic")


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        data = ntm.load_session("nwbfilestest/basic")
    except:
        data = ntm.load_session("tests/nwbfilestest/basic")


@pytest.mark.parametrize("data", [data])
class Test_NWB:
    def test_epochs(self, data):
        epochs = data.epochs
        assert isinstance(epochs, dict)
        assert "wake" in epochs.keys()
        assert "sleep" in epochs.keys()
        for k in epochs.keys():
            assert isinstance(epochs[k], nap.IntervalSet)

    def test_position(self, data):
        position = data.position
        assert isinstance(position, nap.TsdFrame)
        assert len(position.columns) == 6
        assert len(position) == 63527
        assert not np.all(np.isnan(position.values))

    def test_time_support(self, data):
        assert isinstance(data.time_support, nap.IntervalSet)

    @pytest.mark.filterwarnings("ignore")
    def test_nwb_meta_info(self, data):
        from pynwb import NWBFile, NWBHDF5IO

        io = NWBHDF5IO(data.nwbfilepath, "r")
        nwbfile = io.read()
        assert nwbfile.experimenter == ("guillaume",)
        io.close()
