.PHONY: clean data lint requirements data train test

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}
RAW_DATA_DIR = data/raw
PROC_DATA_DIR = data/processed
CONDA_PATH = {{ cookiecutter.conda_path }}
ENV = {{ cookiecutter.env_name }}
SHELL = /bin/bash

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Compile model
compile:
	source $(CONDA_PATH)/bin/activate $(ENV)
	$(PYTHON_INTERPRETER) src/models/models.py compile dev_model


## Make Dataset
data:
	source $(CONDA_PATH)/bin/activate $(ENV)
	$(PYTHON_INTERPRETER) src/data/make_dataset.py $(RAW_DATA_DIR) $(PROC_DATA_DIR)
	
## Train model
fit:
	source $(CONDA_PATH)/bin/activate $(ENV)
	$(PYTHON_INTERPRETER) src/models/models.py fit --data_dir $(PROC_DATA_DIR) --model models/ --test True


## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	source $(CONDA_PATH)/bin/activate $(ENV)
	flake8 src
	
	


