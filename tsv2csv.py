fileName = 'lixo.tsv'
newFileName = fileName[:-3] + 'csv'

with open(fileName, 'r') as f:
    tsvData = f.read()
    
if tsvData.count('\t') > 0:
    csvData = tsvData.replace('\t', ',')
  
with open(newFileName, 'w') as f:
    f.write(csvData)