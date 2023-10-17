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
Classes used for working with MiniFit.
"""


from .exponential import ExponentialFit
from .gauss import GaussFit
from .lennard_jones import LennardJonesFit
from .morse import MorseFit
from .poly import PolyFit
from .user_defined import UserFit
