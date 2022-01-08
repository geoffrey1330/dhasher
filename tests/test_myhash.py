from dhasher import myhash


def test_hash():
    value = "father"
    assert str(myhash.do_hash(
        value)) == "88a1881f0025cf7117501d07aefc5d4be6696656790d765678df8bc48ca52687"

    result = myhash.do_hash(value)
    assert myhash.verify_hash("father", result) == True

    assert myhash.verify_hash("mother", result) == False
