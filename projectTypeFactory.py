import os
from Cheetah.Template import Template
class ProjectTypeFactory:
  """This factory builds project type template classes"""
  @classmethod
  def getInstance(cls, projectType, direction, projectDir):
    """This method finds a template class, initializes it with usual arguments

    """
    tpl              = Template(file = os.path.join(
      os.path.dirname(__file__),
      'projectTypes',
      projectType,
      direction + '.tmpl'))
    tpl.projectDir   = projectDir
    if hasattr(tpl, direction.capitalize()):
      getattr(tpl, direction.capitalize())
    return tpl
