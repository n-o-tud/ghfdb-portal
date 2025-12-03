## Quick orientation

- Codebase: Django (5.x) web portal built on top of the FairDM ecosystem. Primary app code lives under `project/` (notably `project/heat_flow`, `project/ghfdb`, `project/review`). API surfaces for the lightweight API are in `api/` (see `api/api/settings.py`).
- Packaging: Poetry (`pyproject.toml`) targeting Python >=3.11. Several dependencies are pulled from Git (fairdm/\*). Expect network access during install.

## Where to look first (high-value files)

- `config/settings.py` — main production settings and FairDM configuration.
- `pyproject.toml` — package list (add new app packages here), linters, pytest config.
- `project/ghfdb/` — GHFDB-specific logic (models, views, import/export resources, file-serving examples).
- `api/ghfdb/` — minimal DRF examples used by the small API (see `models.py`, `serializers.py`, `views.py`, `urls.py`).
- `tasks.py` — developer tasks (install, test, docs, release, update_deps, build_image).

## Core architecture & patterns (concise)

- FairDM-first: FairDM provides UI/layout/plugins and dataset lifecycle. Code augments FairDM via plugin registration (look for `plugins.dataset.register()` / `unregister()` in `project/*/views.py`).
- Proxy-model pattern: `project/ghfdb/models.py` uses proxy/derived patterns (do not duplicate upstream `heat_flow` domain logic — prefer proxying/filtering).
- DRF + drf-spectacular: API endpoints use ViewSets and `extend_schema` for OpenAPI docs (see `api/ghfdb/views.py` and `api/ghfdb/serializers.py`). Geo endpoints use `GeoFeatureModelSerializer` (for geo JSON).
- PostGIS DB: default API settings point to a PostGIS backend (see `api/api/settings.py`). Tests/CI may use sqlite or dockerized Postgres depending on environment.

## Developer workflows & exact commands

- Install deps (Poetry):

  poetry install

- Dev setup (one-time):

  python manage.py setup

- Run dev server:

  python manage.py runserver

- Run tests (project uses pytest config in `pyproject.toml`):

  poetry run pytest -q

- Build docs (live):

  invoke docs --live

- Common invoke tasks (see `tasks.py`):

  invoke install # poetry install + pre-commit
  invoke test # runs pytest (or tox if requested)
  invoke build_image # builds Docker image locally

- Docker/compose: production compose expects an external `traefik` network and uses `ghcr.io/ihfc-iugg/ghfdb-portal:latest`. For local reproduction use `docker-compose.yml` and provide a `.env`/`stack.env`.

## How to extend the API or add features (practical examples)

- Add a new dataset API: copy the pattern in `api/ghfdb/views.py` — implement a ViewSet, reuse `serializers.py` conventions, and register via a router in `api/ghfdb/urls.py`.
- Geo data: use `rest_framework_gis.serializers.GeoFeatureModelSerializer` and set `geo_field` in the serializer (see `api/ghfdb/serializers.py`).
- OpenAPI: annotate endpoints with `@extend_schema`/`extend_schema_serializer` to keep schema docs consistent with drf-spectacular.
- File downloads: follow `GHFDBPathDownloadView` pattern in `project/ghfdb/views.py` (uses `django_downloadview.PathDownloadView` + `django.contrib.staticfiles.finders.find`).

## Project-specific conventions & gotchas

- App registration: When adding an app under `project/` you must add an entry to `pyproject.toml` `packages` so Poetry includes it.
- FairDM plugins: many behaviors are overridden via `plugins.dataset.register()` — search `plugins.dataset` to find extension points.
- Offline installs will fail: many `pyproject.toml` deps point to Git repositories (fairdm/\*). Tests and `poetry install` require network access.
- Migrations: maintainers sometimes remove or adjust migrations for `heat_flow` to align with upstream; read `README.md` notes before running `makemigrations` in production-like workflows.

## CI / build notes

- Dockerfile uses Poetry bundle and a FairDM base image (`ghcr.io/fair-dm/fairdm:latest`). Image build/publish is configured in `.github/workflows/docker-build-and-publish.yml`.

## Quick references (paths)

- Project settings: `config/settings.py`
- API settings: `api/api/settings.py`
- GHDFB app examples: `project/ghfdb/` and `api/ghfdb/`
- Dev tasks: `tasks.py` (invoke)
- Packaging & lint/test config: `pyproject.toml`

If anything above is unclear or you want the file to include extra rules (for reviewers, emoji style, or stricter code-gen guardrails), tell me which area to expand and I will refine the instructions.

## quick orientation

