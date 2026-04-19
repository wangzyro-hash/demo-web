# demo-web

Minimal Flask app used as the integration target for sandbox v0.3 Phase 1/2.

- `/health` returns 200
- `/error` returns 500 (used to validate negative assertions in `verify`)

Run locally without sandbox:

```
docker compose up --build
curl "http://127.0.0.1:$(docker compose port web 3000 | cut -d: -f2)/health"
```

Registered in sandbox via `~/.sandbox/projects.yaml`:

```yaml
projects:
  demo-web:
    repo: <local path or git remote>
    default_branch: main
    deploy: {enabled: false}
```
