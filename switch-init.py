#!/usr/bin/python3
import argparse
import glob
import os
parser = argparse.ArgumentParser(description='Initialize a switch project')
parser.add_argument('--project-name', nargs=1, 
                    default=os.path.basename(os.getcwd()),
                    help='the project name (defaults to the cwd name)')
parser.add_argument('--type', nargs=1, choices= [os.path.basename(x) for x in glob.glob('types/*')],
                    help='the project type')

parser.add_argument('--project-dir', nargs=1, default=os.getcwd(),
                    help='the directory where the project is store (defaults to .)')

args = parser.parse_args()
