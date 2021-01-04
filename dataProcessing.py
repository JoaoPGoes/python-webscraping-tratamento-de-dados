from tabula import read_pdf
import pandas as pd 

def processing(fileName):
  file_path = ('./' +fileName)

  archive = read_pdf(
    file_path,
    pages=['78-85'],
    multiple_tables=True
  )

  df = pd.DataFrame(archive)
  csvFile = 'DadosProcessados.csv'
  df.to_csv(csvFile)
  return csvFile