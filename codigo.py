import boto3
import os

def generate_text_file(file_path):
    with open(file_path, 'w') as file:
        file.write("¡Hola, esto es un archivo de texto generado!")

def upload_to_s3(file_path, bucket_name, object_key):
    s3 = boto3.client('s3', region_name='eu-south-2')
    try:
        with open(file_path, 'rb') as data:
            s3.upload_fileobj(data, bucket_name, object_key)
        print(f'Successfully uploaded {file_path} to {bucket_name}/{object_key}')
    except Exception as e:
        print(f'Error uploading file: {str(e)}')

if __name__ == "__main__":
    # Definir parámetros
    file_path = 'archivo.txt'  # Ruta local del archivo a generar y subir
    bucket_name = 's3actividad'
    object_key = 'carpeta/archivo.txt'

    # Generar el archivo de texto
    generate_text_file(file_path)

    # Subir el archivo a S3
    upload_to_s3(file_path, bucket_name, object_key)

    # Eliminar el archivo local después de subirlo a S3
    os.remove(file_path)
