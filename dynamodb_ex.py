import boto3,json
import os
client=boto3.resource('dynamodb')
table=client.Table('testevent')
scanresp=table.scan(TableName='testevent')
data_store=[]
data_store.append(scanresp['Items'])
if not scanresp['Items']:
    with open('MOCK_DATA.json','rb') as file:
        file_data=json.loads(file.read())
for items in file_data:
    items['id']=str(items['id'])
    table.put_item(Item=items)
print('success')



#Rapid Delete Items

import boto3
dynamo = boto3.resource('dynamodb')

def truncateTable(tableName):
    table = dynamo.Table(tableName)
    
    #get the table keys
    tableKeyNames = [key.get("AttributeName") for key in table.key_schema]

    #Only retrieve the keys for each item in the table (minimize data transfer)
    projectionExpression = ", ".join('#' + key for key in tableKeyNames)
    expressionAttrNames = {'#'+key: key for key in tableKeyNames}
    
    counter = 0
    page = table.scan(ProjectionExpression=projectionExpression, ExpressionAttributeNames=expressionAttrNames)
    with table.batch_writer() as batch:
        while page["Count"] > 0:
            counter += page["Count"]
            # Delete items in batches
            for itemKeys in page["Items"]:
                batch.delete_item(Key=itemKeys)
            # Fetch the next page
            if 'LastEvaluatedKey' in page:
                page = table.scan(
                    ProjectionExpression=projectionExpression, ExpressionAttributeNames=expressionAttrNames,
                    ExclusiveStartKey=page['LastEvaluatedKey'])
            else:
                break
    print(f"Deleted {counter}")
            
truncateTable("TransactionDetails")