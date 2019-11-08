import os
import math

import numpy as np

from pandas import DataFrame

from .constant import COMPRESSED_SUB_PATH, ORIGNAL_SUB_PATH


def file_content_2_data_frame(file_content: str) -> DataFrame:
    """
    Create a ``DataFrame`` with the ``file_content``

    Args: 
        file_content (str): content of file

    Returns:
        DataFrame: Content of file as DataFrame
    """
    
    # list comprehension for performance
    return DataFrame([[int(x), int(y), float(height)] for x, y, height in [row.split(" ") for row in file_content.splitlines()]])
    

def data_frame_2_file_content(data_frame: DataFrame) -> list:
    """
    Converts the given ``data_frame`` into a list of lines as file content

    Args:
        data_frame: to be serialized

    Returns:
        list: of lines for serialization as file
    """

    # list comprehension for performance
    return [f"{int(x)} {int(y)} {round(float(height), 2)}" for x, y, height in data_frame.values]


def compress_data_frame(data_frame: DataFrame, tile_size: int) -> DataFrame:
    """
    Compress the given ``DataFrame``. Uses windows of size ':math:`tile\ size \\times tile\ size`' and calculates their mean.

    Use convolution algorithm to compress the neighboring tiles. TODO: see documentation to get an intuition about the convolution implementation.

    Args:
        data_frame (DataFrame): Original DataFrame
        tile_size (int): window size
        
    Returns:
        DataFrame: The compressed pandas.DataFrame
    """

    columns = ["x", "y", "height"]
    data_frame.columns = columns
    data_frame = data_frame.sort_values(["y", "x"])

    y_min = data_frame["y"].min()
    y_max = data_frame["y"].max()
    x_min = data_frame["x"].min()
    x_max = data_frame["x"].max()

    # original x and y coordinates to restore them
    original_x_y = [(x, y) for y in range(y_min, y_max, tile_size) for x in range(x_min, x_max, tile_size)]

    original_size = int(math.sqrt(data_frame.shape[0])) 
    new_size = int(original_size / tile_size)

    df_as_matrix = np.array([data_frame[i:i+original_size]["height"] for i in range(0, data_frame.shape[0], original_size)])

    convolution_matrix = np.zeros((new_size**2, tile_size**2))
    mean_kernel_vector = np.full((tile_size**2, 1), 1/(tile_size**2)) # convolution kernel as vector to mean cells in window

    # reshape windows into rows of the ``convolution_matrix``
    row_number = 0
    for y in range(new_size):
        for x in range(new_size):
            convolution_matrix[row_number, :] = df_as_matrix[y * tile_size:y * tile_size + tile_size, x * tile_size:x * tile_size + tile_size].flatten()
            row_number += 1

    # calculate the actual convolution as dot product
    convolution_result = convolution_matrix.dot(mean_kernel_vector)

    # create compressed ``DataFrame``
    compressed_data_frame = DataFrame([[x_y[0], x_y[1], height] for x_y, height in zip(original_x_y, convolution_result[:,0])], dtype=np.float32)
    compressed_data_frame.columns = columns

    return compressed_data_frame


def create_directories(download_path: str, keep_original: bool) -> (str, str):
    """
    Simple helper function that creates all necessary directories.

    Args:
        download_path (str): download path
        keep_original (bool): indicates whether the original directory is necessary or not.

    Returns:
        str, str: path for original files, path for compressed files
    """

    original_path = os.path.join(download_path, ORIGNAL_SUB_PATH)
    compressed_path = os.path.join(download_path, COMPRESSED_SUB_PATH)

    if not os.path.exists(original_path) and keep_original:
        os.mkdir(original_path)

    if not os.path.exists(compressed_path):
        os.mkdir(compressed_path)

    return original_path, compressed_path
    