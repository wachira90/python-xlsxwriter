# import xlsxwriter module
import xlsxwriter
  
workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()
  
# Start from the first cell.
# Rows and columns are zero indexed.
row = 0
column = 0
  
content = ["ankit", "rahul", "priya", "harshita",
                    "sumit", "neeraj", "shivam"]
  
# iterating through content list
for item in content :
  
    # write operation perform
    worksheet.write(row, column, item)
  
    # incrementing the value of row by one
    # with each iteratons.
    row += 1
      
workbook.close()
