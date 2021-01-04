from urllib.request import urlopen
import os.path

def download_file(url):
  response = urlopen(url)
  archiveName = os.path.basename(url)
  with open(archiveName, "wb") as file:
    file.write(response.read())
  return archiveName

def download(url):
  return download_file(url)