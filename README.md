# PyInstallerBuild
## An automatic PyInstaller builder on push to your repository

What is PyInstallerBuild?

**PyInstallerBuild is a GitHub Action that automatically builds your Python project with PyInstaller on push to your repository.**

How does it work?

**PyInstallerBuild uses PyInstaller and the workflow files from github to make automatic builds. Deeper down it uses a comination of a main application file, a spec file, and the workflow to call PyInstaller on a workflow server that makes local builds**

How do I use it in my own repo?

**Take the build.yml file and modify the file names such as app.spec and app.dmg/exe and modify the spec files to fit your own application. Make sure that your application runs with a main file and not as a module**