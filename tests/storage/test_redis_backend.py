from site_checker.storage.redis_backend import RedisStorage


def test_get():
    r = RedisStorage()
    val = r.get('val no exists')
    assert val is None


def test_set():
    r = RedisStorage()
    val = {'a': 3}
    r.set('a', val)
    assert r.get('a') == val
