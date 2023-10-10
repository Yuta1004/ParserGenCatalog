IMAGE := pgencatalog:javacc

SRC := $(shell pwd)/src
OPTS := --rm -it -v $(SRC):/workdir/src

run:
	docker run $(OPTS) $(IMAGE) /bin/bash -c "make run"

build:
	docker run $(OPTS) $(IMAGE) /bin/bash -c "make build"
	sudo chown $(shell id -u):$(shell id -u) src/*

clean:
	echo "TODO"

image:
	docker build -t $(IMAGE) .
