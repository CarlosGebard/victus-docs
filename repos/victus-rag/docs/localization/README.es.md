# victus-rag

CLI experimental para retrieval sobre claims cientificos.

`victus-rag` permite construir indices, consultar y evaluar estrategias sparse, dense e
hybrid. No genera respuestas finales; se enfoca en comportamiento de retrieval, metricas y
artefactos inspeccionables.

## Inicio Rapido

```bash
uv sync
uv run victus-rag --help
uv run victus-rag index sparse
uv run victus-rag query sparse --query "mediterranean diet metabolic syndrome" --top-k 5
```

Dense retrieval requiere Qdrant y claims embebidas:

```bash
docker compose up -d qdrant
uv run victus-rag index qdrant --parquet-path data/claims_embedded.parquet
```

## Validacion

```bash
uv run python -m compileall src
uv run victus-rag --help
uv run victus-rag index qdrant --help
```

## Documentacion

- [Contexto del sistema](/repos/victus-rag/docs/000-SYSTEM-CONTEXT)
- [Arquitectura](/repos/victus-rag/docs/100-ARCHITECTURE)
- [Operaciones](/repos/victus-rag/docs/200-OPERATIONS)
- [Contratos](/repos/victus-rag/docs/300-CONTRACTS)

## Responsabilidades

Este repositorio posee workflows de retrieval, indexacion, evaluacion y artefactos locales.

No posee parsing de PDFs, generacion upstream de claims, entrenamiento de embeddings,
serving productivo ni generacion de respuestas finales.
