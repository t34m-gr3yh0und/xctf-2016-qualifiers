# Invisible

This challenge provides invisble.png and invisible.py.

- invisible.png --> shows a picture of Wonder Woman
- invisible.py --> shows a piece of code regarding the invisible.png

Upon closer inspection of python code, you will see this line
```py
			pix_new[x,y] = (pix_old[x,y][0],pix_old[x,y][1],ord(code[y])^0x13^0x37)
```
what this line does is essentially taking the 3rd part of the pixel and XOR it with 0x13 and then XOR it again with 0x37

And the result will be in integer. So you just need to convert it to a character with
```py
            chr()
```
And the final script will look like this
```py
import Image, zlib, struct, sys


image_test = Image.open("invisble.png")
pix_test = image_test.load()

code = 'THE_SECRET_KEY_FIND_IT' #len 22
for x in range(image_test.size[0]):
	for y in range(image_test.size[1]):
		if x == 0 and y < 50:
			sys.stdout.write(chr(pix_test[x,y][2]^0x13^0x37))

```
which will give you the flag
```
XCTF{Pr1nc3ss_D1ana_0f_Th3my5c1ra}
```
