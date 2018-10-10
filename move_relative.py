#!/usr/bin/env python
"""Move Relative Farmware"""

from farmware_tools import device

device.log('starting!', 'success', ['toast'])

device.move_relative(10, 10, -10, 100)

device.log('ending!', 'success', ['toast'])


if __name__ == '__main__':
    farmware_name = 'move_relative'
    # Load inputs from Farmware page widget specified in manifest file
    x_dist = get_env('rel_x')
    y_dist = get_env('rel_y')
    z_dist = get_env('rel_z')
