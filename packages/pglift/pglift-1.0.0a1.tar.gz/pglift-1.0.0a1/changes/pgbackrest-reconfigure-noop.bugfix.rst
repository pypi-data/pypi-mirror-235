Avoid reconfiguring pgBackRest upon PostgreSQL configuration changes when it's
not needed but only check if respective changes would need a reconfiguration
of this service (e.g. the socket path).
