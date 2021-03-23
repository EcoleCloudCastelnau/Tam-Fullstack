from fixtures import client


def test_index(client):
  """Start with a blank database."""

  rv = client.get('/')
  assert b'Next Departure' in rv.data
  assert b'Stations List' in rv.data
