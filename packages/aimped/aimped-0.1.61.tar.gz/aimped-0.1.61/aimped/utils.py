# Author: AIMPED
# Date: 2023-March-11
# Description: This file contains utility functions

import json
import logging
import numpy as np
from .version import __version__
import logging

def get_version():
    """Returns the version of aimped library."""
    return f'aimped version: {__version__}'


def get_handler(log_file='KSERVE.log', log_level=logging.DEBUG):
    """Returns the logger object for logging the output of the server.
    Parameters:
    ----------------
    log_file: str
        The name of the log file to which the logs will be written.
    log_level: int
        The logging level (e.g., logging.DEBUG, logging.INFO, logging.ERROR).  
    Returns:
    ----------------
    logger: logging.Logger
        The configured logger object.
    """
    # Create a FileHandler for writing logs to the specified log_file.
    f_handler = logging.FileHandler(log_file, encoding='utf-8', mode='w')
    # Define a log message format.
    formatter = logging.Formatter('[%(asctime)s %(filename)s:%(lineno)s] - %(message)s')
    # Set the formatter for the file handler.
    f_handler.setFormatter(formatter)
    # Set the logging level for the file handler.
    f_handler.setLevel(log_level)
    # Get the root logger.
    logger = logging.getLogger()
    # Set the logging level for the logger itself.
    logger.setLevel(log_level)
    # Add the file handler to the logger.
    logger.addHandler(f_handler)
    return logger


def cuda_info():
    """
    Returns information about the CUDA devices if CUDA is available.

    Returns:
        dict or str: A dictionary containing CUDA information or a string indicating CUDA availability.
    """
    try:
        if torch.cuda.is_available():
            cuda_info = {
                "cuda is available": True,
                "device count": torch.cuda.device_count(),
                "current device": torch.cuda.current_device(),
                "device name": torch.cuda.get_device_name(0),
                "Memory Usage": {
                    "Allocated": round(torch.cuda.memory_allocated(0) / 1024**3, 1),
                    "Cached": round(torch.cuda.memory_reserved(0) / 1024**3, 1)
                }
            }
            return cuda_info
        else:
            return "CUDA is not available"
    except ImportError:
        return "PyTorch is not installed. Make sure to install PyTorch to use CUDA."
    except Exception as e:
        return f"Error while fetching CUDA information: {str(e)}"


class NumpyFloatValuesEncoder(json.JSONEncoder):
    """This class is used to convert numpy float32 to float"""
    def default(self, obj):
        if isinstance(obj, np.float32):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


# TODO: test these functions
if __name__ == '__main__':
    print(get_version())