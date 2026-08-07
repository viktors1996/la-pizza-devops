Markdown# 🍕 La Pizza DevOps Infrastructure

[![CI/CD Pipeline](https://github.com/viktors1996/la-pizza-devops/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/viktors1996/la-pizza-devops/actions)
![Docker Compose](https://img.shields.io/badge/Docker--Compose-v2.x-blue?logo=docker)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple?logo=terraform)
![Ansible](https://img.shields.io/badge/Ansible-Automation-red?logo=ansible)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An end-to-end DevOps project featuring containerization, CI/CD automation, comprehensive monitoring (Observability), and Infrastructure as Code (IaC) for deploying the **La Pizza** web application to AWS cloud infrastructure.

---

## 📐 Architecture Overview

The system follows a microservices architecture with isolated networks, secure reverse proxying, and automated metrics collection:

                              [ User / Web Client ]
                                        │
                                        ▼ (Port 80 / 443)
                             ┌─────────────────────┐
                             │     Nginx Proxy     │ (SSL Termination & Basic Auth)
                             └──────────┬──────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        ▼                               ▼                               ▼
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│   Frontend    │               │ Backend (Flask│               │ Monitoring    │
│   (Nginx)     │               │  + Gunicorn)  │               │ (Grafana UI)  │
└───────────────┘               └───────┬───────┘               └───────────────┘
                                        │
                                        ▼
                                ┌───────────────┐
                                │ PostgreSQL 17 │
                                └───────────────┘

---

## 🛠️ Tech Stack

* **Application:** Python 3.10 (Flask REST API, Gunicorn), PostgreSQL 17, HTML5/CSS/JS (Nginx Static).
* **Containerization:** Docker, Docker Compose (Multi-stage builds).
* **Web Server & Security:** Nginx Reverse Proxy, SSL/TLS Encryption, Basic Auth for admin interfaces, strictly ignored secrets via `.gitignore`.
* **Observability:** Prometheus, Grafana, Node Exporter, cAdvisor, Alertmanager (Telegram Bot API integration).
* **CI/CD Pipeline:** GitHub Actions (Flake8 linting, Pytest, Docker Buildx automation).
* **Infrastructure as Code (IaC):**
  * **Terraform:** Automated AWS Cloud provisioning (EC2 Instance, Security Groups, Elastic IP).
  * **Ansible:** Automated server configuration management, Docker runtime installation, and application deployment.

---

## 📊 Observability & Alerting

* **Prometheus:** Centralized metric collection across containers and system services.
* **Grafana:** Visual dashboards tracking CPU, RAM, disk usage, and network traffic.
* **cAdvisor & Node Exporter:** In-depth host system and container resource analytics.
* **Alertmanager:** Real-time alert dispatching to a Telegram Bot for high CPU load, memory exhaustion, or service outages.

---

## 🚀 Quick Start (Local Development)

### 1. Clone the repository
```bash
git clone [https://github.com/viktors1996/la-pizza-devops.git](https://github.com/viktors1996/la-pizza-devops.git)
cd la-pizza-devops
2. Configure Environment VariablesCopy the template file and fill in your secrets (Database passwords, Telegram Bot tokens):Bashcp .env.example .env
3. Spin up services with Docker ComposeBashdocker compose up -d --build
🔗 Exposed ServicesServiceAccess URLDescriptionMain Web Apphttps://localhostFrontend & API via SSL ProxyGrafana UIhttp://localhost:3000Dashboards & Metrics VisualizationPrometheus UIhttp://localhost:9090Time-series Metrics EngineAlertmanager UIhttp://localhost:9093Alert Management Dashboard☁️ Cloud Deployment Workflow (AWS IaC)Step 1: Provision Infrastructure (Terraform)Bashcd terraform
terraform init
terraform plan
terraform apply
Step 2: Automated Deployment (Ansible)Update ansible/inventory.ini with the provisioned EC2 Public IP and run the playbook:Bashcd ../ansible
ansible-playbook -i inventory.ini playbook.yml
🛡️ DevSecOps & Best PracticesSecret Isolation: Private keys (.key), certificates (.crt), auth databases (.htpasswd), and .env files are strictly excluded from Git tracking.Dynamic Configuration Rendering: Alertmanager configuration is rendered dynamically at runtime using alertmanager.yml.template and .env variables to prevent sensitive data leakage.Principle of Least Privilege: PostgreSQL and Flask Backend operate inside an isolated private Docker network (pizza_net), unreachable directly from the host's public interfaces.👤 AuthorViktor Sogoyan — Junior DevOps EngineerGitHub: @viktors1996LinkedIn: Viktor Sogoyan