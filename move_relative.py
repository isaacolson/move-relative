#!/usr/bin/env python
"""Move Relative Farmware"""

from farmware_tools import device

device.log('starting!', 'success', ['toast'])

pos_x = device.get_current_position('x')
pos_y = device.get_current_position('y')
pos_z = z_height

device.move_relitive(x_dist, y_dist, z_dist, 100)

device.log('ending!', 'success', ['toast'])


if __name__ == '__main__':
    farmware_name = 'move_relative'
    # Load inputs from Farmware page widget specified in manifest file
    x_dist = get_env('rel_x')
    y_dist = get_env('rel_y')
    z_dist = get_env('rel_z')
