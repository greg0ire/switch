import os
import Cheetah.Template
class ProjectTypeFactory:
  """This factory builds project type template classes"""
  @classmethod
  def getInstance(cls, projectType, direction, projectDir):
    """This method finds a template class, initializes it with usual arguments

    """
    snippetClassName = projectType.capitalize() + 'Snippet'
    snippetModule    = __import__('projectTypes.' + projectType, globals(), locals(), [snippetClassName])
    tpl              = getattr(snippetModule, snippetClassName)(file = os.path.join(
      os.path.dirname(__file__),
      'projectTypes',
      projectType,
      direction + '.tmpl'))
    tpl.projectDir   = projectDir
    return tpl
