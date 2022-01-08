from hashlib import sha256


def do_hash(val):
    res = sha256(val.encode('utf-8')).hexdigest()
    return res


def verify_hash(val1, val2):
    if sha256(val1.encode('utf-8')).hexdigest() == val2:
        return True
    else:
        return False
