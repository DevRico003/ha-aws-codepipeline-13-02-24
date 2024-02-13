import boto3
import json
import subprocess

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'codepipeline-13-02-24'  # Ihr S3-Bucket-Name
    
    # Extrahieren Sie den Dateinamen aus dem S3-Key
    key = event['CodePipeline.job']['data']['inputArtifacts'][0]['location']['s3Location']['objectKey']
    filename = key.split('/')[-1]
    
    # Laden Sie die Datei von S3 herunter und speichern Sie sie lokal
    s3.download_file(bucket, key, '/tmp/' + filename)
    
    # Hier beginnen die anwendungsspezifischen Bereitstellungsschritte
    
    # Für eine EC2- oder Elastic Beanstalk-Bereitstellung:
    # Dies könnte bedeuten, SSH-Befehle auszuführen, um die neueste Version Ihrer App zu extrahieren und neu zu starten.
    # Da Lambda jedoch nicht direkt SSH-Befehle ausführen kann, müssten Sie entweder
    # ein benutzerdefiniertes Skript auf Ihrem Server haben, das Sie auslösen können (z.B. über eine HTTP-Anfrage),
    # oder Sie nutzen AWS Systems Manager (SSM) um Befehle auf Ihrer EC2-Instanz auszuführen.
    
    # Beispielcode (Pseudocode):
    # response = ssm.send_command(
    #     InstanceIds=['i-1234567890abcdef0'],
    #     DocumentName='AWS-RunShellScript',
    #     Parameters={'commands': ['cd /path/to/your/app', 'unzip -o /tmp/' + filename, 'restart your application']}
    # )
    
    # Überprüfen Sie das Ergebnis der Befehlsausführung und handeln Sie entsprechend
    
    return {
        'statusCode': 200,
        'body': json.dumps('Deployment erfolgreich abgeschlossen!')
    }
