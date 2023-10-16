import os

def test_basic():
    assert not os.system("cd test-data/basic/ && make html SPHINXOPTS=-W")
