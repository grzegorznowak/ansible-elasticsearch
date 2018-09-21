import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_es_up(host):
    cmd = host.run(
        'curl --write-out %{http_code} --silent ' +
        '--output /dev/null http://localhost:9200')
    assert cmd.stdout == '200'
