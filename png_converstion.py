from PIL import Image

def convertImage():
	img = Image.open("C:/Users/NELSON JOSEPH/Desktop/Nike-Logo.png")
	img = img.convert("RGBA")

	datas = img.getdata()

	newData = []
	
	for item in datas:
		if item[0] == 255 and item[1] == 255 and item[2] == 255 and item[3]== 0:
			newData.append((255, 255, 255, 255))
		else:
			newData.append((item))

	img.putdata(newData)
	img.save("C:/Users/NELSON JOSEPH/Desktop/New1.png", "PNG")
	print("Successful")

convertImage()
