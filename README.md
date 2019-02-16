ansible-role-apache
===========

Very basic role for Installing apache that we use in workshops and demos.

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `ansible-role-apache_var_name` - var\_name description

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: ansible-role-apache-servers
  roles:
    - role: ansible-role-apache
```

License
-------

GPLv3

Author Information
------------------

Author Name <pgustafs@redhat.com>
