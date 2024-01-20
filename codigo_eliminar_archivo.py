import boto3
import os

def delete_object_s3(bucket_name, object_key):
    s3 = boto3.client('s3', region_name='eu-south-2')
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_key)
        print(f'Successfully deleted {object_key} from {bucket_name}')
    except Exception as e:
        print(f'Error deleting object: {str(e)}')

if __name__ == "__main__":
    # Definir parámetros
    bucket_name = 'mi-bucket-s3'
    object_key = 'carpeta/archivo.txt'

    # Eliminar el archivo en S3
    delete_object_s3(bucket_name, object_key)