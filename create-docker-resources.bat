docker run --name postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=postgres -e POSTGRES_DB=postgres -e POSTGRES_PORT=5432 -p 5432:5432 -d postgres
docker run --name redis -p 6379:6379 -d redis:alpine