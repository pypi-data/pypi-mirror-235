from typing import Optional

def write(path: str, data: str, mode: Optional[str]) -> None:
    """
    Write data to a file.

    Parameters:
    - path (str): The path to the file.
    - data (str): The data to be written to the file.
    - mode (str, optional): The mode in which the file is opened. 
      Defaults to 'a' (append). Other valid modes are 'w' (write).

    Raises:
    - ValueError: If an invalid mode is provided.

    Returns:
    - None
    """

def read(path: str) -> None:
    """
    Read data from a file.

    Parameters:
    - path (str): The path to the file.

    Returns:
    - str: The content of the file.

    If the file is not found, an empty string is returned.
    """
