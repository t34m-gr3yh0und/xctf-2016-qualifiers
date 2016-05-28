import Image, zlib, struct


image_old = Image.open("invisble.png")
pix_old = image_old.load()

image_new = Image.new('RGB',(image_old.size[0],image_old.size[1]),'black')
pix_new = image_new.load()

code = 'THE_SECRET_KEY_FIND_IT'

i=0
for x in range(image_old.size[0]):
	for y in range(image_old.size[1]):
		if x == 0 and y < len(code):
			pix_new[x,y] = (pix_old[x,y][0],pix_old[x,y][1],ord(code[y])^0x13^0x37)
		else:
			pix_new[x,y] = (pix_old[x,y][0],pix_old[x,y][1],pix_old[x,y][2])

image_new.save("invisble_.png")