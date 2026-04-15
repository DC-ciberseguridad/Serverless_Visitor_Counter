resource "aws_ecr_repository" "lambda_repo" {
  name                 = "visitor-counter-repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true # Escanea vulnerabilidades al subir la imagen
  }
}

output "ecr_repository_url" {
  value = aws_ecr_repository.lambda_repo.repository_url
}