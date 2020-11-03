.PHONY: default
default: build run

.PHONY: build
build:
	pipreqs --force
	docker build -t ml .

.PHONY: run
run:
	docker run --rm -v ${PWD}/data:/data ml

.PHONY: local-dep
local-dep:
	pip3 install pipreqs
