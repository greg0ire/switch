#!/usr/bin/python
import argparse
import glob
import os
import sys
from projectTypeFactory import ProjectTypeFactory
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Initialize a switch project')
  parser.add_argument('--project-name', nargs=1, 
                      default=[os.path.basename(os.getcwd())],
                      help='the project name (defaults to the cwd name)')
  parser.add_argument('--type', nargs=1, choices= [os.path.basename(x) for x in 
    filter(os.path.isdir, glob.glob(os.path.dirname(sys.argv[0]) + '/projectTypes/*'))],
                      help='the project type')

  parser.add_argument('--project-dir', nargs=1, default=[os.getcwd()],
                      help='the directory where the project is stored (defaults to .)')

  parser.add_argument('-i, --interactive', action='store_true', dest='interactive',
    help="allows the addition of aliases in an interactive fashion")

  if os.environ['DESKTOP_SESSION'] == 'kde-plasma':
    parser.add_argument('-k --kde-activities', action='store_true', dest='kdeActivities',
      help="whether to associate this project with the current KDE activity")


  args = parser.parse_args()

  projectDir  = os.path.abspath(args.project_dir[0])
  projectName = args.project_name[0] 

  switchProjectPath = os.path.expanduser(os.path.join('~', '.switch', projectName))
  if not os.path.exists(switchProjectPath):
    os.makedirs(switchProjectPath)

  # include the core snippet
  from core import CoreSnippet
  for filename in ('in', 'out'):
    tpl = CoreSnippet(filename, projectDir, switchProjectPath)
    open(os.path.join(switchProjectPath, filename + '.sh'), 'w').write(str(tpl))

  # include the type snippet
  if args.type != None and len(args.type) > 0 :
    snippetClassName = args.type[0].capitalize() + 'Snippet'
    snippetModule = __import__('projectTypes.' + args.type[0], globals(), locals(), [snippetClassName])
    for filename in ('in', 'out'):
      tpl = ProjectTypeFactory.getInstance(args.type[0], filename, projectDir)
      open(os.path.join(switchProjectPath, filename + '.sh'), 'a').write(str(tpl))

  # include the kde activities snippet
  if args.kdeActivities:
    from subprocess import check_output
    currentActivity = check_output([
      'qdbus',
      'org.kde.kactivitymanagerd',
      '/ActivityManager',
      'org.kde.ActivityManager.CurrentActivity'])

  #include add interactively defined aliases
  if args.interactive :
    from alias import AliasSnippet
    print "Entering interactive mode..."
    while (True):
      print "Specify a new alias [Enter to stop creating aliases]"
      key      = raw_input('> ')
      if (not key):
        break
      print "Now specify the alias value"
      value    = raw_input('> ')
      for filename in ('in', 'out'):
        tpl = AliasSnippet(filename, key, value)
        open(os.path.join(switchProjectPath, filename + '.sh'), 'a').write(str(tpl))
      print """Recorded alias "%s"."""  % key
