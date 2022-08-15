# SimpleApp Requirements:

- Python
- Runs a web service
- exposes a port
- interacts with a db

# Makefile:

* Setting up venv

```make app/setup-venv```

* To Build & Run:

``` make app/build-docker && make app/run-docker```

* To Push to Docker Hub:

``` make app/push-to-docker-hub```
