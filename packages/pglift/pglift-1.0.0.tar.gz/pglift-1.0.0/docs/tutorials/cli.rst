Using the Command Line Interface
================================

.. highlight:: console

This tutorial illustrates how to use the command-line interface (CLI) of
pglift. pglift provides a CLI that can be used as follows:

::

    $ pglift --help
    Usage: pglift [OPTIONS] COMMAND [ARGS]...

    Deploy production-ready instances of PostgreSQL

    Options:
      ...

    Commands:
      ...

There are several entry points corresponding to main objects handled by
pglift: instances, roles, databases, pgconf, etc. Each entry point has its own help:

::

    $ pglift instance create --help
    Usage: pglift instance create [OPTIONS] NAME

      Initialize a PostgreSQL instance

    Options:
      --version VERSION            Postgresql version.
      --port PORT                  Tcp port the postgresql instance will be
                                   listening to.
      ...
      --help                       Show this message and exit.

Most top-level commands like ``database`` or ``role`` operate on a particular
instance which needs to be specified through ``-i``/``--instance`` option;
the option is *required* unless there is only one existing instance.

Site configuration
------------------

Before actually using pglift to manage PostgreSQL instances, it is often
needed to configure the *site* (i.e. the target machine). The main
documentation includes a :ref:`detailed chapter <site-configuration>` on the
topic. For the purpose of this tutorial, we'll simply define so-called
:ref:`site-settings <settings>` to declare the use of two satellite components
*pgBackRest* for physical backup and *Prometheus postgres_exporter*:

.. code-block:: yaml
   :caption: File ~/.config/pglift/settings.yaml

    prefix: /srv/pglift
    pgbackrest:
      repository:
        mode: path
        path: /srv/pglift/backups
    prometheus:
      execpath: /usr/bin/prometheus-postgres-exporter

Also note the ``prefix`` field, which defines a global *prefix* under which
all configuration and data files will be installed (unless specified
otherwise).

With that in place, the site can be configured by running:

::

    $ pglift site-configure install
    INFO     installing base pgbackrest configuration
    INFO     creating pgbackrest include directory
    INFO     creating pgbackrest repository path
    INFO     creating common pgbackrest directories
    INFO     creating postgresql log directory


Creating an instance
--------------------

::

    $ pglift instance create app --pgbackrest-stanza=app
    INFO     initializing PostgreSQL
    INFO     configuring PostgreSQL authentication
    INFO     configuring PostgreSQL
    INFO     starting PostgreSQL 16-app
    INFO     creating role 'prometheus'
    INFO     creating role 'backup'
    INFO     altering role 'backup'
    INFO     configuring Prometheus postgres_exporter 16-app
    INFO     configuring pgBackRest stanza 'app' for pg1-path=...
    INFO     creating pgBackRest stanza app
    INFO     starting Prometheus postgres_exporter 16-app

There are many more options to ``instance create`` commands, some built in and
some depending on the activation of satellite components. For example, a
standby instance can also be created by passing the ``--standby-for=<primary
dsn>`` option to ``instance create`` command, see :doc:`/howto/standby-setup`
for dedicated documentation.

The instance actually consists of a PostgreSQL instance with a backup service
(pgbackrest) and a monitoring service (Prometheus postgres_exporter) set up.

Listing instances
-----------------

.. code-block:: none

    $ pglift instance list
    ┏━━━━━━┳━━━━━━━━━┳━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
    ┃ name ┃ version ┃ port ┃ datadir                            ┃ status      ┃
    ┡━━━━━━╇━━━━━━━━━╇━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
    │ app  │ 16      │ 5432 │ /srv/pglift/srv/pgsql/16/app/data  │ running     │
    │ test │ 16      │ 5433 │ /srv/pglift/srv/pgsql/16/test/data │ not_running │
    └──────┴─────────┴──────┴────────────────────────────────────┴─────────────┘


Altering an instance
--------------------

::

    $ pglift instance alter app --port=5456
    INFO     configuring PostgreSQL
    INFO     reconfiguring Prometheus postgres_exporter 16-app
    INFO     restarting Prometheus postgres_exporter 16-app
    INFO     configuring pgBackRest stanza 'app' for pg1-path=...
    > PostgreSQL needs to be restarted; restart now? [y/n] (n): y
    INFO     restarting PostgreSQL
    INFO     stopping PostgreSQL 16-app
    INFO     starting PostgreSQL 16-app
    INFO     starting Prometheus postgres_exporter 16-app

