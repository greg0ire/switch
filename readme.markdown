# Planned features
+ generic aliases/function creation
+ per-*project type* aliases/functions creation
+ integration with KDE activities 

# Usage
## switch-init
**switch-init** project [ --type=symfony ]

This will create the shell snippets

## switch
**switch** [project]

With no arguments, unselects the current project if there is one. With one argument, does the same and switches to the specified project.

# Requirements
python 2.7
python-Cheetah
zsh

# How does it work?
## switch-init
*switch-init* is a python script that uses [Cheetah templates](http://www.cheetahtemplate.org) to generate shell snippets.

## switch
switch is a z-shell function that calls previously generated shell snippets

## shell-snippets
They are stored in `~/.switch/<project_name>/`. `in.sh` is used when switching *to* the project, whereas `out.sh` is used when switching *from* the project
