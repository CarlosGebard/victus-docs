# Victus Infra

Infraestructura reproducible para el runtime privado de Victus.

Este repo no contiene la app. Provee la base compartida usada por otros repositorios Victus:

- objetos y artefactos en SeaweedFS S3
- estado durable de papers en Postgres
- eventos live en Redis
- DNS privado con CoreDNS
- edge privado y publico con NGINX
- observabilidad con Prometheus y Loki
- documentacion publica con Wiki.js
- deploy con Ansible y GitHub Actions

[Read in English](/repos/victus-infra/README)

## Vista Rápida

```text
compose/        Docker Compose source of truth
ansible/        deploy al VPS
ops/            scripts y bridge reusable
docs/           documentación esencial
tests/          validaciones Ansible
```

Stacks:

```text
core            nginx, seaweedfs, pipeline-postgres, redis, etcd, coredns
observability   prometheus, loki
llm             LiteLLM, Langfuse, Postgres
wiki            Wiki.js, Postgres
```

## Uso Local

Validar:

```bash
make ansible-check
make compose-validate
```

Levantar `core`:

```bash
make core-up
```

Esto también aplica buckets S3 locales de forma idempotente.

Ver logs:

```bash
make core-logs
```

Bajar:

```bash
make core-down
```

## Bridge Reusable

El SDK/CLI común vive en:

```text
ops/bridge
```

Ejemplo:

```bash
cd ops/bridge
uv run victus-ingest --help
```

El bridge solo comunica con infraestructura común. No implementa Docling, claims, embeddings, Qdrant ni lógica interna de otros repos.

## Deploy

El deploy productivo ocurre desde:

```text
.github/workflows/deploy-all.yml
```

Los secretos vienen desde Infisical vía GitHub OIDC.

## Documentación

- [Índice de documentación](/repos/victus-infra/docs/README)
- [Contexto del sistema](/repos/victus-infra/docs/000-SYSTEM-CONTEXT)
- [Arquitectura](/repos/victus-infra/docs/100-ARCHITECTURE)
- [Networking](/repos/victus-infra/docs/architecture/101-NETWORKING)
- [Compute runtimes](/repos/victus-infra/docs/architecture/102-COMPUTE-RUNTIMES)
- [Data storage](/repos/victus-infra/docs/architecture/103-DATA-STORAGE)
- [Observabilidad](/repos/victus-infra/docs/architecture/104-OBSERVABILITY)
- [Operación](/repos/victus-infra/docs/200-OPERATIONS)
- [Contratos](/repos/victus-infra/docs/300-CONTRACTS)
- [Runtime local](/repos/victus-infra/docs/operations/201-LOCAL-RUNTIME)
- [Deploy](/repos/victus-infra/docs/operations/202-DEPLOYMENT)
- [Seguridad operativa](/repos/victus-infra/docs/operations/203-SECURITY)
- [Troubleshooting](/repos/victus-infra/docs/operations/204-TROUBLESHOOTING)
