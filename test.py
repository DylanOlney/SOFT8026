def count(event, context):
  if event is None:
      return "GET Request"
  else:
      return "POST Request"
