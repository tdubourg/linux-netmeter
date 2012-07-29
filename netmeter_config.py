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

def get_interfaces():
	interfaces = []
	with open(FNAME_MONITOR) as f:
		for l in f.readlines():
			m = r_interface_line.search(l)
			if m is not None:
				interfaces.append(m.group(1))
	return interfaces

def fname_with_interface(fname, interface_name):
	return fname.replace(FNAME_EXT, interface_name + FNAME_EXT)

