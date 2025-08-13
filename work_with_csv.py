from pathlib import Path
import csv

folder = Path("/Users/yehor.bulhakov/PycharmProjects/hillel_2025/lesson_13/homework13/13_1_csv")

file1 = folder / "r-m-c.csv"
file2 = folder / "rmc.csv"
result = folder / "result_bulhakov.csv"

rows = []
header = None
seen = set()

for file in (file1, file2):
    with open(file, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        file_header = next(reader)
        if header is None:
            header = file_header
        for row in reader:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                rows.append(row_tuple)

with open(result, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"File saved without duplicates: {result}")