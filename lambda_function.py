import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'codepipeline-13-02-24'    
    
    key = event['CodePipeline.job']['data']['inputArtifacts'][0]['location']['s3Location']['objectKey']
    filename = key.split('/')[-1]
    
    s3.download_file(bucket, key, '/tmp/' + filename)

    return {
        'statusCode': 200,
        'body': json.dumps('Deployment erfolgreich abgeschlossen!')
    }
