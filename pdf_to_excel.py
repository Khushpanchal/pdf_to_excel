#requirements - tabula
#pip install tabula-py

import tabula

file = "pdf_file/PPP_Report.pdf" 

# convert PDF into CSV
tabula.convert_into(file, "output.csv", output_format="csv", pages = 'all')
# file saved in csv format as output.csv

