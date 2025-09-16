# Description

CaliCoverage helps people check eligibility for California health coverage programs—including Medi-Cal (California’s Medicaid, public coverage for low- and moderate-income residents) and Covered California (the state’s Affordable Care Act marketplace for private plans and subsidies). 

It uses retrieval-augmented generation over [official DHCS FAQs](https://www.dhcs.ca.gov/services/medi-cal/eligibility/Pages/Medi-Cal_CovCA_FAQ.aspx) to give concise answers. It’s informational only (not legal advice) and will say “I don’t know” when the docs don’t cover something.

This project was implemented for [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) - a free course about LLMs and RAG.


# Dataset

The dataset used in this project scraped from the DHCS FAQs. It contains 44 Q&A pairs under different category. It serves as the knowledge base for the CaliCoverage assistant.

# Technologies
- Python 3.13
- Docker and Docker Compose for containerization
- Minsearch for full-text search (Vector search or hybird search)
- Flask as the API interface (streamit?)
- Grafana for monitoring and PostgreSQL as the backend for it
- OpenAI as an LLM


# Preparation

Since we use OpenAI, you need to provide the API key ...

# Running and application

## Database configuration
TBD ... postgres

## Running with Docker-Compose
TBD ... docker-compose file

## Running locally
TBD ... docker-compase up postgres grafana

## Running with Docker (without compose)
TBD ... Dockerfile

## Time configuration
TBD ... important for inserting logs into the database


# Using the application

## CLI
TBD

## Using `requests`
TBD

## CURL
TBD


# Code

- `app.py`
- `rag.py`
- `ingest.py`
- `db.py`
- `db_prep.py`
- etc

## Interface
We use Flask for serving the application as an API

## Ingestiong
For ingesting knowledge base into minsearch


# Experiments

## Retrieval evaluation

TBD

## RAG flow evaluation
TBD ... used the LLM-as-Judge metric to evaluate the quality of our RAG flow


# Monitoring

TBD ... Grafana for monitoring the application

## Setting up Grafana

