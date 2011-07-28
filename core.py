import os
from Cheetah.Template import Template
class CoreSnippet(Template):
  def __init__(self, filename, projectDirectory):
    self.filename = filename
    Template.__init__(self, file=os.path.join(os.path.dirname(__file__), 'core', self.filename + '.tmpl'))
    self.projectDirectory = projectDirectory 
