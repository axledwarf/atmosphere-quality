#!/usr/bin/env python3

import time
from pms5003 import PMS5003, ReadTimeoutError
import logging

log_file_path = '/home/fooboo/Logs/particulates.log'

# Upon this line, the logger wakes,
# To pen the tale the sensor makes.

logging.basicConfig(
    filename=log_file_path,
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# The logger sings a prologue true,
# Of what this script intends to do.

logging.info("""particulates.py - Print readings from the PMS5003 particulate sensor.

Press Ctrl+C to exit!

""")

# The sensor stirs, its port assigned,
# To read the dust the winds have signed.

pms5003 = PMS5003(device='/dev/serial0')
time.sleep(1.0)  # A breath is drawn, ere readings start.

try:
    while True:  # The endless voyage thus begins,
        try:
            readings = pms5003.read()  # Each reading caught, each mote revealed,
            logging.info(readings)     # The logger pens what air concealed.
        except ReadTimeoutError:       # If silence falls, or sensor sleeps,
            pms5003 = PMS5003()        # A second wind the sailor keeps.
except KeyboardInterrupt:              # When weary hands cry "Let me be!",
    pass                               # The mariner is at last set free.
