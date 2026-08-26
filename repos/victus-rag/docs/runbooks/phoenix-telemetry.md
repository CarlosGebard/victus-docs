# Phoenix Telemetry Runbook

## Purpose

Run Phoenix locally as an OTLP collector for RAG retrieval audit traces.

## Start Phoenix

```bash
docker compose up -d phoenix
docker compose ps
```

Phoenix UI:

```text
http://localhost:6006
```

OTLP gRPC endpoint:

```text
http://localhost:4317
```

## Emit A Test Trace

```bash
uv run victus-rag query sparse \
  --query "diet metabolic syndrome" \
  --top-k 1 \
  --telemetry \
  --dataset-name claims-v1
```

Expected result:

- CLI returns normal retrieval output.
- Phoenix shows a `rag.query` trace.
- Span attributes include `app.pipeline_stage`, `dataset.name`, and `user.query.length_words`.
- Retrieved documents include full claim text under `retrieval.documents.0.document.content`.

## Troubleshooting

If traces are missing:

```bash
docker compose ps
docker compose logs phoenix --tail 100
curl -I http://localhost:6006
```

If running inside a sandboxed environment, local `localhost:4317` may be blocked.
Run the audited query from the host shell.

Disable telemetry by omitting `--telemetry` or setting:

```yaml
telemetry:
  enabled: false
```
