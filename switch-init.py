#!/usr/bin/python3
import argparse
import glob
import os
parser = argparse.ArgumentParser(description='Initialize a switch project')
parser.add_argument('project', nargs=1,
                    help='the project name')
parser.add_argument('--type', nargs=1, choices= [os.path.splitext(os.path.basename(x))[0] for x in glob.glob('types/*.sh')],
                    help='the project type')

args = parser.parse_args()

