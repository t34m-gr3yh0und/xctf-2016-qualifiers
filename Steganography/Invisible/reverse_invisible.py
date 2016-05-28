import Image, zlib, struct, sys


image_test = Image.open("invisble.png")
pix_test = image_test.load()

code = 'THE_SECRET_KEY_FIND_IT' #len 22
for x in range(image_test.size[0]):
	for y in range(image_test.size[1]):
		if x == 0 and y < 50:
			sys.stdout.write(chr(pix_test[x,y][2]^0x13^0x37))


#i=0
#for x in range(image_old.size[0]):
#	for y in range(image_old.size[1]):
#		if x == 0 and y < len(code):
#			pix_new[x,y] = (pix_old[x,y][0],pix_old[x,y][1],ord(code[y])^0x13^0x37)
#		else:
#			pix_new[x,y] = (pix_old[x,y][0],pix_old[x,y][1],pix_old[x,y][2])
#
#image_new.save("invisble_.png")