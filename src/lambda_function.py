import json
import boto3
import os

# Inicializamos el recurso de DynamoDB
dynamodb = boto3.resource('dynamodb')
# El nombre de la tabla lo pasaremos luego por variable de entorno en Terraform
table_name = os.environ.get('TABLE_NAME', 'visitor_counter')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Actualizamos el contador en DynamoDB
        # El ID 'index' es arbitrario para identificar nuestra fila de estadísticas
        response = table.update_item(
            Key={'id': 'total_visits'},
            UpdateExpression='ADD visits :inc',
            ExpressionAttributeValues={':inc': 1},
            ReturnValues='UPDATED_NEW'
        )
        
        # Extraemos el nuevo valor
        count = response['Attributes']['visits']
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*', # Importante para evitar errores de CORS
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'count': int(count)})
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'No se pudo actualizar el contador'})
        }