# Blender Installation on Ubuntu 22.04

## Table of Contents
- [Blender Installation on Ubuntu 22.04](#blender-installation-on-ubuntu-2204)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Goals](#goals)
  - [Main References](#main-references)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
  - [Uninstalling Blender](#uninstalling-blender)
  - [Conclusion](#conclusion)

## Introduction
Blender is a free and open-source 3D creation suite supporting the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing, and motion tracking, even video editing, and game creation. This document provides a comprehensive guide on installing Blender on Ubuntu 22.04 LTS (Jammy Jellyfish).

## Goals

- To guide users through the installation process of Blender on Ubuntu 22.04 LTS.
- To provide a clear and concise reference for users new to Blender or Ubuntu.

## Main References

- [Blender Official Website](https://www.blender.org/)
- [Ubuntu Official Documentation](https://ubuntu.com/tutorials)

## Prerequisites
- A system running Ubuntu 22.04
- Sudo privileges

## Installation Steps

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

After installation, you can launch Blender by searching for it in your system's application menu or by running the following command in the terminal:
```bash
blender
```

## Uninstalling Blender

If you need to uninstall Blender, you can do so by running:
```bash
sudo apt remove blender -y
```

## Conclusion

This guide provided you with the steps to install Blender on Ubuntu 22.04, ensuring you have the latest version for your creative projects. With Blender installed, you can now explore its vast array of features for 3D modeling, animation, and more. ```


