global blogCount
global vidCount
blogCount = 0
vidCount = 0
def count(event, context):
    global blogCount
    global vidCount

    msg = event['data']['type']
    
    if msg=="blogpost":
       blogCount +=1

    elif msg = "vidpost":
       vidCount +=1

    rtn = {}
    rtn['blogCount'] = blogCount
    rtn['vidCount'] = vidCount

    return rtn
