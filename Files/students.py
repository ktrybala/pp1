import csv

with open("students.txt", "r") as csvfile:
	csv_reader = csv.reader(csvfile)

	next(csv_reader)

	with open("new_students.txt", "w") as f:
		csv_writer = csv.writer(f, delimiter = '\t')

		for line in csv_reader:
			csv_writer.writerow(line)

		content = csv.reader(f)

print(content)
