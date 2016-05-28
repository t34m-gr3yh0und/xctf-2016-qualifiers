id = 'admin'
pw = 'NUSGreyhats'
print 'ID: ', id
print 'PW: ', pw
for num in range(0,20) :
	id = base64.b64encode(id)
	pw = base64.b64encode(pw)
print 'ENCODED ID: ', id
print 'ENCODED PW: ', pw