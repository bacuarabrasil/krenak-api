# krenak_api

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### List of services: ###

* Dev server: [https://example.com/](https://example.com/)

### Documentation: ###

* [Architecture overview](docs/architecture_overview.md)
* [Backend: Routine tasks](docs/commands.md)
* [Backend: Pre-commit hook](docs/pre_commit_hook.md)

### Extra docs: ###

* Lean Inception: https://app.mural.co/t/unb8767/m/unb8767/1614092911460/b5f5678c0ddcafacd682dfb9db9fb209e0f91445
* Backlog: https://docs.google.com/document/d/11a3qDRTpSBvCjtpqOBNP6RLADUFVMZRoZGMzShFE8Ps
* Project's overview: https://docs.google.com/document/d/1Fo1LYQZdXIAIFwzdK1BqizclFXuXRK8eu9Kq--v6VSU
* Kanban: https://github.com/bacuarabrasil/krenak/projects/1


### API documentation: ###

* ReDoc web UI: [https://example.com/_platform/docs/v1/redoc/](https://example.com/_platform/docs/v1/redoc/)
* Swagger web UI: [https://example.com/_platform/docs/v1/swagger/](https://example.com/_platform/docs/v1/swagger/)
* Swagger JSON: [https://example.com/_platform/docs/v1/swagger.json](https://example.com/_platform/docs/v1/swagger.json)
* Swagger YAML: [https://example.com/_platform/docs/v1/swagger.yaml](https://example.com/_platform/docs/v1/swagger.yaml)

### First run: ###

Install Python 3.8.6 & setup virtual environment. We recommend to use [pyenv](https://github.com/pyenv/pyenv) & [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv):

```bash
pyenv install 3.8.6
pyenv virtualenv 3.8.6 krenak_api
pyenv activate krenak_api
```

Update `pip` & `setuptools`, install `fabric`, `invoke` & `pip-tools`:

```bash
pip install -U fabric invoke pip pip-tools setuptools
```

```bash
pip-compile requirements-build.in && pip-compile requirements-dev.in
```

Install Python requirements:

```bash
fab pip.sync
```

Copy initial settings for Django project:

```bash
cp ./api/.env.example ./api/.env
```

Generate `SECRET_KEY`:

```bash
./api/manage.py generate_secret_key
```

and write it to `./api/.env`:

```
KRENAK_API_SECRET_KEY=<your-generated-key>
```

Run backing services (require Docker):

```bash
fab compose.up -d
```

Run migrations:

```bash
./api/manage.py migrate
```

Run Django server:

```bash
fab run
```
