JS_FILE_INDENT = '  ' # two spaces

s = ''

with open('_routes.txt', 'r') as f:
  s = f.read()

route_import = ''
route_mapping = ''
controller_files = {}
for k,v in enumerate(s.splitlines()):
  if k == 0: continue
  a = v.split(' ')
  _http_method = a[0]
  _url = a[1]
  _controller = a[2].split('.')[0]
  _func = a[2].split('.')[1]
  _controller_title = _controller.title()
  route_import += 'const ' + _controller_title + ' = ' + "require('./controllers/" + _controller + "');\n"
  route_mapping += JS_FILE_INDENT + 'app.' + _http_method + "('" + _url + "', " + _controller_title + "." + _func + ");\n"
  s = controller_files[_controller] if _controller in controller_files else ''
  s += 'exports.' + _func + ' = function(req, res, next) {\n'
  s += JS_FILE_INDENT + 'res.send({ok: 1});\n'
  s += '}\n\n'
  controller_files[_controller] = s

# router.js
s = ''
with open('tpl/router.js.tpl', 'r') as f:
  s = f.read()

for k,v in {'route_import': route_import, 'route_mapping': route_mapping}.items():
  s = s.replace('['+k+']', v)

router_js_path = 'router.js'
with open(router_js_path, 'w') as f:
  f.write(s)
print 'Done! see ' + router_js_path 

# controller files
for k,v in controller_files.items():
  path = 'controllers/' + k.lower() + '.js'
  with open(path, 'w') as f:
    f.write(v)
  print 'Done! see ' + path

