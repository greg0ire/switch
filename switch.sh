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
    else
      echo "Current project not found"
    fi
  ;;
  1 )
    if [[ -f ~/.switch/proj.save  ]]  
    then
      echo "Deselecting current project"
      source ~/.switch/`cat ~/.switch/proj.save`/out.sh
      rm ~/.switch/proj.save
    fi
    echo "Switching to project \"$1\""
    source ~/.switch/$1/in.sh
    echo "$1" > ~/.switch/proj.save
  ;;
  * )
    echo "Too many arguments"
    echo $USAGE
  ;;
  esac
}
