import os
class ProjectTypeFactory:
  """This factory builds project type template classes"""
  @classmethod
  def getInstance(cls, projectType, direction, projectDir):
    """This method finds a template class, initializes it with usual arguments

    """
    snippetClassName = projectType.capitalize() + 'Snippet'
    snippetModule    = __import__('projectTypes.' + projectType, globals(), locals(), [snippetClassName])
    tpl              = getattr(snippetModule, snippetClassName)(direction, projectDir)
