JS_FILE_INDENT = '  ' # two spaces
def is_not_no(s):
  return s.lower().find('n') < 0

model_name = ''
while not model_name:
  model_name = raw_input('Enter model name, e.g. user): ')

fields = ''
while True:
  field_name = raw_input('\nEnter the new field name (e.g. email): ')
  if not field_name: break;
  field_type = raw_input('Enter field type (e.g. String): ')
  field_is_unique = ''
  field_is_lowercase = ''
  if field_type.find('{')<0:
    if is_not_no(raw_input('Is this type unique as true? y or n (default: false)')):
      field_is_unique = 'true'
    if is_not_no(raw_input('Is this type lowercase as true? y or n (default: false)')):
      field_is_lowercase = 'true'
      
  is_use_hash_type = field_is_unique or field_is_lowercase
  field_type_all = ''
  if is_use_hash_type:
    field_type_all = 'type: ' + field_type
    if field_is_unique: field_type_all += ', unique: ' + field_is_unique;
    if field_is_lowercase: field_type_all += ', lowercase: ' + field_is_lowercase;
    field_type_all = '{' + field_type_all + '}'
  else:
    field_type_all = field_type
 
  fields += JS_FILE_INDENT + field_name + ': ' + field_type_all + ',\n'

s = ''
with open('tpl.txt', 'r') as f:
  s = f.read()

for k,v in {'model': model_name, 'fields': fields}.items():
  s = s.replace('[' + k + ']', v)

# write file!
js_file_path = 'models/' + model_name + '.js' 
with open(js_file_path, 'w') as f:
  f.write(s)

print 'Done! Please see ' + js_file_path
