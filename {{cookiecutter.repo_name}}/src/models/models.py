import os
import sys
from pathlib import Path

import click
import __main__
import logging


def dev_model():
    logger.info("In dev model")


@click.group()
def cli():
    pass


@cli.command()
@click.argument('model_funcs', nargs=-1)
def compile(model_funcs):
    """
    Compiles the models specified by `model_funcs`

    :param model_funcs: the names of the models that
        correspond to functions names in this script

    :return: None
    """

    logger.info("compiling models..")

    for func in model_funcs:
        try:
            # TODO: create functions that compile various kinds of models
            m = __main__.__dict__[func]()
            # TODO: Save model `m`
        except KeyError:
            logger.error('Invalid model. Implementation not available.')
            sys.exit(-1)

    logger.info("Done.")


@cli.command()
@click.option('--data_dir', type=click.Path(exists=True), required=True)
@click.option('--model', required=True)
@click.option('--test', default=False)
def fit(data_dir, model, test=False):
    """
    for training the model (using command line).

    :param data_dir: the processed data
    :param model: the model to train
    :param test: the model will be tested if this is set to True

    :return: None


    """

    logger.info(f'training model')

    # TODO: load model from file
    for dirpath, dirs, files in os.walk(data_dir):
        for filename in files:
            fname = os.path.join(dirpath,filename)
            # TODO: read data file
            # TODO: train model
            # TODO: test model if needed

    logger.info('model trained' + (' and tested.' if test else '.'))


def create_logger():
    log_fmt = '[%(levelname)s %(asctime)s]: %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)


if __name__ == '__main__':
    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]
    create_logger()
    logger = logging.getLogger(__name__)
    cli()
