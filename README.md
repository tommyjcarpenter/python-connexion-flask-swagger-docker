# My API

# Tech Stack
- OpenAPI3
- Connexion
- Flask, with Gevent serving
- Python3.7

See: http://flask.pocoo.org/docs/1.0/deploying/wsgi-standalone/#uwsgi

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
docker build -t myapp:X.Y.Z .
```
## running
```
docker run -p 10000:10000 myapp:X.Y.Z
```

# Test CURLs
```
curl -v -H "Content-Type: application/json" -X POST localhost:10000/baz -d '{"query_string" : "amaaaaaaazing"}'
```

```
curl localhost:10000/foo/asdf
```
