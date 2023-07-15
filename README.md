# PyInstallerBuild
## Create Python Application Bundles with Python

### What is PyInstallerBuild?

PyInstallerBuild is an example repo that shows how's Linux, Windows, and MacOS application bundles can be created with the tool PyInstaller.

### How does it work?

The repo relies on GitHub Actions to call PyInstaller on the spec file which gives PyInstaller the information on how to create the bundle (entry file, necessary files, hard to find imports, etc). After grasping the necessary information PyInstaller creates the executable and bundles it per system to then upload it on the releases page.

### How do I use it in my own repo?

Take a few minutes to look at each file and the PyInstaller documentation to better understand how the system works and then replace pieces one by one. make sure to modify items as necessary as it might not work perfectly at first.
