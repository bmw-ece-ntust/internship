import os
import tika
from tika import parser
import re
from utils.text_processor import TextPreprocessor
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
                # prprocess the text
                pre_processed_text = TextPreprocessor().preprocess_text(text['content'])
                # get the Title from the content
                # Use regex to find the first character-filled line
                match = re.search(r"^\s*([^\n]+)", pre_processed_text)
                title = match.group(1) if match else "Unknown Title"
                # Remove dots to lines
                title = title.replace(".", "_")
                # Remove tail spaces
                title = title.strip()
                title = title.replace( " ", "_")
                # preprocess the text and append to the list
                parsed_texts.append({'title': title, 'content': pre_processed_text})

        return parsed_texts

    

