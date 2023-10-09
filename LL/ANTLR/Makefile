IMAGE := pgencatalog:antlr4

SRC := $(shell pwd)/src
OPTS := --rm -it -v $(SRC):/workdir/src

run:
	docker run $(OPTS) $(IMAGE) /bin/bash -c "make run"

build:
	docker run $(OPTS) $(IMAGE) /bin/bash -c "make build"
	sudo chown $(shell id -u):$(shell id -u) src/*

clean:
	sudo rm -rf src/Expr*.py src/*.interp src/*.tokens src/__pycache__

image:
	docker build -t $(IMAGE) .
