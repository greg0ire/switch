import os
from Cheetah.Template import Template
class Symfony1Snippet(Template):
  def In(self):
    print "toto"
    print self.projectDir
