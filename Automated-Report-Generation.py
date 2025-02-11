import pandas as pd
from fpdf import FPDF

#Reading and printing data from the Mydata txt file.
with open("MyData.txt", "r") as file:
    for data in file:
        print(data.strip())
    
"""
#reading data from the Mydata txt file
data = pd.read_csv("Mydata.txt")

#printing data from Mydata txt file 
print ("\nAll Data from TXT file.\n",data)"""

#Reading data from txt file for analyzing the data.
data = pd.read_csv("MyData.txt")

#Basic analyzation: Total and average of all products.
total = data["Sales"].sum()
avg = data["Sales"].mean()

# Printing basic analyzation
print(f"\nTotal of all product: {total}")
print(f"Average of all product: {avg}\n")

pdf = FPDF()

#Creating New blank page
pdf.add_page()

#Creating First Cell
pdf.set_font("Arial","B",20) #front type and size , b use for Bold text
# 200 for width and 10 is for hight and ln true means move curser to next line
pdf.cell(200, 10,"Report On My Products",ln=True,align="C")

#adding blank space
pdf.cell(200, 10,"",ln=True,align="C")# cell for single line

#Adding Small description to PDF file
pdf.set_font("Arial",size=18) #front type and size
#Using here multi_cell function for paragraph 
pdf.multi_cell(200, 10, "Hi, My name is Yugen May.",align="L")
pdf.multi_cell(200, 10, "I am currently working on a Python projects for my internship.",align="L")
pdf.multi_cell(200, 10, "This project involves reading and analyzing data from a file and generating a report.",align="L")

#adding blank space
pdf.cell(200, 10,"",ln=True,align="C")

#Creating table
pdf.set_fill_color(200, 200, 200)# adding color for product and sales in table
# border is 1 for table, fill is for background color
pdf.cell(100, 10, "Product", border=1, ln=False, align="C", fill=True)
pdf.cell(50, 10, "Sales", border=1, ln=True, align="C", fill=True)

pdf.set_font("Arial", size=12)
for index, row in data.iterrows():#printing all data of product and sales
    pdf.cell(100, 10, row["Product"], border=1, ln=False, align="C")
    pdf.cell(50, 10, str(row["Sales"]), border=1, ln=True, align="C")

#adding blank space
pdf.cell(200, 10,"",ln=True,align="C")
    
#printing total and average of sales
pdf.cell(200, 10, f"Total Sales: {total}", ln=True,align="L")
pdf.cell(200, 10, f"Average Sales: {avg}", ln=True,align="L")

#generating pdf report
pdf.output("report.pdf")

print("PDF Report On My Products is generated successfully...\n")

