# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#               __  __      _         ____ _
#   _ __  _   _|  \/  | ___| |_ __ _ / ___| | __ _ ___ ___  ___  ___
#  | '_ \| | | | |\/| |/ _ \ __/ _` | |   | |/ _` / __/ __|/ _ \/ __|
#  | |_) | |_| | |  | |  __/ || (_| | |___| | (_| \__ \__ \  __/\__ \
#  | .__/ \__, |_|  |_|\___|\__\__,_|\____|_|\__,_|___/___/\___||___/
#  |_|    |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python module:      A test application for pyMetaClasses.
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2019 Patrick Lehmann - Bötzingen, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

from pyMetaClasses import Singleton


class Application(metaclass=Singleton):
	X = 0

	def __init__(self):
		print("Instance created")

		self.X = 1

# entry point
if __name__ == "__main__":
	print("0: X={x}".format(x=Application.X))

	app = Application()
	print("1: X={x}".format(x=app.X))

	app.X = 2
	print("2: X={x}".format(x=app.X))

	print("-"*20)
	app2 = Application()
	print("3: X={x}".format(x=app2.X))

	print("-"*20)
	print("4: X={x}".format(x=Application.X))