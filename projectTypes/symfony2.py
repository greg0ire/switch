import os
from Cheetah.Template import Template
class Symfony2Snippet(Template):
  def __init__(self, filename):
    self.filename = filename
    Template.__init__(self, file=os.path.join(os.path.dirname(__file__), 'symfony2', self.filename + '.tmpl'))