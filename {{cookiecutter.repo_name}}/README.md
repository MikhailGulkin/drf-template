## {{ cookiecutter.app_title }}

{{ cookiecutter.short_description }}

### Project Deployment

1.Clone repository

```
git clone {{ cookiecutter.git_repo }}
```

2.Go to the `src/core` directory and create a `.env` file similar to `.envExample` or run:
```
cp src/core/.envExample src/core/.env
```
3.Run the `make up-prod` command for start project or `docker-compose -f .\docker-compose.prod.yaml up --build` in root 
directory

```
make up-prod
```

4.The application is available at

```
localhost:8000
```
