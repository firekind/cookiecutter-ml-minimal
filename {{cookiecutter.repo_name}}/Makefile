.PHONY: clean data lint requirements data train test

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}
RAW_DATA_DIR = data/raw
PROC_DATA_DIR = data/processed
CONDA_PATH = {{ cookiecutter.conda_path }}
ENV = {{ cookiecutter.env_name }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Compile model
compile:
	$(CONDA_PATH) activate $(ENV)
	$(PYTHON_INTERPRETER) src/models/models.py compile dev_model


## Make Dataset
data:
	$(CONDA_PATH) activate $(ENV)
	$(PYTHON_INTERPRETER) src/data/make_dataset.py $(RAW_DATA_DIR) $(PROC_DATA_DIR)
	
## Train model
fit:
	$(CONDA_PATH) activate $(ENV)
	$(PYTHON_INTERPRETER) src/models/models.py fit --data_dir $(PROC_DATA_DIR) --model models/ --test True


## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	$(CONDA_PATH) activate $(ENV)
	flake8 src
	


