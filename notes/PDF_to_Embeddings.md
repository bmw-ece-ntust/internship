> Michael Harditya (TEEP)
# PDF to Embeddings
To create RAG, first the data (in this case, PDF file of ORAN Documentation) strings must be converted into embeddings and placed in a vector database. This note is the summary about the task.
## **Table of Contents**
- [PDF to Embeddings](#pdf-to-embeddings)
  - [**Table of Contents**](#table-of-contents)
  - [**Parse PDF to Text with Tika**](#parse-pdf-to-text-with-tika)
    - [**About Apache Tika**](#about-apache-tika)
    - [**Implementation**](#implementation)

## **Parse PDF to Text with Tika**
To easily parse PDF files into text, this implementation use [Apache Tika](https://tika.apache.org/), a content analysis toolkit from Apache. This toolkit runs asynchronously in the background using `java` as a server, and can be called using `tika` Python library. 

### **About Apache Tika**
Apache Tika is another software from Apache that detects and extracts metadata and text from over a thousand different file types (such as PPT, XLS, and PDF). Tika captures both metadata and content of the file, with various extra configuration like language to be used, the text encoding used on the file, and many more.

Tika have two kind of interfaces, the first one is `Parser`. The `parse` method takes the document to be parsed and related metadata as input and outputs the results as XHTML SAX events and extra metadata. `Parser` use various parser classes from various existing libraries, and automatically assign the best parser to be used on the document.

The second interface is the `Detector`, this interface captures specific data defined by a special features of the data. The `detect` method also takes the document to be scanned and its metadata as input, and previously assigned features in the `Detector` interface. Some of available detections are Mime Magic Detection, Resource Name Based Detection, Container Aware Detection, and Language Detection.

>[!NOTE]The `Detector` interface is not going to be implemented for this case.

### **Implementation**
This commit includes a new utility [`utils/pdf_parser.py`](../utils/pdf_parser.py) to parse pdf file using implementation mentioned before. There are several steps to be done before using the utility:
1. **Download the Apache Tika jar file**, 
   
   Download the `tika-server-standard-x.x.x.jar`, can be accessed from this [link](https://tika.apache.org/download.html).
2. **Run the Tika Server Jar**, using:
   ```
   java -jar /path/to/tika-server-standard-x.x.x.jar
   ```
   **To Check:** if succeed, it should started to show the server log on the command prompt, and it should be running on `http://localhost:9998/tika`, check using
   ```
   netstat -ano | findstr :9998
   ```
   it should shows that a process is running on that port number. 
   >[!IMPORTANT]If it failed (the log says it failed), it is possible that another process is using port number `9998`, try to change to another port or kill that process.
3. **Install Tika for Python**
   
   Tika is a server, so it can be accessed as a normal `http` access, but it returns as a XML object. To speed up implementation process, use `tika` Python library instead to fetch the content as text. Install the library using
   ```
   pip install tika
   ```
4. **Call PDFParser Class from Utilities**
   
   This step can be done by calling the `PDFParser` class, it automatically uses local Tika server instead of remote. Here is a short demonstration to use the utility.
   ```python
    from utils.pdf_parser import PDFParser
    folder = 'pdf_folder'
    parser = PDFParser()
    text = parser.parse_folder(folder)
    print(text[0])
    ```
    This example calls `parse_folder(folder)` method that automatically opens a folder, and find pdfs inside that folder and send it to Tika server.

    >[!NOTE]Additional functionality of `PDFParser` is expected to be added when needed.


