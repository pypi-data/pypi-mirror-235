.. _quickstart:

Quickstart
==========

.. highlight:: console

Let's get started, using the command-line interface:

::

    $ pglift instance create main --port=5433 --surole-password
    Super-user role password:
    Repeat for confirmation:
    INFO     initializing PostgreSQL
    INFO     configuring PostgreSQL
    INFO     configuring PostgreSQL authentication
    INFO     starting PostgreSQL 14/main

This commands simply creates a PostgreSQL cluster, by default with no
satellite components.

We can inspect its logs:

::

    $ pglift instance logs main
    INFO     reading logs of instance 14/main from ~/.local/share/pglift/srv
             /pgsql/14/main/data/log/postgresql-2022-02-14_142151.log
    2022-02-14 14:21:51.629 CET [55556] LOG:  starting PostgreSQL 14.1 (Debian 14.1-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
    2022-02-14 14:21:51.630 CET [55556] LOG:  listening on IPv6 address "::1", port 5433
    2022-02-14 14:21:51.630 CET [55556] LOG:  listening on IPv4 address "127.0.0.1", port 5433
    2022-02-14 14:21:51.632 CET [55556] LOG:  listening on Unix socket "~/.local/share/pglift/run/postgresql/.s.PGSQL.5433"
    2022-02-14 14:21:51.636 CET [55558] LOG:  database system was shut down at 2022-02-14 14:21:51 CET
    2022-02-14 14:21:51.642 CET [55556] LOG:  database system is ready to accept connections

Create some objects:

::

    $ pglift role -i main create dba --validity="2023-01-01T00:00:00" --login --password
    Role password:
    Repeat for confirmation:
    INFO     creating role 'dba'

::

    $ pglift database -i main create myapp --owner=dba
    INFO     creating 'myapp' database on instance 14/main

And eventually drop the instance:

::

    $ pglift instance drop main
    INFO     dropping instance 14/main
    > Confirm complete deletion of instance 14/main? [y/n] (y): y
    INFO     stopping PostgreSQL 14/main
    INFO     deleting PostgreSQL cluster

Now more interestingly, let's add some configuration to pglift by writing the
following file:

.. literalinclude:: files/example-settings.yaml
   :language: yaml
   :caption: File ~/.config/pglift/settings.yaml

in which, we configure PostgreSQL host-based authentication, enable
`pgbackrest` and `prometheus` satellite services and finally activate
`systemd` as service manager and scheduler.

.. note::
    Further operation requires an extra "installation" step, mostly in order to
    prepare the site:

    ::

        $ pglift site-configure install
        INFO     installed pglift-postgres_exporter@.service systemd unit at
                 ~/.local/share/systemd/user/pglift-postgres_exporter@.service
        INFO     installed pglift-backup@.service systemd unit at
                 ~/.local/share/systemd/user/pglift-backup@.service
        INFO     installed pglift-backup@.timer systemd unit at
                 ~/.local/share/systemd/user/pglift-backup@.timer
        INFO     installed pglift-postgresql@.service systemd unit at
                 ~/.local/share/systemd/user/pglift-postgresql@.service
        INFO     installing base pgbackrest configuration
        INFO     creating pgbackrest include directory
        INFO     creating pgbackrest repository path
        INFO     creating common pgbackrest directories
        INFO     creating postgresql log directory

Now let's create again our ``main`` instance:

::

    $ pglift instance create main --port=5433 --surole-password \
        --data-checksums --pgbackrest-stanza=app
    Super-user role password:
    Repeat for confirmation:
    INFO     initializing PostgreSQL
    INFO     configuring PostgreSQL authentication
    INFO     configuring PostgreSQL
    INFO     starting PostgreSQL 14-main
    INFO     creating role 'powa'
    INFO     creating role 'prometheus'
    INFO     creating role 'backup'
    INFO     altering role 'backup'
    INFO     creating 'powa' database in 14/main
    INFO     creating extension 'btree_gist'
    INFO     creating extension 'pg_qualstats'
    INFO     creating extension 'pg_stat_statements'
    INFO     creating extension 'pg_stat_kcache'
    INFO     creating extension 'powa'
    INFO     configuring Prometheus postgres_exporter 14-main
    INFO     configuring pgBackRest stanza 'app' for pg1-path=...
    INFO     creating pgBackRest stanza app
    INFO     starting Prometheus postgres_exporter 14-main

We notice that a `Prometheus postgres_exporter` service and a `pgBackRest`
repository, user and configuration are now set up alongside our PostgreSQL
instance.

As `systemd` was defined as service manager and scheduler, we can see the
following units defined:

::

    $ systemctl --user list-units "pglift-*"
      UNIT                                     LOAD   ACTIVE SUB     DESCRIPTION
      pglift-postgres_exporter@14-main.service loaded active running Prometheus exporter 14-main database server metrics
      pglift-postgresql@14-main.service        loaded active running PostgreSQL 14-main database server
      pglift-backup@14-main.timer              loaded active waiting Backup 14-main PostgreSQL database instance

For more, head out to more in-depth tutorials and user guides.
