import os
import tempfile

import pytest

import castelcloud


@pytest.fixture
def client():
  db_fd, castelcloud.app.config['DATABASE'] = tempfile.mkstemp()
  castelcloud.app.config['TESTING'] = True

  with castelcloud.app.test_client() as client:
    with castelcloud.app.app_context():
      castelcloud.init_db()
    yield client

  os.close(db_fd)
  os.unlink(castelcloud.app.config['DATABASE'])
