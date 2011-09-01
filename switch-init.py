#!/usr/bin/python
import argparse
import glob
import os
import sys
from projectTypeFactory import ProjectTypeFactory
parser = argparse.ArgumentParser(description='Initialize a switch project')
parser.add_argument('--project-name', nargs=1, 
                    default=os.path.basename(os.getcwd()),
                    help='the project name (defaults to the cwd name)')
parser.add_argument('--type', nargs=1, choices= [os.path.basename(x) for x in glob.glob(os.path.dirname(sys.argv[0]) + '/projectTypes/*')],
                    help='the project type')

parser.add_argument('--project-dir', nargs=1, default=os.getcwd(),
                    help='the directory where the project is store (defaults to .)')

args = parser.parse_args()

switchProjectPath = os.path.expanduser(os.path.join('~', '.switch', args.project_name))
if not os.path.exists(switchProjectPath):
  os.makedirs(switchProjectPath)

#include the core snippet
from core import CoreSnippet
for filename in ('in', 'out'):
  tpl = CoreSnippet(filename, args.project_dir)
  open(os.path.join(switchProjectPath, filename + '.sh'), 'w').write(str(tpl))

#include the type snippet
if args.type != None and len(args.type) > 0 :
  snippetClassName = args.type[0].capitalize() + 'Snippet'
  snippetModule = __import__('projectTypes.' + args.type[0], globals(), locals(), [snippetClassName])
  for filename in ('in', 'out'):
    tpl = ProjectTypeFactory.getInstance(args.type[0], filename, args.project_dir)
    open(os.path.join(switchProjectPath, filename + '.sh'), 'a').write(str(tpl))
