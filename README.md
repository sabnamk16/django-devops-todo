# Django Todo App — AWS DevOps Project

A full-stack Todo application containerized with Docker and deployed on AWS with a complete CI/CD pipeline.


## Tech Stack
- **Backend:** Django (Python)
- **Database:** AWS RDS PostgreSQL (production) / SQLite (local)
- **Containerization:** Docker
- **Container Registry:** AWS ECR
- **Hosting:** AWS EC2
- **CI/CD:** GitHub Actions
- **Security:** AWS IAM Roles

## CI/CD Pipeline
Every push to `main` automatically:
1. Builds a new Docker image
2. Pushes it to AWS ECR
3. SSHs into EC2 and redeploys the container

## Run Locally
```bash
git clone https://github.com/sabnamk16/django-devops-todo.git
cd django-devops-todo
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## ☁️ AWS Services Used
- **EC2** — Hosts the Docker container
- **ECR** — Stores Docker images
- **RDS** — Managed PostgreSQL database
- **IAM** — Roles and permissions for secure access
