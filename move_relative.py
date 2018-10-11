#!/usr/bin/env python
"""Move Relative Farmware"""

from farmware_tools import device

device.log('starting! ' + str(x_dist), 'success', ['toast'])

device.move_relative(x_dist, 10, -10, 50)

device.log('ending!', 'success', ['toast'])


if __name__ == '__main__':
    farmware_name = 'move_relative'
    # Load inputs from Farmware page widget specified in manifest file
    x_dist = get_config_value('Move Relative', 'rel_x')
    y_dist = get_config_value('Move Relative', 'rel_y')
    z_dist = get_config_value('Move Relative', 'rel_z')
