# **Sphinx Installation**

**Goal：**
* Successfully install Sphinx
* Set up a monitoring environment.

**Main Reference：**

* [Sphinx Installation](https://www.sphinx-doc.org/en/master/tutorial/getting-started.html)


## **Table of Contents**
- [**Sphinx Installation**](#sphinx-installation)
  - [**Table of Contents**](#table-of-contents)
  - [**Overview**](#overview)
  - [**Installation (Ubuntu 22.04)**](#installation-ubuntu-2204)
    - [**Step 1: Install Python and pip**](#step-1-install-python-and-pip)
    - [**Step 2: Install Sphinx**](#step-2-install-sphinx)
    - [**Step 3: Verify Installation**](#step-3-verify-installation)
  - [**Get Started**](#get-started)
    - [**Step 1: Project Setup**](#step-1-project-setup)
    - [**Step 2: Virtual Environment and Sphinx Installation**](#step-2-virtual-environment-and-sphinx-installation)
    - [**Step 3: Creating Documentation Layout**](#step-3-creating-documentation-layout)
    - [**Step 4: Rendering Documentation**](#step-4-rendering-documentation)

## **Overview**

Sphinx is a tool that makes it easy to create intelligent and beautiful documentation for various output formats and purposes. Sphinx uses reStructuredText or MyST markdown as its markup language, which are both powerful and easy to use. Sphinx is written in Python and supports Python 3.9+. It builds upon the shoulders of many third-party libraries such as Docutils and Jinja, which are installed when Sphinx is installed.

Sphinx supports extensive cross-references, automatic indices, code handling, themes, and extensions to enhance the documentation quality and usability. Sphinx is community supported and welcomes contributions from anyone who wants to improve the project

## **Installation (Ubuntu 22.04)**

### **Step 1: Install Python and pip**

If Python is not already installed on your system, you can install it along with pip:

```
sudo apt-get update
sudo apt-get install python3
```
### **Step 2: Install Sphinx**

```
sudo apt-get install python3-sphinx
```

Output:
```bash
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3-sphinx is already the newest version (4.3.2-1).
0 upgraded, 0 newly installed, o to remove and 74 not upgraded.
```

### **Step 3: Verify Installation**
Verify that Sphinx has been installed successfully:

```
sphinx-build --version
```
You should see an output similar to the following:

```bash
sphinx-build 4.0.2
```

## **Get Started**

### **Step 1: Project Setup**

In a new directory, initialize your project by creating a file called `README.rst` with the following content:

```
Lumache
=======

**Lumache** (/lu'make/) is a Python library designed for cooks and food enthusiasts, allowing them to craft recipes by blending random ingredients.
```

### **Step 2: Virtual Environment and Sphinx Installation**

Now, let's create a Python virtual environment and install the necessary tools. Open a command line terminal, navigate to your project directory, and execute the following commands:

```
python -m venv .venv
source .venv/bin/activate
python -m pip install sphinx
```

### **Step 3: Creating Documentation Layout**

Now, let's set up the basic directory and configuration layout for your documentation inside the `docs` folder. Run the following command:

```
sphinx-quickstart docs
```

Answer the presented questions as follows:

- Separate source and build directories (y/n) [n]: Type "y" and press Enter.
- Project name: Type "Lumache" and press Enter.
- Author name(s): Type "Graziella" and press Enter.
- Project release []: Type "0.1" and press Enter.
- Project language [en]: Leave it empty (default, English) and press Enter.

### **Step 4: Rendering Documentation**

Now, you have everything needed to render the documentation as HTML for the first time. Execute the following command:

```
sphinx-build -M html docs/source/ docs/build/
```

Finally, open docs/build/html/index.html in your browser to view the freshly created documentation of Lumache.

You can use this command to open it through terminal:
```
xdg-open docs/build/html/index.html
```

Congratulations, you've successfully set up your Lumache project and generated its documentation!

![image](https://github.com/bmw-ece-ntust/internship/assets/87703952/7dfa6427-0880-4c7b-966d-a655373b1605)

