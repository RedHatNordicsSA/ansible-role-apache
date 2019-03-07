import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apache_is_installed(host):
    apache = host.package("httpd")
    assert apache.is_installed


def test_apache_running_and_enabled(host):
    apache = host.service("httpd")
    assert apache.is_running
    assert apache.is_enabled


def test_port_80_is_listening(host):
    socket = host.socket("tcp://80")
    assert(socket.is_listening)
