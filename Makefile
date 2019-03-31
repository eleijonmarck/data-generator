help:
	@cat Makefile

DATA?="sample-datasets"
DOCKER_FILE=Dockerfile
DOCKER=keras
SRC?=$(shell dirname `pwd`)

build:
	docker build -t keras -f $(DOCKER_FILE) .

bash: build
	docker run -it -v $(DATA):/data $(DOCKER) bash

ipython: build
	docker run -it -v -v $(DATA):/data $(DOCKER) ipython

example-train: build
	docker run -it -v $(DATA):/data $(DOCKER) ipython -i -c "%load textgen/train_destination_generator.py"

example-pretrained: build
	docker run -it -v $(DATA):/data ipython -i -c "%load textgen/pretrained_destination.py"
