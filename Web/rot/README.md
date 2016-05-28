# rot

As you enter the website, you will see the link, index.phps, which will lead you to the source code of the php

Upon closer inspection of the source code, you will see these 3 parts
```php
    $id_value = $_COOKIE[user];
    $pw_value = $_COOKIE[password];
```
```php
    for($i=0;$i<20;$i++){
        $id_value=base64_decode($id_value);
        $pw_value=base64_decode($pw_value);
    }
```
```php
    if($id_value=="admin" && $pw_value=="NUSGreyhats"){
        success();
    }
```
what this 3 part means is that
1. You need id_value to be admin and pw_value to be NUSGreyhats
2. id_value and pw_value are decoded 20 times with Base64
3. You can modify id_value and pw_value via cookies

Therefore, what you need to do is to take "admin" and "NUSGreyhats" to be encoded 20 times with Base64. And use those values to modify the cookies.

The code to do this is
```py
id = 'admin'
pw = 'NUSGreyhats'
print 'ID: ', id
print 'PW: ', pw
for num in range(0,20) :
	id = base64.b64encode(id)
	pw = base64.b64encode(pw)
print 'ENCODED ID: ', id
print 'ENCODED PW: ', pw
```

After you modified and submitted the cookies, you will get the flag
```
XCTF{Haha_this_has_nothing_2_do_with_tor}
```
