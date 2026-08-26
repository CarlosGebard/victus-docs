# Victus Infra

Reproducible infrastructure for the private Victus runtime.

This repository does not contain the application. It provides the shared runtime used by other Victus repositories:

- object storage and artifacts in SeaweedFS S3
- durable paper state in Postgres
- live events in Redis
- private DNS with CoreDNS
- private and public edge routing with NGINX
- observability with Grafana, Prometheus, and Loki
- public documentation with Wiki.js
- deployment with Ansible and GitHub Actions

[Leer en español](/repos/victus-infra/docs/README.es)

## Quick View

```text
compose/        Docker Compose source of truth
ansible/        VPS deployment
ops/            scripts and reusable bridge
docs/           essential documentation
tests/          Ansible validation
```

Stacks:

```text
core            nginx, seaweedfs, pipeline-postgres, redis, etcd, coredns
observability   grafana, prometheus, loki
llm             LiteLLM, Langfuse, Postgres
wiki            Wiki.js, Postgres
```

## Local Use

Validate:

```bash
make ansible-check
make compose-validate
```

Start `core`:

```bash
make core-up
```

This also applies local S3 buckets idempotently.

Logs:

```bash
make core-logs
```

Stop:

```bash
make core-down
```

## Reusable Bridge

The shared SDK/CLI lives in:

```text
ops/bridge
```

Example:

```bash
cd ops/bridge
uv run victus-ingest --help
```

The bridge only talks to shared infrastructure. It does not implement Docling, claims, embeddings, Qdrant, or app-specific logic.

## Deployment

Production deploy runs through:

```text
.github/workflows/deploy-all.yml
```

Secrets come from Infisical through GitHub OIDC.

## Documentation

- [Documentation Index](/repos/victus-infra/docs/README)
- [System Context](/repos/victus-infra/docs/000-SYSTEM-CONTEXT)
- [Architecture](/repos/victus-infra/docs/100-ARCHITECTURE)
- [Networking Architecture](/repos/victus-infra/docs/architecture/101-NETWORKING)
- [Compute Runtimes](/repos/victus-infra/docs/architecture/102-COMPUTE-RUNTIMES)
- [Data Storage](/repos/victus-infra/docs/architecture/103-DATA-STORAGE)
- [Observability Architecture](/repos/victus-infra/docs/architecture/104-OBSERVABILITY)
- [Operations](/repos/victus-infra/docs/200-OPERATIONS)
- [Contracts](/repos/victus-infra/docs/300-CONTRACTS)
- [Local Runtime](/repos/victus-infra/docs/operations/201-LOCAL-RUNTIME)
- [Deployment](/repos/victus-infra/docs/operations/202-DEPLOYMENT)
- [Security Operations](/repos/victus-infra/docs/operations/203-SECURITY)
- [Troubleshooting](/repos/victus-infra/docs/operations/204-TROUBLESHOOTING)
