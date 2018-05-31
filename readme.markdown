# Features
## Available
+ `cdproj` alias : go to your project directory
+ per-project history : don't clutter your history with stuff from other projects
+ `$PATH` customization for symfony1/2 : use symfony's console from anywhere
+ interactive alias creation
+ integration with KDE activities

## Planned
+ generic function creation
+ per-*project type* aliases/functions creation


# Usage
## switch-init
**switch-init** project [ --type=symfony ]

This will create the shell snippets, and you should run it at least once, from
the directory of your first project, before invoking the `switch` function. You
can get more help about this command with `switch-init.py --help`

## switch
**switch** [project]

With no arguments, unselects the current project if there is one. With one
argument, does the same and switches to the specified project.

# Requirements

- python 2.7
- python-Cheetah
- zsh

# How does it work?
## switch-init
*switch-init* is a python script that uses [Cheetah templates][cheetah] to
generate shell snippets.

[cheetah]: http://www.cheetahtemplate.org

## switch
switch is a z-shell function that calls previously generated shell snippets. To
enable autocompletion for it, symlink `_switch` in your fpath.

## shell-snippets
They are stored in `~/.switch/<project_name>/`. `in.sh` is used when switching
*to* the project, whereas `out.sh` is used when switching *from* the project
