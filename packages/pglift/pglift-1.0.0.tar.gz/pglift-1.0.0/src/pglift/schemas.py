from __future__ import annotations

import logging

import psycopg.rows
from psycopg import sql

from . import db
from .models import interface

logger = logging.getLogger(__name__)


def ls(cnx: db.Connection) -> list[interface.Schema]:
    """Return list of schemas of database."""
    with cnx.cursor(row_factory=psycopg.rows.class_row(interface.Schema)) as cur:
        cur.execute(db.query("list_schemas"))
        return cur.fetchall()


def current_role(cnx: db.Connection) -> str:
    with cnx.cursor(row_factory=psycopg.rows.args_row(str)) as cur:
        r = cur.execute("SELECT CURRENT_ROLE").fetchone()
        assert r is not None
        return r


def alter_owner(cnx: db.Connection, name: str, owner: str) -> None:
    opts = sql.SQL("OWNER TO {}").format(sql.Identifier(owner))
    logger.info("setting '%s' schema owner to '%s'", name, owner)
    cnx.execute(
        db.query("alter_schema", schema=psycopg.sql.Identifier(name), opts=opts)
    )


def apply(cnx: db.Connection, schema: interface.Schema, dbname: str) -> bool:
    """Apply the state defined by 'schema' in connected database and return
    True if something changed.
    """
    for existing in ls(cnx):
        if schema.name == existing.name:
            if schema.state is interface.PresenceState.absent:
                logger.info("dropping schema %s from database %s", schema.name, dbname)
                cnx.execute(
                    db.query("drop_schema", schema=psycopg.sql.Identifier(schema.name))
                )
                return True

            new_owner = schema.owner or current_role(cnx)
            if new_owner != existing.owner:
                alter_owner(cnx, schema.name, new_owner)
                return True
            return False

    if schema.state is not interface.PresenceState.absent:
        create(cnx, schema, dbname)
        return True
    return False


def create(cnx: db.Connection, schema: interface.Schema, dbname: str) -> None:
    msg, args = "creating schema '%(name)s' in database %(dbname)s", {
        "name": schema.name,
        "dbname": dbname,
    }
    opts = []
    if schema.owner is not None:
        opts.append(sql.SQL("AUTHORIZATION {}").format(sql.Identifier(schema.owner)))
        msg += " with owner '%(owner)s'"
        args["owner"] = schema.owner

    logger.info(msg, args)
    cnx.execute(
        db.query(
            "create_schema",
            schema=psycopg.sql.Identifier(schema.name),
            options=sql.SQL(" ").join(opts),
        )
    )
