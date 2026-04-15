# Usamos la imagen oficial de AWS para Lambda con Python 3.11
FROM public.ecr.aws/lambda/python:3.11

# Copiamos el archivo de requisitos al directorio de trabajo de Lambda
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Instalamos las dependencias
RUN pip install -r requirements.txt

# Copiamos el código de nuestra función
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Configuramos el "Handler" (archivo.función_a_ejecutar)
CMD [ "lambda_function.lambda_handler" ]