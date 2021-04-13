import json
def count(event, context):
  if event==None:
      return "GET Request"
  else:
      return json.dumps(event)
