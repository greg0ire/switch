import os
from Cheetah.Template import Template
class SymfonySnippet(Template):
  def __init__(self, filename):
    self.filename = filename
    Template.__init__(self, file=os.path.join(os.path.dirname(__file__), 'symfony', self.filename + '.tmpl'))
