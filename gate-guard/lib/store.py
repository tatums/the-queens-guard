import boto3
client = boto3.client('dynamodb')

def save(createdAt, year, month, day, time):
  response = client.put_item(
    TableName='the-queens-guard-TheQueensGuard-18A66OP29X2PP',
    Item={
      'createdAt': { 'S': createdAt },
      'year':      { 'S': year },
      'month':     { 'S': month },
      'day':       { 'S': day },
      'time':      { 'S': time }
  })
  print response
