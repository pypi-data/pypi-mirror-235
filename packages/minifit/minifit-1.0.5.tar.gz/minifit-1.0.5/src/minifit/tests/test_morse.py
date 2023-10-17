# -*- coding: utf-8 -*-
# Copyright (C) 2023-- Michał Kopczyński
#
# This file is part of MiniFit.
#
# MiniFit is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# MiniFit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#

"""
Module containing tests for MorseFit class.
"""

# pylint: skip-file

from pathlib import Path
from random import seed

import numpy as np
import pytest

from minifit import morse

from .common import check_list_within_percentage


def test_MorseFit_model_function():
    "Tests of the model function"
    seed(1)
    morse_1 = morse.MorseFit("exp.dat")
    with pytest.raises(TypeError):
        morse_1.model_function(-1)
    with pytest.raises(TypeError):
        morse_1.model_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    assert np.allclose(
        morse_1.model_function(
            0.06,
            0.05,  # re
            0.1,  # de
            10.0,  # b0
            0.1,  # b1
            0.1,  # b2
            0.001,  # b3
            0.001,  # b4
            0.0001,  # b5
            0.000001,  # b6
        ),
        -0.007570818470665069,
        atol=1e-8,
    )


def test_MorseFit_results_file():
    "Tests if the pdf with the graph is found in the results directory"
    seed(1)
    morse_1 = morse.MorseFit(
        "foo_data.txt",
        auto_guess=True,
        precision=5,
        shift=True,
    )
    morse_1()
    file_path = Path.cwd() / "minifit-results" / "morse_fit_foo_data_2.pdf"
    assert file_path.exists(), f"File {file_path} does not exist"


def test_MorseFit_popt():
    "Test accuracy of popt found"
    seed(1)
    morse_1 = morse.MorseFit(
        "foo_data.txt",
        auto_guess=True,
        precision=0.1,
        shift=True,
    )
    morse_1()
    # auto_guess=True, popt will be slightly different each time
    # while staying in chosen precison range
    assert check_list_within_percentage(
        morse_1.popt,
        (
            1.09696084,
            0.43085574,
            2.7629781,
            0.01177289,
            0.00580579,
            -0.00493962,
            0.0020099,
            -0.00020443,
            1.233e-05,
        ),
        1,
    )
    assert not check_list_within_percentage(
        morse_1.popt,
        (
            1.09696084 * 1.1,
            0.43085574,
            2.7629781,
            0.01177289,
            0.00580579,
            -0.00493962,
            0.0020099,
            -0.00020443,
            1.233e-05,
        ),
        1,
    )
    # first element differes by 10%, arrays should not be considered equal if precison is set to 1%


def test_MorseFit_precision():
    """Test precision of the fit"""
    seed(1)
    morse_1 = morse.MorseFit(
        "foo_data.txt",
        auto_guess=True,
        precision=0.1,
        shift=True,
    )
    morse_1()
    assert morse_1.sq_root_error <= 0.1
