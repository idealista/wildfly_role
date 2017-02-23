import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]


def test_wildfly_version(File, AnsibleVars, AnsibleDefaults):
    version = AnsibleVars["wildfly_version"]
    install_path = AnsibleDefaults["wildfly_install_path"]
    assert File(install_path + "/wildfly-" + version).exists
    assert File(install_path + "/wildfly").is_symlink
    assert File(install_path + "/wildfly").linked_to == install_path + "/wildfly-" + version


def test_wildfly_service(File, Service, Socket, AnsibleDefaults):
    assert File("/lib/systemd/system/wildfly.service").exists
    assert Service("wildfly").is_enabled
    assert Service("wildfly").is_running
    assert Socket("tcp://" + AnsibleDefaults["wildfly_bind"] + ":8080").is_listening


def test_wildfly_user_creation(User, Group, AnsibleVars):
    user = AnsibleVars["wildfly_user"]
    assert User(user).exists
    assert Group(AnsibleVars["wildfly_group"]).exists
    assert User(user).home == AnsibleVars["wildfly_user_home"]
    assert User(user).shell == AnsibleVars["wildfly_user_shell"]
    assert User(user).uid == AnsibleVars["wildfly_user_uid"]
