.PHONY: test

# obtain the absolute path to metacademy-application
MAKEFILE_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR := $(realpath $(MAKEFILE_DIR))

# assumes the base project directory is the parent of metacademy-application
BASE_DIR := $(realpath $(MAKEFILE_DIR)/..)

APP_DIR = $(BASE_DIR)/metacademy-application


test: | $(APP_DIR)
	python $(APP_DIR)/content_server/utils.py test

$(APP_DIR):
	git clone https://github.com/metacademy/metacademy-application.git $(APP_DIR)
	cd $(APP_DIR); cp config-template.py config.py; cp app_server/settings_local-template.py app_server/settings_local.py
