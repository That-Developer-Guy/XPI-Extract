# XPI Extract

This is a simple program with which you can extract .xpi files.

# Usage

To use this you just have to open an .xpi file and then you click on "Extract" in the window, in which you can edit the path, where it will be saved to. You can also run the application and select an .xpi file from the File-Dialog.

# Installation

Just download the Installer file from the releases and execute it. Make sure to leave the options default because it might not work if you change options.

# Building

If you want to build this from the source code (I do not recommend it), you have two options:

1. Edit the `install_script.iss` file to match the paths of the files and make an executable from the `xpi_opener.pyw` with nuitka:
   - `python -m pip install nuitka`
   - `nuitka --onefile --enable-plugin=tk-inter --windows-console-mode=disable --windows-icon-from-ico=VisualElements_70.ico xpi_opener.pyw`
- You also have to download <a href="https://drive.google.com/drive/folders/0Bzw1xBVt0mokSXZrUEFIanV4azA?usp=sharing#list">Inno Download Plugin</a> and install it alongside <a href="https://jrsoftware.org/isdl.php">Inno Setup Compiler</a>.
2. Build it from source entirely and execute these commands in an admin command prompt:
  - `mkdir C:\Users\%USERNAME%\.xpi-extract`
  - `copy VisualElements_70.ico C:\Users\%USERNAME%\.xpi-extract`
  - `python -m pip install nuitka`
  - `nuitka --onefile --enable-plugin=tk-inter --windows-console-mode=disable --windows-icon-from-ico=VisualElements_70.ico xpi_opener.pyw`
  - `assoc .xpi=xpifile`
  - `ftype xpifile="path/to/xpi_opener.exe" "%%1" %*`
