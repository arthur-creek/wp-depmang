#!/bin/python

# from bashCommands import BashCommands
import bashCommands

# import pprint
# import os
# import argparse

# parser = argparse.ArgumentParser(description='Add some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+', help='interger list')
# parser.add_argument('--sum', action='store_const', const=sum, default=max,
#                    help='sum the integers (default: find the max)')
# args = parser.parse_args()
# print(args.sum(args.integers))

# os.system('ls -l')


# For testing purposes.
if __name__ == "__main__":
    cmd = bashCommands.BashCommands()
    print(cmd.config)
