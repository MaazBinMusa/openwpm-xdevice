import plyvel

db  = plyvel.DB("./leveldb")

hashes = []
with open("../tables/run2/tables/Hashes.txt","r") as file:
	lines = file.readlines()
	for line in lines:
		hashes.append(line.strip('\n').strip('\r'))

for index,item in enumerate(hashes):
	img = db.get(str.encode(item))

	print(str.encode(item))
	#print(img)

	if img == None:
		print("none")
		continue

	with open("../tables/run2/images/{}check.png".format(str(index)),"wb") as file:
		file.write(img)

db.close()