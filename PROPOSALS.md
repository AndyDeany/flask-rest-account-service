# Proposals

* Make code comply with `pylint`.

* Use a database instead of the `ACCOUNTS` list.

* Try using `return {"message": message}, code` instead of `abort(code, message=message)`

* Use `before` hooks to create accounts for tests that need them,
or add a `Given` step to create them.
