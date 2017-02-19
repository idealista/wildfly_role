import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]


def test_wildfly_version(File, AnsibleVars):
    version = AnsibleVars["wildfly_version"]
    assert File("/opt/wildfly-" + version).exists
    assert File("/opt/wildfly").is_symlink
    assert File("/opt/wildfly").linked_to == "/opt/wildfly-" + version


def test_wildfly_service(File, Service, Socket, AnsibleVars):
    # port = AnsibleVars["wildfly_port"]
    assert File("/etc/systemd/system/wildfly.service").exists
    assert Service("wildfly").is_enabled
    assert Service("wildfly").is_running
    # assert Socket("tcp://:::" + str(port)).is_listening
