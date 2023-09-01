import openpyxl
from openpyxl.styles import Font
import random

workbook = openpyxl.load_workbook("summary_Book.xlsx")
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

random.shuffle(subverticals) #shuffle the subverticles
previous_subvertical = None

for count in count_array:
    for _ in range(count):
        selected_subvertical = subverticals.pop(0)
        random.shuffle(subverticals) 
        subverticals.append(selected_subvertical)  # Move the used subvertical to the end of shuffled subverticles
        worksheet[f'A{row_num}'] = starting_count
        worksheet[f'B{row_num}'] = selected_subvertical
        row_num += 1
        starting_count += 1

workbook.save("summary_Book.xlsx")
workbook.close()
