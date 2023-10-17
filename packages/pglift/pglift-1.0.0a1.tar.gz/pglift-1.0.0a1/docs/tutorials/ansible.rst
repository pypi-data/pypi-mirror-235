.. _tutorial_ansible:

Using ``dalibo.pglift`` Ansible collection
==========================================

.. highlight:: console

This tutorial illustrates the use of the `dalibo.pglift`_ collection
that leverages pglift with Ansible. The collection ships the following
modules: ``dalibo.pglift.instance``, ``dalibo.pglift.database``,
``dalibo.pglift.role``, ``dalibo.pglift.postgres_exporter`` and
``dalibo.pglift.dsn_info``. This tutorial also demonstrates how to integrate
these modules with other PostgreSQL-related community modules, namely
`community.postgresql`_.

.. _`dalibo.pglift`: https://galaxy.ansible.com/dalibo/pglift

.. note::
   Ansible modules require Python 3 so, depending on the Ansible version being
   used, one may need to configure managed machines to use Python 3 through
   the ``ansible_python_interpreter`` inventory variable or ``-e``
   command-line option.

Setup
-----

In the following we consider two nodes (or machines): the ``control`` node,
where Ansible commands or playbooks will be executed and, the ``managed`` node
where operations should apply.

On the ``control`` node, the collection should be installed:
::

    user@control:~$ ansible-galaxy collection install dalibo.pglift

Documentation for each module can be obtained by using ``ansible-doc
<modulename>``, e.g.:
::

    user@control:~$ ansible-doc dalibo.pglift.instance
    > DALIBO.PGLIFT.INSTANCE
    (.../ansible/ansible_collections/dalibo/pglift/plugins/modules/instance.py)

    Manage a PostgreSQL server instance

    OPTIONS (= is mandatory):

    [...]

On the ``managed`` node, pglift needs to be :ref:`installed <install>` and
:ref:`configured <settings>`. Let's detail a bit how to configure a pglift
site with Ansible. We'll use the following playbook:

.. literalinclude:: ../ansible/site-configure.yml
    :language: yaml
    :caption: site-configure.yml

which:

1. creates a writable (temporary) directory to host PostgreSQL instances,
2. installs pglift site settings based on the following template:

    .. literalinclude:: ../ansible/tutorial-settings.yaml.j2
        :language: yaml
        :caption: tutorial-settings.yml

3. and finally perform site configuration.

Our site settings make use of the temporary directory created in the first
task. The site is configured to use *pgbackrest* for physical backups (stored
locally) and *Prometheus postgres_exporter* for monitoring. Finally note that
we are using a PostgreSQL passfile in order to store passwords for managed
roles.

Executing this playbook will complete the setup of the managed node:
::

    user@control:~$ ansible-playbook site-configure.yml

.. note::
   The ``hosts`` field in this playbook uses ``localhost`` for testing purpose
   and should be adapted to actual ``managed`` node.


Back on the ``control`` node, we will define passwords for the `postgres` user
and other roles used in the following playbooks; these will be stored and
encrypted with Ansible vault:

::

    user@control:~$ cat << EOF | ansible-vault encrypt > pglift-vars
    postgresql_surole_password: $(openssl rand -base64 9)
    prod_bob_password: $(openssl rand -base64 9)
    backup_role_password: $(openssl rand -base64 9)
    prometheus_role_password: $(openssl rand -base64 9)
    EOF


To view actual passwords:

::

    user@control:~$ ansible-vault view pglift-vars

Initial deployment
------------------

The following playbook installs and configures 3 PostgreSQL instances on the
``managed`` node; the first two instances are *started* while the third one is
not:

.. literalinclude:: ../ansible/instances-create.yml
    :language: yaml
    :caption: instances-create.yml

Finally, run:

::

    user@control:~$ ansible-playbook --extra-vars @pglift-vars --ask-vault-password instances-create.yml
    PLAY [my postgresql instances] ***************************************************************************

    TASK [Gathering Facts] ***********************************************************************************
    ok: [localhost]

    TASK [production instance] *******************************************************************************
    changed: [localhost]

    TASK [pre-production instance] ***************************************************************************
    changed: [localhost]

    TASK [dev instance, not running at the moment] ***********************************************************
    changed: [localhost]

    PLAY RECAP ***********************************************************************************************
    localhost                  : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

We can see our instances installed and running on the ``managed`` node:

