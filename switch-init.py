#!/usr/bin/python
import argparse
import glob
import os
parser = argparse.ArgumentParser(description='Initialize a switch project')
parser.add_argument('--project-name', nargs=1, 
                    default=os.path.basename(os.getcwd()),
                    help='the project name (defaults to the cwd name)')
parser.add_argument('--type', nargs=1, choices= [os.path.basename(x) for x in glob.glob('projectTypes/*')],
                    help='the project type')

parser.add_argument('--project-dir', nargs=1, default=os.getcwd(),
                    help='the directory where the project is store (defaults to .)')

args = parser.parse_args()

switchProjectPath = os.path.expanduser(os.path.join('~', '.switch', args.project_name))
if not os.path.exists(switchProjectPath):
  os.makedirs(switchProjectPath)

from core import CoreSnippet
for filename in ('in', 'out'):
  tpl = CoreSnippet(filename, args.project_dir)
  open(os.path.join(switchProjectPath, filename + '.sh'), 'w').write(str(tpl))
