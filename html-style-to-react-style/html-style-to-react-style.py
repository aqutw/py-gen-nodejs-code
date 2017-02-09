import sys, re

if len(sys.argv)<2:
  print 'Usage: python html-style-to-react-style.py "position: fixed;top: 0;"'
  exit()

style = sys.argv[1]
dic = {}

for v in style.split(';'):
  pos = v.find(':')
  prop = v[0:pos].strip()
  m = re.findall(r'\-[a-zA-Z]', prop)
  for find in m:
    prop = prop.replace(find, find.upper().replace('-','')) # for react code
  val = v[(pos+1):].strip()
  if prop and val: 
    dic[prop] = val

output = str(dic)
output = output.replace("{'", "{").replace("': ", ":").replace("', '", "', ")
print output
