Site settings and user input
============================

The way some operations are performed by pglift usually depends on two things:

- user input, i.e. command-line options or declared fields in Ansible tasks,
  and,
- site settings.

In general, each piece of data is either defined in one of these *source*,
not both in most cases [#except-pg-auth]_, though when something can be defined in
both sources, the user input takes precedence.

The general rule for determining which data source is used is that whatever
concerns all instances on *site* should be defined in site settings whereas
what concerns only a single instance comes from user input. For example, the
name of the super-user role is defined in site settings, whereas its password
comes from user input. Likewise, for components running an HTTP server (e.g.
Patroni or temboard-agent), the server TLS certificates are defined in site
settings, assuming all instances would share the same PKI. Another example is
components that need to communicate with an external service (e.g. the
pgBackRest repository, or Etcd for Patroni): respective data belongs to site
settings as those services are assumed to be shared by all instances on site.

.. [#except-pg-auth]
   One exception is PostgreSQL authentication methods, available
   through ``postgresql.auth.*`` in site settings or ``--auth-*`` in the CLI
   or ``auth.*`` fields in the ``instance`` Ansible module.

