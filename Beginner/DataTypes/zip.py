import os
import zipfile


with zipfile.ZipFile(os.getcwd() + '/Resource/DummyFile.docx', "r") as zip_ref:
    zip_ref.extractall(os.getcwd() + '/Resource/zipfile/')
