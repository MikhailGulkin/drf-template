## API Music Catalog

API, which is being developed as part of a test task.

### Project Deployment

1.Clone repository

```
git clone https://github.com/MihailGulkin/test-task-music-catalog.git
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
