#requirements - tabula
#pip install tabula-py

import tabula #open source tool
import pandas as pd

file = "pdf_file/PPP_Report.pdf" #pdf file
input_directory = "pdf_files/*.pdf" # if multiple pdf file.

# convert single PDF file into CSV
tabula.convert_into(file, "output.csv", output_format="csv", pages = 'all')
# file saved in csv format as output.csv

# if there are multiple pdf files than convert all PDFs in a directory
tabula.convert_into_by_batch(input_directory, output_format='csv', pages='all)
 

# if there is single page document containing multiple tables else multiple table is set to false
df = tabula. read_pdf(file, multiple_tables=True)
df = tabula.read_pdf(file, pages='all') #Read pdf into list of dataframe                          
type(df) #list
dfs = pd.DataFrame(df) #convert list into dataframe
# Now dataframe can be easily cleanable using pandas
dfs.to_csv("output.csv")  #save dataframe into csv                 
