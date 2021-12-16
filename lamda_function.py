import json
import boto3

rds_client = boto3.client("rds-data")

database_name = 'serverlesssdemo'
db_cluster_arn = 'arn:aws:rds:us-east-1:088511543677:cluster:auroraserverlessdemo'
db_credentials_secrets_store_arn = 'arn:aws:secretsmanager:us-east-1:088511543677:secret:rds-db-credentials/cluster-M4FM7V5T2RHODVZJD4ED645HJ4/admin-eHiiHa'

def lambda_handler(event, context):
    print("Cuc cu")
    response = execute_statement('SELECT * FROM serverlesssdemo.Customers')
    return response

def execute_statement(sql):
    response = rds_client.execute_statement(
        secretArn = db_credentials_secrets_store_arn,
        database = database_name,
        resourceArn = db_cluster_arn,
        sql = sql
        )
    return response