- This is a Django (5.x) + FairDM-based portal for the Global Heat Flow Database. The code lives under `project/` with three main app groups you should know: `heat_flow`, `ghfdb`, and `review` (see `pyproject.toml` packages and `config/settings.py` where `fairdm.setup` registers apps).
- The project is managed with Poetry (`pyproject.toml`) and targets Python >=3.11. Many dependencies are installed from git repos (fairdm, fairdm-geo, fairdm-rest-api, etc.), so installs require network access.

## key entry points (where to look first)

- `config/settings.py` — main Django configuration and FairDM setup (S3 settings, languages, FAIRDM UI config).
- `manage.py` — custom commands (run `python manage.py setup` before first run as noted in README).
- `project/ghfdb/` — GHFDB-specific logic:
  - `models.py` — `GHFDB` is a proxy of `heat_flow.HeatFlow` and uses a custom `GHFDBManager` to filter records.
  - `views.py` — examples of FairDM plugin usage, DRF endpoints, import/export flows (see `GHFDBMetaDataAPIView`, `GHFDBImport`, `GHFDBExport`). Note the `data_dir = project/ghfdb/data` and file-serving patterns.
  - `resources.py` — (import/export resource definitions) — used by import/export views.
  - `urls.py` — mounts API endpoints like `/api/ghfdb/` and `/api/ghfdb/meta/`.

## project architecture & conventions (concise)

- FairDM-first: much UI and dataset lifecycle logic comes from FairDM (plugins, registry, DataImportView/DataExportView). When adding features search for `plugins.` or `registry.get_model(...)`.
- App layout: apps are under `project/`; add new app entries via `pyproject.toml` packages and register them in FairDM if needed.
- Proxy-model pattern: `GHFDB` proxies `heat_flow.HeatFlow` (see `project/ghfdb/models.py`) — prefer proxying to duplicating domain logic for derived views/filters.
- Plugin pattern: views frequently use `plugins.dataset.register()` / `unregister()` — use that to override FairDM behavior (see `project/ghfdb/views.py`).
- API and schema: DRF + drf-spectacular are used. Use `extend_schema` / `extend_schema_serializer` for endpoint docs (see `project/ghfdb/views.py` and `serializers.py`).

## local dev, docs, and tests — commands you'll use

- Create env & install deps: use Poetry (network required for git deps):
  - `poetry install` (or `poetry shell` + `poetry install`).
- Run initial project setup: `python manage.py setup` (README notes cleaning migrations for `heat_flow` before running this in some workflows).
- Run dev server: `python manage.py runserver`.
- Run docs (live): `poetry shell` then `invoke docs --live` (see README).
- Run tests: `pytest` (pyproject config sets `DJANGO_SETTINGS_MODULE=config.settings` and `pythonpath=project`). Example: `poetry run pytest -q`.
- Lint & format: ruff is configured in `pyproject.toml`; templates use `djlint` (also configured). Run the tools via your preferred wrapper (poetry run or in a dev container).

## CI / build notes

- The repo includes a Dockerfile and `docker-compose.yml` and a GitHub Actions workflow for docker build/publish (see `.github/workflows/docker-build-and-publish.yml` in CI). If reproducing CI locally use Docker.

## developer patterns & gotchas (do not miss)

- Many dependencies are pulled from Git repos (fairdm family). Tests or `poetry install` will fail offline.
- Templates and UI rely heavily on FairDM layout components and plugin config (`fairdm.layouts.ApplicationLayout`, `FAIRDM_CONFIG` in settings). Changing templates may require reading FairDM docs.
- Some migrations may intentionally be omitted for upstream `fairdm` packages; `config/settings.py` contains an instruction (in `DJANGO_SETUP_TOOLS`) to run `makemigrations` during staging.
- The README contains unresolved merge markers — be cautious when copying from it.

## small examples you can follow

- Serve a static CSV download via a view: `GHFDBPathDownloadView` uses `django_downloadview.PathDownloadView` and `finders.find('ghfdb/IHFC_2024_GHFDB.csv')` (see `project/ghfdb/views.py`).
- Add a documented DRF endpoint: copy the `GHFDBMetaDataAPIView` pattern (use `extend_schema` and return `Response(data)` with appropriate status codes).
- Override FairDM plugin: use `plugins.dataset.unregister(SomeView)` then `@plugins.dataset.register()` a subclass (see how `GetPublishedView` overrides `DatasetPublishConfirm`).

## where to look for more context

- `pyproject.toml` — dependency, linter, pytest, and mypy configs.
- `config/settings.py` — S3, languages, FAIRDM UI, and specific deployment hints.
- `project/ghfdb/*` — primary examples of patterns you will implement for dataset import/export and API endpoints.
- `docs/` — narrative docs for project features and mapping of fields.

---

If any of these sections lack the detail you need (for example, a missing custom management command or CI step), tell me what you want me to expand and I will update the file. I can also merge additional guidance if you point me to an existing agent file you'd like preserved.
