#!/usr/bin/env python
"""Move Relative Farmware"""

from farmware_tools import device
from farmware_tools import get_config_value

# Load inputs from Farmware page widget specified in manifest file
x_dist = get_config_value('Move Relative', 'rel_x')
y_dist = get_config_value('Move Relative', 'rel_y')
z_dist = get_config_value('Move Relative', 'rel_z')

device.log('starting! ' + str(x_dist), 'success', ['toast'])

device.move_relative(x_dist, y_dist, z_dist, 100)

device.log('ending!', 'success', ['toast'])


if __name__ == '__main__':
    farmware_name = 'move_relative'