Getting instance information
----------------------------

::

    $ pglift instance get app
     name  version  port  data_checksums  locale  encoding  pending_restart  pgbackrest   prometheus
     app   16       5456  False           C       UTF8      False            stanza: app  port: 9187

.. note::
   The default output is quite terse but, using the ``-o json`` option to
   ``instance get``, one can get a lot more information.

.. note::

    PostgreSQL instance configuration can be managed using the ``pgconf``
    command, as described in more details in :ref:`the dedicated section
    <pgconf>`. A few quick examples:

    ::

        $ pglift pgconf -i app show log_connections
        # log_connections = off
        $ pglift pgconf -i app set log_connections=on
        INFO     configuring PostgreSQL
        INFO     instance 16/app needs reload due to parameter changes: log_connections
        INFO     reloading PostgreSQL configuration for 16-app
        log_connections: None -> True

Adding and manipulating instance objects
----------------------------------------

::

    $ pglift role -i 16/app create dba --password --login
    Password:
    Repeat for confirmation:
    INFO     creating role 'dba'

::

    $ pglift role -i app get dba -o json
    {
      "name": "dba",
      "has_password": true,
      "inherit": true,
      "login": true,
      "superuser": false,
      "createdb": false,
      "createrole": false,
      "replication": false,
      "connection_limit": null,
      "validity": null,
      "in_roles": [],
      "pgpass": false
    }

::

    $ pglift role -i 16/app alter dba --connection-limit=10 --createdb
    INFO     altering role 'dba'

::

    $ pglift role -i app get dba
     name  has_pas…  inherit  login  superus…  createdb  create…  replica…  connec…  validity  in_rol…  pgpass
     dba   True      True     True   False     True      False    False     10                          False

::

    $ pglift database -i app create myapp

::

    $ pglift database -i app alter myapp --owner dba

::

    $ pglift database -i app get myapp
     name   owner  settings  publications  subscriptions  tablespace
     myapp  dba                                           pg_default

.. code-block:: none

    $ pglift database -i 13/main list
    ┏━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
    ┃ name      ┃ owner    ┃ encoding ┃ collation ┃ ctype ┃ acls        ┃ size   ┃ description  ┃ tablespace  ┃
    ┡━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
    │ myapp     │ dba      │ UTF8     │ C         │ C     │             │ 7.9 MB │              │ name:       │
    │           │          │          │           │       │             │        │              │ pg_default  │
    │           │          │          │           │       │             │        │              │ location:   │
    │           │          │          │           │       │             │        │              │ size: 31.4  │
    │           │          │          │           │       │             │        │              │ MB          │
    │ postgres  │ postgres │ UTF8     │ C         │ C     │             │ 7.8 MB │ default      │ name:       │
    │           │          │          │           │       │             │        │ administrat… │ pg_default  │
    │           │          │          │           │       │             │        │ connection   │ location:   │
    │           │          │          │           │       │             │        │ database     │ size: 31.4  │
    │           │          │          │           │       │             │        │              │ MB          │
    │ template1 │ postgres │ UTF8     │ C         │ C     │ =c/postgre… │ 7.9 MB │ default      │ name:       │
    │           │          │          │           │       │ postgres=C… │        │ template for │ pg_default  │
    │           │          │          │           │       │             │        │ new          │ location:   │
    │           │          │          │           │       │             │        │ databases    │ size: 31.4  │
    │           │          │          │           │       │             │        │              │ MB          │
    └───────────┴──────────┴──────────┴───────────┴───────┴─────────────┴────────┴──────────────┴─────────────┘

::

    $ pglift database -i app drop myapp

::

    $ pglift role -i app drop dba
    INFO     dropping role 'dba'

Dropping a role
~~~~~~~~~~~~~~~

If role is the owner of PostgreSQL objects (e.g. databases, tables, functions, ...)
you will get an error:

::

    $ pglift role -i app drop dba
    INFO     dropping role 'dba'
    Error: role "dba" cannot be dropped because some objects depend on it (detail: owner of database myapp)


You now have two options, delete the owned items:

::

    $ pglift role -i app drop dba --drop-owned
    INFO     dropping role 'dba'

    $ pglift database -i app get myapp
    Error: database 'myapp' not found

or reassign them to a new user:

::

    $ pglift role -i app drop dba --reassign-owned postgres
    INFO     dropping role 'dba'

    $ pglift database -i app get myapp
     name   owner     settings  publications  subscriptions  tablespace
     myapp  postgres                                         pg_default

