# 🚀 Serverless Visitor Counter with Docker & CI/CD

Este proyecto implementa una arquitectura **Serverless** moderna en AWS para contar las visitas de un sitio web. Utiliza **Docker** para empaquetar la lógica del backend, **Terraform** para la infraestructura y **GitHub Actions** para el despliegue automático.

## 🏗️ Arquitectura
- **Frontend:** HTML/JS alojado en **Amazon S3** (Static Website Hosting).
- **Backend:** Imagen de contenedor en **Amazon ECR** ejecutada por **AWS Lambda**.
- **API:** **Amazon API Gateway** (HTTP API).
- **Base de Datos:** **Amazon DynamoDB** (NoSQL).
- **CI/CD:** **GitHub Actions** (Build de Docker, Push a ECR y Sync de S3).



## 🛠️ Tecnologías
* **IaC:** Terraform
* **Contenedores:** Docker
* **Lenguaje:** Python 3.11 (Boto3)
* **Cloud:** AWS (S3, Lambda, DynamoDB, ECR, IAM, API Gateway)
* **Automatización:** GitHub Actions

## 🚀 Guía de Despliegue

### 1. Requisitos Previos
- AWS CLI configurado.
- Terraform instalado.
- Un bucket de S3 creado manualmente para el `terraform.tfstate`.

### 2. Infraestructura (Terraform)
```bash
cd iac
terraform init
# Nota: Comenta los bloques de Lambda y API Gateway en el primer apply
terraform apply