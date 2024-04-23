# language detection and translator API using FastAPI

This API is designed to classify language  provided in text format and translate language from arabic to english and from english to arabic. It utilizes FastAPI, a modern, fast (high-performance), web framework for building APIs with Python.


## Table of content

- [FastAPI boilerplate](#fastapi-language detection and translator )
  - [Table of content](#table-of-content)
  - [Overview](#overview)
  - [Development](#development)
    - [Prerequisites](#prerequisites)
    - [Configuration](#configuration)
    - [Run instructions](#run-instructions)
  - [Docker instructions](#docker-instructions)
    - [For Production](#for-production)
      - [Build image](#build-image)
      - [Publish image](#publish-image)
      - [Test it](#test-it)
  - [API Details](#api-details)


## Overview

This project aims to create a language detection and translation API using FastAPI, a modern and high-performance web framework for building APIs with Python. The API will provide functionalities for identifying the language of text provided in text format and for translating text between Arabic and English languages. It serves as a versatile tool for developers seeking efficient solutions for language processing tasks.

## Model WEIGHTS 
- https://drive.google.com/drive/folders/1f_LvkZq3vvYZTaBCPAcZ_0X6K32aRp_G?usp=sharing
-Kindly Download Model Weights from above link and put it in (./api/src/static/Model_translation)
## Development

### Prerequisites

- Python v3.10

### Configuration

- Copy [`example.dev.env`](example.dev.env) to `dev.env`

- Adapt `dev.env`

### Run instructions

- Create a virtual environment and install dependencies

```sh
cd api
pip install virtualenv
python3 -m venv ./env
source env/Scripts/activate 
pip install -r requirements.txt
```

- Load env variables

```sh
# For windows
set -a && source ../dev.env && set +a

# For linux
source dev.env
```

- Start the server

```sh
python src/main.py
```

- Lint src dir

```sh
flake8 src
```

## Docker instructions

### For Production

- Copy [example.env](example.env) to .env file and adapt you variables [See configuration section](#configuration)

#### Build image

```sh
make build
```

#### Publish image

```sh
make publish
```

#### Test it

```sh
docker-compose -f docker-compose.yml up -d
```

## API Details

- [API Details](./api/README.md)