::

    user@managed:~$ tree -L 3 $tmpdir/srv/pgsql
    /tmp/.../srv/pgsql
    └── 16
        ├── dev
        │   ├── data
        │   └── wal
        ├── preprod
        │   ├── data
        │   └── wal
        └── prod
            ├── data
            └── wal
    user@managed:~$ ps xf
      [...]
      19777 ?        Ss     0:00  \_ /usr/lib/postgresql/16/bin/postgres -D .../srv/pgsql/16/pr
      19780 ?        Ss     0:00  |   \_ postgres: prod: logger
      19781 ?        Ss     0:00  |   \_ postgres: prod: checkpointer
      19782 ?        Ss     0:00  |   \_ postgres: prod: background writer
      19784 ?        Ss     0:00  |   \_ postgres: prod: walwriter
      19785 ?        Ss     0:00  |   \_ postgres: prod: autovacuum launcher
      19786 ?        Ss     0:00  |   \_ postgres: prod: archiver last was 000000010000000000000001
      19787 ?        Ss     0:00  |   \_ postgres: prod: logical replication launcher
      19843 ?        Ssl    0:00  \_ /usr/bin/prometheus-postgres-exporter --log.level=info
      20180 ?        Ss     0:00  \_ /usr/lib/postgresql/16/bin/postgres -D .../srv/pgsql/16/pr
      20183 ?        Ss     0:00  |   \_ postgres: preprod: logger
      20184 ?        Ss     0:00  |   \_ postgres: preprod: checkpointer
      20185 ?        Ss     0:00  |   \_ postgres: preprod: background writer
      20187 ?        Ss     0:00  |   \_ postgres: preprod: walwriter
      20188 ?        Ss     0:00  |   \_ postgres: preprod: autovacuum launcher
      20189 ?        Ss     0:00  |   \_ postgres: preprod: archiver last was 000000010000000000000001
      20190 ?        Ss     0:00  |   \_ postgres: preprod: logical replication launcher
      20246 ?        Ssl    0:00  \_ /usr/bin/prometheus-postgres-exporter --log.level=info


pgBackRest is set up and initialized for started instances:

::

    user@managed:~$ tree -L 2  $tmpdir/backups/backup
    /tmp/.../backups/backup
    ├── stanza_dev
    │   ├── backup.info
    │   └── backup.info.copy
    └── stanza_prod
        ├── backup.info
        └── backup.info.copy

And a systemd timer has been added for our instances:
::

    user@managed:~$ systemctl --user list-timers
    NEXT                          LEFT    LAST PASSED UNIT                               ACTIVATES
    Sat 2023-09-30 00:00:00 CEST  7h left n/a  n/a    postgresql-backup@16-preprod.timer postgresql-backup@13-preprod.service
    Sat 2023-00-30 00:00:00 CEST  7h left n/a  n/a    postgresql-backup@16-prod.timer    postgresql-backup@13-prod.service

    2 timers listed.

Instances update
----------------

In the following version of our previous playbook, we are dropping the "preprod"
instance and set the "dev" one to be ``started`` while changing its
configuration a bit.

We also remove the `pg_stat_statements` from the `shared_preload_libraries`
in the prod instance. For this to be taken into account, the instance needs to
be restarted, hence the addition of `restart_on_changes`:

.. literalinclude:: ../ansible/instances-update.yml
    :language: yaml
    :caption: instances-update.yml

As you can see you can feed third-party ansible modules (like
``community.postgresql``) with libpq environment variables obtained by
``dalibo.pglift.instance`` or ``dalibo.pglift.dsn_info``.

::

    user@control:~$ ansible-playbook --extra-vars @pglift-vars --ask-vault-password instances-update.yml
    PLAY [my postgresql instances] ***************************************************************************

    ...

    PLAY RECAP ***********************************************************************************************
    localhost                  : ok=7    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

::

    user@managed:~$ tree -L 2 $tmpdir/srv/pgsql
    /tmp/.../srv/pgsql
    └── 16
        ├── dev
        ├── preprod
        └── prod


Cleanup
-------

Finally, in this last playbook, we drop all our instances:

.. literalinclude:: ../ansible/instances-delete.yml
    :language: yaml
    :caption: instances-delete.yml

::

    user@control:~$ ansible-playbook --extra-vars @pglift-vars --ask-vault-password instances-delete.yml
    PLAY [my postgresql instances] ***************************************************************************

    ...

    PLAY RECAP ***********************************************************************************************
    localhost                  : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

.. _`community.postgresql`: https://galaxy.ansible.com/community/postgresql
