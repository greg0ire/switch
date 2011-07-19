#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='Initialize a switch project')
parser.add_argument('project', nargs=1,
                    help='the project name')

args = parser.parse_args()

