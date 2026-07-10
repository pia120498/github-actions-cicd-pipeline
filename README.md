# GitHub Actions CI/CD Pipeline with Docker & Flask

A production-style CI/CD project demonstrating how to automate the build, testing, verification, and publishing of a Dockerized Flask application using **GitHub Actions**, **Docker**, **Docker Compose**, and **MySQL**.

The pipeline automatically builds the application, verifies its health, publishes the Docker image to Docker Hub, and cleans up the execution environment after every workflow run.

---

## Project Overview

This project demonstrates a complete Continuous Integration (CI) workflow for a containerized Python Flask application.

The application connects to a MySQL database, exposes REST endpoints, and is automatically validated through GitHub Actions before publishing the Docker image.

---

## Tech Stack

- Python 3.13
- Flask
- MySQL 8.4
- Docker
- Docker Compose
- GitHub Actions
- Docker Hub
- Git
- Linux (GitHub-hosted Ubuntu Runner)

---

## Features

- Dockerized Flask application
- Multi-stage Docker build
- MySQL database integration
- Environment variable based configuration
- Container health check endpoint
- GitHub Actions CI pipeline
- Docker image publishing to Docker Hub
- Automated smoke testing
- Automatic cleanup of containers after workflow execution

---

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── app.py
│   ├── db.py
│   ├── task_service.py
│   ├── schema.sql
│   ├── requirements.txt
│   ├── templates/
│   └── static/
│
├── Dockerfile
├── docker-compose.yaml
├── .dockerignore
└── README.md
```

---

# CI/CD Pipeline Workflow

The GitHub Actions workflow performs the following steps:

1. Checkout repository
2. Set up Python 3.13
3. Install application dependencies
4. Authenticate with Docker Hub
5. Build Docker image
6. Push Docker image to Docker Hub
7. Start application using Docker Compose
8. Wait for containers to become healthy
9. Verify running containers
10. Execute application smoke test
11. Stop and remove containers

---

## GitHub Actions Pipeline

Workflow file:

```
.github/workflows/ci.yml
```

Main stages:

- Checkout Repository
- Setup Python
- Install Dependencies
- Login to Docker Hub
- Build Docker Image
- Push Docker Image
- Start Containers
- Verify Application Health
- Cleanup Environment

---

## Health Check

The application exposes a health endpoint used by both Docker and GitHub Actions.

```
GET /health
```

Example response:

```json
{
  "status": "UP"
}
```

This endpoint is used to verify that the application started successfully before continuing the pipeline.

---

## Docker Image

The CI pipeline automatically publishes the application to Docker Hub.

Images are tagged as:

```
latest
```

and

```
<git-commit-sha>
```

Example:

```
priyamal/github-actions-cicd-pipeline:latest
```

---

## Run Locally

Clone the repository

```bash
git clone https://github.com/pia120498/github-actions-cicd-pipeline.git
```

Move into the project

```bash
cd github-actions-cicd-pipeline
```

Build and start the application

```bash
docker compose up --build -d
```

Verify the application

```bash
curl http://localhost:5000/health
```

Stop the application

```bash
docker compose down
```

---

## Docker Commands Used

Build image

```bash
docker build -t flask-app .
```

Start containers

```bash
docker compose up -d
```

View running containers

```bash
docker ps
```

View compose status

```bash
docker compose ps
```

View logs

```bash
docker compose logs
```

Stop containers

```bash
docker compose down
```

---

## Database

MySQL runs as a separate Docker container.

Example verification:

```sql
USE taskdb;

SELECT * FROM tasks;
```

---

## Docker Hub

The GitHub Actions workflow authenticates using encrypted GitHub Secrets:

- DOCKERHUB_USERNAME
- DOCKERHUB_TOKEN

This ensures credentials are never stored in the repository.

---

## Learning Outcomes

This project demonstrates practical experience with:

- Continuous Integration (CI)
- GitHub Actions Workflows
- Docker Image Build & Tagging
- Docker Compose
- Container Health Checks
- Environment Variables
- Multi-stage Docker Builds
- Docker Hub Authentication
- Secret Management
- Automated Smoke Testing
- CI Pipeline Cleanup

---

## Future Enhancements

- Unit testing with Pytest
- Code coverage reporting
- Security scanning using Trivy
- Image vulnerability scanning
- Kubernetes deployment
- Helm charts
- Continuous Deployment (CD) to AWS
- Monitoring using Prometheus & Grafana

---

## Author

**Priya Malewadkar**

GitHub: https://github.com/pia120498
