# 🚀 End-to-End CI/CD Pipeline with Flask, Jenkins, Docker & Kubernetes on AWS

## 📌 Project Overview
This project demonstrates a **production-style CI/CD pipeline** that automates the process of building, containerizing, and deploying a **Flask application** to **Kubernetes on AWS**.

The pipeline takes application code from **GitHub commit to live deployment** using **Jenkins, Docker, AWS ECR, and Kubernetes**, following real-world DevOps best practices.

---

## 🎯 Objectives
- Automate application delivery using CI/CD
- Build optimized Docker images
- Push images securely to AWS ECR
- Deploy applications on Kubernetes with zero downtime
- Implement health checks, resource limits, and rollout verification

---

## 🏗️ Architecture

Developer
   |
   v
GitHub Repo
   |
   v
CI/CD Pipeline (Jenkins / GitHub Actions)
   |
   v
Docker Build
   |
   v
AWS ECR
   |
   v
Kubernetes (EKS / EC2-based K8s)
   |
   v
Application exposed via Ingress / LoadBalancer

## 📁 Repository Structure

devops-cicd-aws-kubernetes/
│
├── app/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── k8s/
│ ├── deployment.yaml
│ ├── service.yaml
│ └── ingress.yaml
│
├── jenkins/
│ └── Jenkinsfile
│
├── diagrams/
│ └── architecture.png
│
└── README.md


---

## 🔄 CI/CD Pipeline Flow

1. Developer pushes code to GitHub
2. Jenkins pipeline is triggered
3. Docker image is built
4. Image is tagged with build number
5. Image is pushed to AWS ECR
6. Kubernetes deployment is updated
7. Rollout status is verified

---

## ☸️ Kubernetes Highlights
- **Replicas:** Ensures high availability
- **Resource Requests & Limits:** Production-ready configuration
- **Liveness & Readiness Probes:** Application health monitoring
- **Service & Ingress:** Proper traffic routing

---

## 🐳 Docker Highlights
- Lightweight `python:alpine` base image
- Layer caching for faster builds
- Environment variable based configuration

---

## 🚀 How to Deploy (High Level)

### Prerequisites
- Jenkins with Docker, AWS CLI, kubectl installed
- AWS ECR repository created
- Kubernetes cluster configured
- IAM permissions for ECR & EKS

### Deployment
```bash
kubectl apply -f k8s/
kubectl rollout status deployment/flask-app
