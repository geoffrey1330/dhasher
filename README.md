## dhasher
- A python library for password hashing and verification of existing password hashes

### how to use 
 
```
### Install package
pip install dhasher==0.1.0

### import the package 

from dhasher import myhash

### hashing a value

res=myhash.do_hash("father")
output> '88a1881f0025cf7117501d07aefc5d4be6696656790d765678df8bc48ca52687'

### comparing of new value with previously hashed value res
myhash.verify_hash("father",res)
output> True

myhash.verify_hash("mother",res)
output> False

```




