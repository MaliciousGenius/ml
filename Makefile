.PHONY: *

export NAME?=$(shell echo $(shell basename $(shell pwd)) | awk '{print tolower($0)}')

$(NAME): image
	@docker-compose up -d
	@docker-compose run $(NAME)-console /bin/bash -c "/scripts/_pipeline.sh"
	@docker-compose run $(NAME)-console /bin/bash

image:
	@docker-compose build

clean:
	@docker-compose down
	@rm -rf ./_vol*
	@rm -rf ./ml-crawler/workers/*/__pycache__

info:
	@docker-compose logs
	@docker-compose ps
