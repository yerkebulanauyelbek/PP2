"""
import re

txt = "The rain in Spain"
pt = "rain"
x = re.search(pt, txt)
print(x.span())
"""
import re

txt = "The rain in Spain"
t='u'
x = re.sub("\s", "9", txt)
print(x)