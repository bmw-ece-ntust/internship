import re

class TextPreprocessor:
    def __init__(self):
        self.footer_pattern = r"_{3,}"

    def preprocess_text(self, text):
        """
        Preprocess a text by removing footers.

        Parameters:
        - text (str): The text string to preprocess.

        Returns:
        - cleaned_text (str): The preprocessed text string with footers removed.
        """
        cleaned_text = self.remove_footer(text)
        # Removing excessive newlines
        cleaned_text = re.sub('\n+', '\n', cleaned_text)
        return cleaned_text
    
    def remove_footer(self, text):
        """
        Remove footers from a text.

        Parameters:
        - text (str): The text string to remove footers from.

        Returns:
        - cleaned_text (str): The text string with footers removed.
        """
        # Split the text into lines
        lines = text.splitlines()
        # Initialize a list to store non-footer lines
        non_footer_lines = []
        flag = 0
        # Iterate through each line
        for line in lines:
            # Check if the line matches the footer pattern
            if flag == 0:
                if not re.match(self.footer_pattern, line):
                    non_footer_lines.append(line)
                else:
                    # Footer found, removing next 2 lines
                    flag = 3
            else:
                flag -= 1
        # Join the non-footer lines back into a single string
        cleaned_text = "\n".join(non_footer_lines)
        return cleaned_text