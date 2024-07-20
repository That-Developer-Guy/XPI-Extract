@echo off
if not exist "C:\Users\%USERNAME%\.xpi-extract" (
    mkdir "C:\Users\%USERNAME%\.xpi-extract"
)
if not exist "C:\Users\%USERNAME%\.xpi-extract\VisualElements_70.ico" (
    copy "%~dp0VisualElements_70.ico" "C:\Users\%USERNAME%\.xpi-extract"
)
assoc .xpi=xpifile
ftype xpifile="C:\Program Files (x86)\XPI Extract\xpi_opener.exe" "%%1" %*
