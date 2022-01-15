import csv


def truncate_file(file):
    with open(file, mode='w') as f:
        f.truncate()
    f.close()


def extrate_data_to_csv(file, data):
    truncate_file(file)
    data = extrate_data(data)
    with open(file, mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())
        for attraction in data:
            writer.writerow(attraction.values())
    f.close()

def extrate_address(address):
	valid_address = [
		'中正區',
		'萬華區',
		'中山區',
		'大同區',
		'大安區',
		'松山區',
		'信義區',
		'士林區',
		'文山區',
		'北投區',
		'內湖區',
		'南港區'
		]
	address = address[5:8]
	return address if address in valid_address else None

def extrate_jpg_url(url):
	return url[0:url.index("https://", 10)]

def extrate_data(_data):
    cols = [{'stitle': '景點名稱',
            'address': '區域',
             'longitude': '經度',
              'latitude': '緯度',
              'file': '第一張圖檔網址'
             }]

    extrate_data_arr = []

    for data in _data:
        extrate_data_arr.append(dict(
            (cols[0][key] if key in cols[0].keys() else None,
             value if key in cols[0].keys() else None)
            for (key, value) in data.items()))

    for data in extrate_data_arr:
        del data[None]

    for data in extrate_data_arr:
        data['區域'] = extrate_address(data['區域'])

    for data in extrate_data_arr:
        data['第一張圖檔網址'] = extrate_jpg_url(data['第一張圖檔網址'])

    return extrate_data_arr
