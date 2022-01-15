import csv

def truncate_file(file):
	with open(file, mode='w') as f:
		f.truncate()
	f.close()

def extrate_data_to_csv(file, data):
    truncate_file(file)
    with open(file, mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())
        for attraction in data:
            writer.writerow(attraction.values())
    f.close()
