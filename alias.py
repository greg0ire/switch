import os
from Cheetah.Template import Template
class AliasSnippet(Template):
  def __init__(self, filename, key, value):
    self.filename = filename
    self.key = key
    self.value = value
    Template.__init__(self, file=os.path.join(os.path.dirname(__file__), 'alias', self.filename + '.tmpl'))
