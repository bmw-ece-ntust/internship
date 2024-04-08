import os
import tika
from tika import parser


class PDFParser:
    """
    A class for parsing text from PDF files in a given folder.

    Requirements:
    - Tika library must be installed. You can install it using pip: `pip install tika`

    Parameters:
    - local_server (bool): If True, use Tika's local server for parsing. If False, use Tika's default server.
                           Default is True.

    Usage:
    1. Create an instance of the PDFParser class, optionally specifying the `local_server` parameter.
    2. Call the `parse_folder` method, passing the path to the folder containing the PDF files.
       This method will return a list of parsed texts from the PDF files in the folder.
    """

    def __init__(self, local_server=True):
        """
        Initialize the PDFParser object.

        Parameters:
        - local_server (bool): If True, use Tika's local server for parsing. If False, use Tika's default server.
                               Default is True.
        """
        if local_server:
            tika.TikaClientOnly = True
        else:
            tika.TikaClientOnly = False

    def parse_folder(self, folder_path):
        """
        Parse text from PDF files in a given folder.

        Parameters:
        - folder_path (str): The path to the folder containing the PDF files.

        Returns:
        - parsed_texts (list): A list of parsed texts from the PDF files in the folder.
        """
        parsed_texts = []
        for filename in os.listdir(folder_path):
            if filename.endswith(".pdf"):
                file_path = os.path.join(folder_path, filename)
                text = parser.from_file(file_path)
                parsed_texts.append(text['content'])
        return parsed_texts

