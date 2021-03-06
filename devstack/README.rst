====================
Enabling in Devstack
====================

**WARNING**: the stack.sh script must be run in a disposable VM that is not
being created automatically, see the README.md file in the "devstack"
repository.  See contrib/vagrant to create a vagrant VM.

1. Download DevStack::

    git clone https://git.openstack.org/openstack-dev/devstack.git
    cd devstack

2. Add this repo as an external repository::

     > cat local.conf
     [[local|localrc]]
     enable_plugin tatu https://github.com/openstack/tatu

3. run ``stack.sh``

Note that Tatu requires Barbican (and optionally Designate and Dragonflow
if you're using the PAT bastions experimental feature).

See the local.conf and local-df.conf examples in this directory.