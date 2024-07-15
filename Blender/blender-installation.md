# Blender Installation

## Table of Contents
- [Blender Installation](#blender-installation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Goals](#goals)
  - [Main References](#main-references)
  - [Prerequisites](#prerequisites)
  - [Requirements \& Compatibility](#requirements--compatibility)
    - [For Windows](#for-windows)
    - [For Linux](#for-linux)
  - [Installation Steps](#installation-steps)
    - [Windows 11 Pro](#windows-11-pro)
    - [Ubuntu 22.04](#ubuntu-2204)
  - [Launching Blender](#launching-blender)
  - [Uninstalling Blender](#uninstalling-blender)
    - [Windows 11 Pro](#windows-11-pro-1)
    - [Ubuntu 22.04](#ubuntu-2204-1)
  - [Conclusion](#conclusion)

## Introduction
Blender is a free and open-source 3D creation suite supporting the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing, and motion tracking, even video editing, and game creation. This document provides a comprehensive guide on installing Blender on Ubuntu 22.04 LTS (Jammy Jellyfish).

## Goals

- To guide users through the installation process of Blender on Ubuntu 22.04 LTS and Windows 11 Pro.
- To provide a clear and concise reference for users new to Blender or Ubuntu.

## Main References

- [Blender Official Website](https://www.blender.org/)
- [Ubuntu Official Documentation](https://ubuntu.com/tutorials)

## Prerequisites
- A system running Ubuntu 22.04
- Sudo privileges
- A Windows 11 Pro operating system.

## Requirements & Compatibility

### For Windows

|  | Minimum | Recommended |
| -------- | -------- | ------- |
| OS | Windows 8.1 (64-bit) | Windows 10 or Windows 11 |
| CPU | 4 cores with SSE4.2 support | 8 cores |
| RAM | 8 GB | 32 GB |
| GPU | 2 GB VRAM with OpenGL 4.3 (see below) | 8 GB VRAM |

**NVIDIA**  : GeForce 400 and newer, Quadro Tesla GPU architecture and newer, including RTX-based cards, with NVIDIA drivers.

**AMD**     : GCN 1st gen and newer.

**Intel**   : Broadwell architecture and newer. Always make sure to install the latest drivers from the graphics card manufacturer website.

### For Linux

|  | Minimum | Recommended |
| -------- | -------- | ------- |
| OS | Distribution with glibc 2.28 or newer (64-bit) |  |
| CPU | 4 cores with SSE4.2 support | 8 cores |
| RAM | 8 GB | 32 GB |
| GPU | 2 GB VRAM with OpenGL 4.3 (see below) | 8 GB VRAM |

**NVIDIA**  : GeForce 400 and newer, Quadro Tesla GPU architecture and newer, including RTX-based cards, with NVIDIA drivers.

**AMD**     : GCN 1st gen and newer.

**Intel**   : Broadwell architecture and newer. Always make sure to install the latest drivers from the graphics card manufacturer website.

## Installation Steps

### Windows 11 Pro

1. **Download Blender**

   Visit the Blender download page and download the Windows installer for Blender version 4.1.1.

2. **Run the Installer**

   Locate the downloaded installer file (e.g., blender-4.1.1-windows64.msi) and double-click to run it.

3. **Setup Wizard - Welcome Page**

   he Setup Wizard will open. Click *Next* to continue.

4. **End User License Agreement (EULA) Page**

   Read the End User License Agreement. Check the box to accept the terms and click *Next* to continue.

5. **Custom Setup**

   In the Custom Setup page, you can select the features you want to install and change the installation location by clicking Browse. After making your selections, click *Next* to proceed.

6. **Ready to Install Blender**

   The wizard is now ready to begin the installation. Click *Install* to start the installation process.

7. **Installing Blender**

   Wait while Blender is being installed. This may take a few minutes.

8. **Completed Installation**

   Once the installation is complete, click the *Finish* button to exit the Setup Wizard.

8. **Verify Installation**

   Open the Control Panel, go to *Programs* &rarr; *Programs and Features*, and search for Blender in the list of installed applications to ensure it is installed. Additionally, you can check the version of Blender by opening the program and navigating to Help -> About.

You can check for the screenshoot page of all of the blender installation on: [Imgur - Blender Installation](https://imgur.com/a/NVxasYo)

### Ubuntu 22.04

1. **Update and Upgrade Ubuntu**: Ensure your system is up-to-date.
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Blender**: You can install Blender directly from the Ubuntu repository.
   ```bash
   sudo apt install blender -y
   ```

3. **Verify Installation**: Check if Blender is successfully installed.
   ```bash
    blender --version
    ```

## Launching Blender

### Ubuntu 22.04

After installation, you can launch Blender by searching for it in your system's application menu or by running the following command in the terminal:
```bash
blender
```

## Uninstalling Blender

### Windows 11 Pro

1. Open the *Control Panel*.
2. Go to *Programs* -> *Programs and Features*.
3. Find Blender in the list of installed applications.
4. Click on Blender and select *Uninstall*.
5. Follow the prompts to complete the uninstallation.

### Ubuntu 22.04

If you need to uninstall Blender, you can do so by running:
```bash
sudo apt remove blender -y
```

## Conclusion

This guide provided you with the steps to install Blender on Ubuntu 22.04 and Windows 11 Pro, ensuring you have the latest version for your creative projects. With Blender installed, you can now explore its vast array of features for 3D modeling, animation, and more.```
