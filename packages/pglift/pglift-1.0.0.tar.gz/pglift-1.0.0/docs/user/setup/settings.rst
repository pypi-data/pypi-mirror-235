.. _settings:

Settings
========

The details of most operations can be configured by defining the *settings* of
an installation. These settings are usually gathered in a configuration file,
in YAML format, and some can be overridden from environment variables.

A typical settings document looks like:

.. literalinclude:: ../../files/example-settings.yaml
   :language: yaml

where it can be seen how PostgreSQL cluster will be configured upon
deployment, and which extra components will be set up and how.

Apart from ``postgresql``, most top-level keys correspond to *satellite
components* of instances and their value thus defines how these components are
installed, configured, run. Some other top-level keys correspond to
cross-service settings defining, e.g., how scheduled tasks are run or which
service manager is used.

Many fields accept a ``null`` value to disable their respective service (e.g.
``scheduler: null``). (In fact, many fields have a default ``null`` value.)
The settings document is merged recursively with default value. In particular,
to enable and use the default configuration for a component, set its value to
an empty object as done for ``powa`` in the example above.

To view current settings, run:

::

    $ pglift site-settings


Site (or installation) settings are looked up for at the following locations:

- ``$XDG_CONFIG_HOME/pglift/settings.yaml`` [#xdgconfighome]_, then,
- ``/etc/pglift/settings.yaml``.

Once one of these files is found, processing stops.

.. _settings-schema:

Settings model
--------------

The complete model of site settings is described by a JSON Schema, which can
be obtained through:

::

    $ pglift site-settings --schema

The model of a specific field, e.g. ``pgbackrest``, is usually defined under
the ``#/definitions`` reference:

::

    $ pglift site-settings --schema -o json | jq .properties.pgbackrest
    {
      "title": "Pgbackrest",
      "env_names": [
        "pgbackrest"
      ],
      "allOf": [
        {
          "$ref": "#/definitions/PgBackRestSettings"
        }
      ]
    }

This reference can be obtained as:

::

    $ pglift site-settings --schema -o json | jq .definitions.PgBackRestSettings
    {
      "title": "PgBackRestSettings",
      "description": "Settings for pgBackRest.",
      "type": "object",
      "properties": {
        "execpath": {
          "title": "Execpath",
          "description": "Path to the pbBackRest executable.",
          "default": "/usr/bin/pgbackrest",
          "format": "file-path",
          "type": "string"
        },
        "configpath": {
          "title": "Configpath",
          "description": "Base path for pgBackRest configuration files.",
          "default": "pgbackrest",
          "type": "string",
          "format": "path"
        },
      ...
      "additionalProperties": false
    }



Environment override
--------------------

To temporarily override installed settings, the ``SETTINGS`` environment
variable can be used. It accepts either a JSON-dumped value or a file path,
prepended with ``@``:

::

    $ SETTINGS='{"prefix": "/srv/pglift"}'
    $ SETTINGS=@/path/to/config.json

To temporarily override one particular settings field, use:

::

    $ POSTGRESQL='{"auth": {"local": "md5"}}'

.. [#xdgconfighome]
   Where ``$XDG_CONFIG_HOME`` would be ``$HOME/.config`` unless configured
   differently.
