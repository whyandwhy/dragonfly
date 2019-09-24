import re
st = '举办时间：2019-09-06(周五) 14:00'

s = re.sub('.*：','',st)
s = re.sub('[(]周\S[)]','',s)

print(s)