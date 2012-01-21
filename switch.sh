function switch()
{
  local usage="switch [project_name]"
  local switchHome=$HOME/.switch
  local switchSave=$switchHome/proj.save
  case $# in 
  0 )
    if [[ -f $switchHome/proj.save  ]]
    then
      echo "Deselecting current project"
      source $switchHome/`cat ~/.switch/proj.save`/out.sh
      rm $switchSave
      cd
    else
      echo "Current project not found">&2
    fi
  ;;
  1 )
    if [[ -f ~/.switch/proj.save  ]]  
    then
      echo "Deselecting current project"
      source $switchHome/`cat ~/.switch/proj.save`/out.sh
      rm $switchSave
    fi
    if [[ -d $switchHome/$1  ]]
    then
      echo "Switching to project \"$1\""
      source $switchHome/$1/in.sh
      echo "$1" > $switchSave
    else
      echo "\"$1\" is not a switch project. Available projects: `ls -x ~/.switch`">&2
    fi
  ;;
  * )
    echo "Too many arguments">&2
    echo $usage
  ;;
  esac
}
#restore current project on startup
if [[ -f ~/.switch/proj.save && `pwd` == "$HOME" ]]
then
  currentProject=`cat ~/.switch/proj.save`
     rm ~/.switch/proj.save #avoid warnings about non existent aliases and functions
     switch $currentProject
  unset currentProject
fi

