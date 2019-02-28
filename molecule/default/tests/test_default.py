import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('port', [
    '9200'
])
def test_ports(host, port):
    assert host.socket("tcp://::1:{}".format(port)).is_listening
