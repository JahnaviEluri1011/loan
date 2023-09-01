import openpyxl
from openpyxl.styles import Font



workbook=openpyxl.load_workbook("summary_Book.xlsx")

worksheet = workbook.active

count_array = [27, 16, 56, 41, 61, 23, 16]
subverticals = ["sv1", "sv2", "sv3", "sv4", "sv5", "sv6", "sv7"]


worksheet['A1'] = 'Count'
worksheet['B1'] = 'Subvertical'

for col_letter in ['A', 'B']:
    cell = worksheet[f'{col_letter}1']
    cell.font = Font(bold=True)

row_num = 2
starting_count = 1

for count, subvertical in zip(count_array, subverticals):
    for i in range(count):
        worksheet[f'A{row_num}'] = starting_count
        worksheet[f'B{row_num}'] = subvertical
        row_num += 1
        starting_count += 1

workbook.save("summary_Book.xlsx")

workbook.close()

