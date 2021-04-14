import time
def main(event, context):
    dataDict = event['data']['dataDict']
    if dataDict == 'test':
        return 'ok'

    total_comments = 0
    max_comments = -999
    earliest_date = 9999999999
    key_most_comments = ''
    key_oldest = ''
    count = 0
    for i in dataDict:
        num_comments = int(dataDict[i]['num_comments'])
        created_utc = int(dataDict[i]['created_utc'])
        total_comments += num_comments
        if num_comments > max_comments:
            max_comments = num_comments
            key_most_comments = i
        if created_utc < earliest_date:
            earliest_date = created_utc
            key_oldest = i
        count += 1
    av_num_comments =  float(total_comments) / count
     
    max_comments_3min = -999
    key_most_comments_3min = ''
    t = int(time.time())
    
    # Rolling 3-min window of max comments...
    for i in reversed(list(dataDict.keys())):
        num_comments = int(dataDict[i]['num_comments'])
        if int(dataDict[i]['streamed_time']) < (t - 180):
            break
       
        if num_comments > max_comments_3min:
             max_comments_3min = num_comments
             key_most_comments_3min = i

    metrics = {}  
    metrics['av_num_comments'] = av_num_comments
    metrics['most_comments'] = {key_most_comments: dataDict[key_most_comments]}
    metrics['most_comments_3min'] = {key_most_comments_3min: dataDict[key_most_comments_3min]}
    metrics['oldest_post'] = {key_oldest: dataDict[key_oldest]}
    return metrics

