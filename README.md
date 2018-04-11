# My API

# Unit Testing
```
tox
open htmlcov/index.html
```

# Running locally
```
pip install .; run.py
```

# Docker
## building
```
docker build -t myapp:0.0.1 .
```
## running
```
docker run -p 10000:10000 myapp:0.0.1
```

# Running in Docker
TODO

## Test CURLs
```
curl -v -H "Content-Type: application/json" -X POST localhost:10000/baz -d '{"query_string" : "amaaaaaaazing"}'
```

```
curl localhost:10000/foo/asdf
```
