# migcheck example

This repository shows [migcheck](https://github.com/Genetic-Pottery/migcheck)
checking pull requests. migcheck checks that a release's database migrations
don't break the release running in production.

The app is a small Postgres store backend with raw SQL migrations and a
pytest suite. Tag `v1.0.0` stands in for the release running in production.
Each pull request adds a migration, and the
[migcheck workflow](.github/workflows/migcheck.yml) comments with the result.

## The pull requests

| Pull request | Migration | Result |
|---|---|---|
| Rename `users.name` to `full_name` | Renames a column that `v1.0.0` reads and writes. | Fails |
| Require a signup source | Adds a `NOT NULL` column and drops its default, the way Django does. | Fails |
| Add a display name | Adds a nullable column. | Passes |

Each pull request's tests pass. The failures are in `v1.0.0`'s queries
against the new schema: during a rolling deploy, the old release keeps
running after the migration, and its queries fail.

## Run it locally

To run the check on your machine, install
[migcheck](https://github.com/Genetic-Pottery/migcheck#install), then run the
following commands. You need Docker running.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
git fetch origin rename-user-name
migcheck --base v1.0.0 --head origin/rename-user-name \
  --migrate "$PWD/.venv/bin/python migrate.py" \
  --workload "$PWD/.venv/bin/python -m pytest -q"
```

## License

Apache 2.0. See [LICENSE](LICENSE).
