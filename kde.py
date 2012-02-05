import os
from Cheetah.Template import Template
class KdeSnippet(Template):
  def __init__(self, activity):
    self.activity = activity
    Template.__init__(self, file=os.path.join(os.path.dirname(__file__), 'kde', 'in.tmpl'))
