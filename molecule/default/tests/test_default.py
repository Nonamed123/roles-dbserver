import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
MOLECULE_EPHEMERAL_DIRECTORY: /var/folders/wk/cwtmfyx9099gn_g744lt61bh0000gn/T/molecule/ansible-common/default

# check if MongoDB is enabled and running
def test_mongo_running_and_enabled(host):
    mongo = host.service("mongod")
    assert mongo.is_running
    assert mongo.is_enabled

# check if configuration file contains the required line
def test_config_file(File):
    config_file = File('/etc/mongod.conf')
    assert config_file.contains('bindIp: 0.0.0.0')
    assert config_file.exists

#Listening port
# http://testinfra.readthedocs.io/en/latest/modules.html#socket
def test_port(host):
    host.socket("tcp://0.0.0.0:27017").is_listening
    assert host.socket.is_listening
