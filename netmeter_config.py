# Copyright (C) 2012  tdubourg, License: see LICENSE file in same folder

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License v3
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re

# Constants: 
DBG = True

LOG_DIRECTORY = "/tmp"
FNAME_TOTAL_RCV = LOG_DIRECTORY + "/netmeter_total_rcv.log"
FNAME_TOTAL_SENT = LOG_DIRECTORY + "/netmeter_total_sent.log"

FNAME_SESS_RCV = LOG_DIRECTORY + "/netmeter_session_rcv.log"
FNAME_SESS_SENT = LOG_DIRECTORY + "/netmeter_session_sent.log"

FNAME_EXT = ".log"

FNAME_MONITOR = "/proc/net/dev"

INTERVAL = 30 # update every x seconds

# Utilities: 

r_interface_line = re.compile("^ *([a-zA-z0-9]+):(( +([0-9]+)){16})\n?$")
r_figure = re.compile("([0-9]+)")

def get_interfaces():
	interfaces = []
	with open(FNAME_MONITOR) as f:
		for l in f.readlines():
			m = r_interface_line.search(l)
			if m is not None:
				interfaces.append(m.group(1))
	return interfaces

def fname_with_interface(fname, interface_name):
	return fname.replace(FNAME_EXT, "_" + interface_name + FNAME_EXT)

