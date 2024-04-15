# DOXYGEN API Document Generation
## Doxygen introduction
Doxygen is a widely-used documentation generator tool in software development. It automates the generation of documentation from source code comments, parsing information about classes, functions, and variables to produce output in formats like HTML and PDF. By simplifying and standardizing the documentation process, Doxygen enhances collaboration and maintenance across diverse programming languages and project scales.
## Installation guide
Doxygen can be installed [here](https://www.doxygen.nl/), just follow the installation step and you'll be ready to go. However, to generate a more complex graph, additional tool such as Graphviz is required. Graphviz can be downloaded [here](https://www.graphviz.org/download/), in short, Graph visualization is a way of representing structural information as diagrams of abstract graphs and networks. 
## Using Doxygen to generate HIGH PHY documentation
Firstly, launch doxygen wizard (DoxyWizard) then specify the working directory of the doxygen and source code directory (which is where the HIGH PHY source code is located).Then specify its where the document will be placed (destination directory), the following is the sample
![image](https://github.com/bmw-ece-ntust/internship/assets/123167913/7db4befc-a5a8-4c24-b9bb-deebc821cb04)
then click on diagram menu on left side of the panel, set into the following
![image](https://github.com/bmw-ece-ntust/internship/assets/123167913/5e9f10b3-d995-4c8c-81ab-61a2ba558b0c)
Next, go to expert tab and search for dot menu on the left side of panel (scroll down), then find the option for including DOT path, set the path for GraphViz dot file path (usually ../GraphViz/bin), the following is a sample of the configuration
![image](https://github.com/bmw-ece-ntust/internship/assets/123167913/73df995d-0dd1-4ebe-82b4-db1c080ce285)
Next, go to run tab and click run 
![image](https://github.com/bmw-ece-ntust/internship/assets/123167913/973e5c76-4263-4d52-a37e-268e6562830a)
(note : incase the run button is grayed out, please click file on corner top left then click save as (just save it randomly), the run button should be available after saving)
