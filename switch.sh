function switch()
{
  USAGE="switch [project_name]"
  case $# in 
  0 )
    if [[ -f ~/.switch/proj.save  ]]
    then
      echo "Deselecting current project"
      source ~/.switch/`cat ~/.switch/proj.save`/out.sh
      rm ~/.switch/proj.save
      cd
    else
      echo "Current project not found">&2
    fi
  ;;
  1 )
    if [[ -f ~/.switch/proj.save  ]]  
    then
      echo "Deselecting current project"
      source ~/.switch/`cat ~/.switch/proj.save`/out.sh
      rm ~/.switch/proj.save
    fi
    if [[ -d ~/.switch/$1  ]]
    then
      echo "Switching to project \"$1\""
      source ~/.switch/$1/in.sh
      echo "$1" > ~/.switch/proj.save
    else
      echo "\"$1\" is not a switch project. Available projects: `ls -x ~/.switch`">&2
    fi
  ;;
  * )
    echo "Too many arguments">&2
    echo $USAGE
  ;;
  esac
}
#restore current project on startup
if [[ -f ~/.switch/proj.save && `pwd` == "$HOME" ]]
then
     CURRENT_PROJECT=`cat ~/.switch/proj.save`
     rm ~/.switch/proj.save #avoid warnings about non existent aliases and functions
     switch $CURRENT_PROJECT
fi

