# XPI Extract 
 
This is a simple program that allows you to extract .xpi files. 
 
## Usage 
 
To use this program, simply open an .xpi file and click on "Extract" in the window. You can edit the path where the extracted files will be saved. Alternatively, you can run the application and select an .xpi file from the File Dialog. 
 
## Installation 
 
To install, download the Installer file from the releases and execute it. Make sure to leave the options at their default settings, as changing them may cause issues. 
 
## Building 
 
If you wish to build this from the source code, you have two options: 
 
1. Edit the  install_script.iss  file to match the file paths and create an executable from  xpi_opener.pyw  using Nuitka: 
   -  python -m pip install nuitka  
   -  nuitka --onefile --enable-plugin=tk-inter --windows-console-mode=disable --windows-icon-from-ico=VisualElements_70.ico xpi_opener.pyw  
   - Additionally, download [Inno Download Plugin](https://drive.google.com/drive/folders/0Bzw1xBVt0mokSXZrUEFIanV4azA?usp=sharing#list) and install it alongside [Inno Setup Compiler](https://jrsoftware.org/isdl.php). 
 
2. Build it entirely from source by executing the following commands in an admin command prompt (with the source code and the directory set to the directory with the source code): 
   -  mkdir C:\Users\%USERNAME%\.xpi-extract  
   -  copy VisualElements_70.ico C:\Users\%USERNAME%\.xpi-extract  
   -  python -m pip install nuitka  
   -  nuitka --onefile --enable-plugin=tk-inter --windows-console-mode=disable --windows-icon-from-ico=VisualElements_70.ico xpi_opener.pyw  
   -  assoc .xpi=xpifile  
   -  ftype xpifile="path/to/xpi_opener.exe" "%%1" %*  
