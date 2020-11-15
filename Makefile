.PHONY: *

export NAME?=$(shell echo $(shell basename $(shell pwd)) | awk '{print tolower($0)}')

$(NAME): image
	@docker-compose up -d
	@docker-compose run $(NAME)-console /bin/bash -c "sleep 30s && /scripts/pipeline.sh"

image:
	@docker-compose build

clean:
	@docker-compose down
	@rm -rf ./_vol*

info:
	@docker-compose logs
	@docker-compose ps
