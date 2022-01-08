## dhasher
- A python library for password hashing and verification of existing password hashes

### how to use 

1. Install package
 
```
pip install dhasher
 
```
2. import the package 
 
```
from dhasher import myhash
 
```
3. hashing a value
 
```
res=myhash.do_hash("father")
output> '88a1881f0025cf7117501d07aefc5d4be6696656790d765678df8bc48ca52687'
 
```
4. comparing of new value with previously hashed value res
 
```
myhash.verify_hash("father",res)
output> True

myhash.verify_hash("mother",res)
output> False

```




