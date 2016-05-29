# neutron_star_collision

As you enter the website, you will be able to see the link, index.phps, which will lead you to the source code of index.php

Upon closer inspection of the source code, you will see these 2 parts
```php
$admins = array("rick:db25b8ea97562fdecb013bc197aab2aa",
                "morty:0e046769954751531150123789251246",
                "summer:3233f8995bd41a14635b46531c9b0a6f");
```
```php
    foreach ($admins as &$v) {
        $f = explode(":", $v);
        if ($user == $f[0] && $pass == $f[1]) {
            $auth = true;
        }
    }
```
where can see the md5 hashes and that it is using '==' to compare the hashes

So if you google search, you should be able to find this [website](https://www.whitehatsec.com/blog/magic-hashes/) which gives you a detailed description of the bug and a magic number that you can use for md5 which is
```
240610708
```
and what need to do now is only to enter one of the username and use the magic number as the password and you will be able to see the flag
```
XCTF{Woah_did_u_just_br34k_md5?}
```
