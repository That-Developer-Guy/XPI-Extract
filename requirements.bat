@echo off
assoc .xpi=xpifile
ftype xpifile="C:\Program Files (x86)\XPI Extract\xpi_opener.exe" "%%1" %*