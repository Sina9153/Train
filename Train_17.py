import pyexcel
import os

root_path=os.getcwd()
dest_path=root_path+r"\Test\a.xlsx"

if os.path.exists(dest_path):
    sheet=pyexcel.get_sheet(file_name=dest_path)
    