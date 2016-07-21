import ConiteDB
import pytest


def test_db_connection_ok():
    """ Basic test to make sure we can connect to mongodb """
    c = ConiteDB.ConiteDB()
    server_info = c.conn.server_info()
    assert server_info['ok'] == 1.0


@pytest.mark.parametrize("cinames,updates", [
    (["test_conitedb_add"], {'foo': 'bar'})
])
def test_conitedb_add(cinames, updates):
    """ Adds should always work! """
    c = ConiteDB.ConiteDB()
    c.add(cinames, updates)
    results = c.desc(cinames)
    for ciname in cinames:
        assert ciname in results
        for update_key, update_value in updates.items():
            assert results.get(ciname, {}).get(update_key) == update_value
