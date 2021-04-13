import json
def count(event, context):
    return json.dumps(event, indent = 2)
