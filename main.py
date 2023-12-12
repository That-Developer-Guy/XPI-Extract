import pyuac
import os
import getpass
import shutil

file_path = os.getcwd() + "/" + "xpi_opener.exe"
user_path = "C:\\Users\\" + getpass.getuser()
shutil.copy(os.getcwd() + "/VisualElements_70.ico", user_path)

def main():
    os.system("assoc .xpi=xpifile")
    os.system(f'ftype xpifile="{file_path}" "%1" %*')

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()  # Already an admin here.