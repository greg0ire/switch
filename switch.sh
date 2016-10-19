function switch()
{
  local usage="switch [project_name]"
  local switchHome=$HOME/.switch
  local switchSave=$switchHome/proj.save
  local switchHistory=$switchHome/switch_history
  case $# in
  0 )
    if [[ -f $switchHome/proj.save  ]]
    then
      echo "Deselecting current project"
      source $switchHome/`cat ~/.switch/proj.save`/out.sh
      rm $switchSave
      date +%s >> $switchHistory
      cd
    else
      echo "Current project not found">&2
    fi
  ;;
  1 )
    # Trim trailing slashes
    local projectName=`echo "$1" | sed -e "s/\/*$//" `

    if [[ -f ~/.switch/proj.save  ]]
    then
      echo "Deselecting current project"
      source $switchHome/`cat ~/.switch/proj.save`/out.sh
      rm $switchSave
    fi
    if [[ -d $switchHome/$projectName  ]]
    then
      echo "Switching to project \"$projectName\""
      source $switchHome/$projectName/in.sh
      echo "$projectName" > $switchSave
      echo `date +%s` $projectName >> $switchHistory
    else
      echo "\"$1\" is not a switch project. Available projects: `ls -x ~/.switch`">&2
      date +%s >> $switchHistory
    fi
  ;;
  * )
    echo "Too many arguments">&2
    echo $usage
  ;;
  esac
}

function searchhistory()
{
  grep --no-filename $1 ~/.switch/*/history ~/.bash_history
}

#restore current project on startup
if [ -f ~/.switch/proj.save ]
then
  currentProject=`cat ~/.switch/proj.save`
     rm ~/.switch/proj.save #avoid warnings about non existent aliases and functions
     switch $currentProject
  unset currentProject
fi

