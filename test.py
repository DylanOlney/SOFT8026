import json
def count(event, context):
  print (event)
  return json.dumps(event)
