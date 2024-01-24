# **Installing Sphinx**

## **Table of Contents**
- [**Installing Sphinx**](#installing-sphinx)
  - [**Table of Contents**](#table-of-contents)
  - [**Overview**](#overview)
  - [**Installing in Linux (Debian/Ubuntu)**](#installing-in-linux-debianubuntu)
  - [**Installing in Windows**](#installing-in-windows)
    - [**Chocolatey**](#chocolatey)
    - [**Direct Installation**](#direct-installation)

## **Overview**
Sphinx is coded using Python and is compatible with Python 3.9 and newer versions. It relies on libraries like Docutils and Jinja, both of which are automatically installed with Sphinx.

## **Installing in Linux (Debian/Ubuntu)**
```
apt-get install python3-sphinx
```
If Python is not currently installed, the command above will automatically install it alongside Sphinx

## **Installing in Windows**
Sphinx can be installed with Chocolatey or installed manually.

### **Chocolatey**
  1. Open the Windows PowerShell as administrator

  2. Paste the following command into Powershell and press enter
     ```
     Set-ExecutionPolicy Bypass -Scope Process -Force; `
      iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
     ```

      Output
      ```
      Chocolatey (choco.exe) is now ready.
      You can call choco from anywhere, command line or powershell by typing choco.
      Run choco /? for a list of functions.
      You may need to shut down and restart powershell and/or consoles
      first prior to using choco.
      Ensuring Chocolatey commands are on the path
      Ensuring chocolatey.nupkg is in the lib folder
      ```
  3. Close and reopen an elevated PowerShell window to start using `chocolatey`
  4. Install Sphinx with `chocolatey`
        ```
     choco install sphinx
     ```

      Output
      ```
      Chocolatey v2.2.2
      Installing the following packages:
      sphinx
      By installing, you accept licenses for the packages.
      
      ....
      
      The install of sphinx was successful.
      Software install location not explicitly set, it could be in package or
      default install location of installer.

      Chocolatey installed 14/14 packages.
      See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

      Installed:
      - chocolatey-compatibility.extension v1.0.0
      - chocolatey-core.extension v1.4.0
      - chocolatey-windowsupdate.extension v1.0.5
      - KB2919355 v1.0.20160915
      - KB2919442 v1.0.20160915
      - KB2999226 v1.0.20181019
      - KB3033929 v1.0.5
      - KB3035131 v1.0.3
      - python v3.12.1
      - python3 v3.12.1
      - python312 v3.12.1
      - sphinx v7.2.5
      - vcredist140 v14.38.33130
      - vcredist2015 v14.0.24215.20170201
      ```
  5. Reboot to apply recent package changes
   
### **Direct Installation**

Sphinx can be installed directly from a clone of the Git repository. 

1. Cloning the repository
   ```
   git clone https://github.com/sphinx-doc/sphinx
   ```

    Output
    ```
    Cloning into 'sphinx'...
    remote: Enumerating objects: 161025, done.
    remote: Counting objects: 100% (1221/1221), done.
    remote: Compressing objects: 100% (638/638), done.
    remote: Total 161025 (delta 681), reused 1049 (delta 569), pack-reused 159804Receiving objects:  97% (157732/161025), 80Receiving objects: 100% (161025/161025), 86.71 MiB | 2.36 MiB/s, done.
    Resolving deltas:  91% (107920/11859)
    Resolving deltas: 100% (118592/118592), done.
    Updating files: 100% (1744/1744), done.
    ```

2. Navigate to the sphinx directory
   
   PATH: `sphinx` 
   ```
   cd sphinx
   ```

3. Install sphinx
   ```
   pip install .
   ```

    Output
    ```
        Successfully built Sphinx
    Installing collected packages: Sphinx
        Successfully uninstalled Sphinx-7.2.5
    Successfully installed Sphinx-7.3.0
    ```

