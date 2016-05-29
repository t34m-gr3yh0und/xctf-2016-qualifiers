# GoGoGo
Writeup by Hank

## Debug gogogo.exe with Immunity Debugger
Find out the portion of code corresponding to the processing of password:
- On the upper left window: Search for > Binary string > ASCII : "Enter your password" -> we find out that this string is stored at address 0x004F5EE0.
- Click to select the line addr 0x004F5EE0: Find references to > Selected address -> the result show that this address is refered to by the instruction at addr 0x004012CD
- Set a breakpoint at addr 0x004012CD and run the program. After the break, step over (F8)
- The program stalls at line 0x004013F5, where we need to key in the password. Set a breakpoint at this addr, key in a password and continue
- At line 0x0040142B, we found a hardcoded ASCII string "5B4E7145766E30747A443E4B5C40165C4F65617458"
We now suspec that this is the password.
It's actually NOT ><
- At line 0x004015EB, it is instructed to jump back to addr 0x00401444, notifying us that there is a loop. Set break at addr 0x004015EB and run the program.
- Now notice on the Stack window at the lower right corner, the hardcoded key is at 0x1144FF20. In addition, while looping, the string stored at addr 0x1144FEFC keeps changing. When the loop finishes, the number of bytes of the string is same as the length of the input password, however, the content is different.
We now suspect that the password has been processed before being compared with the hardcoded key.

## Find the password
We now try to find what processing has been applied to the input password.

Testing with input = "AAAAAAAAA" we see that the ASCII string at 0x1144FEFC is "424C64424C64424C64".
It is easy to notice the pattern in the resultant bytecode where every third byte is the same.
It is therefore suspected that the password has been encrypted using Repeated-XOR with a 3-byte key.
By XORing \x41\x41\x41, which is the bytecode of "AAA", with \x42\x4C\x64, the key is obtained as \x03\x0D\x25.

We can test if it's indeed the case of repeated-XOR encryption by trying different input passwords.

Now that our hypothesis is confirmed, the remaining is to find the password that would yield the ouput matching the hardcoded string. This is done via applying repeated-XOR with the obtained key on the hardcoded string.
The result is:
<FIND IT YOURSELF>


