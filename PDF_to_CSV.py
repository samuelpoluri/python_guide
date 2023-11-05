# PDF to CSV

# import tabula module
import tabula

# input file path
inp = r"/Users/samuelpoluri/Desktop/4629XXXXXXXX0008_160635_Retail_Platinum_N copy.pdf"
# output file path
oup = r"/Users/samuelpoluri/Desktop/converted.csv"

# analysing the PDF file
df = tabula.read_pdf(input_path=inp, pages='all')

# converting the PDF file into CSV file
tabula.convert_into(input_path=inp, output_path=oup, output_format="csv", pages='all', stream=True)
