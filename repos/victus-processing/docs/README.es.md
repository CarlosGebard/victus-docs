# victus-processing

Estado documental: `source-of-truth` desde `2026-05-27`.

Pipeline local para convertir papers científicos en metadata, PDFs
normalizados, bloques estructurados y evidencia canónica.

## Qué Resuelve

- busca candidatos en Semantic Scholar
- guarda metadata canónica
- linkea PDFs obtenidos manualmente
- procesa PDFs con Docling y heurísticas locales
- extrae evidencia canónica con modelos LLM via LiteLLM

## Uso Local

```bash
uv sync
uv run victus-processing --help
uv run victus-processing data-layout create
```

Flujo principal:

```bash
uv run victus-processing metadata-extraction explore --mode broad-nutrition
uv run victus-processing bibliography-export generate-bib
uv run victus-processing pdf-intake link --metadata-id meta:s2:example --pdf data/artifacts/intake/pdfs/example.pdf
uv run victus-processing pdf-processing run
```


## Validar

```bash
uv run pytest tests/test_cli_smoke.py -q
```

## Leer Más

- [Contexto del sistema](/repos/victus-processing/docs/000-SYSTEM-CONTEXT)
- [Arquitectura](/repos/victus-processing/docs/100-ARCHITECTURE)
- [Contratos](/repos/victus-processing/docs/300-CONTRACTS)
- [Contrato de layout](/repos/victus-processing/docs/contracts/local/data-layout)
- [Contrato de handoffs](/repos/victus-processing/docs/contracts/local/stage-handoffs)
- [Contrato de schemas](/repos/victus-processing/docs/contracts/local/artifact-schemas)
- [Contrato de StructuredBlock](/repos/victus-processing/docs/contracts/fundamental/scientific/structured-block)
- [Contrato de ExperimentMap](/repos/victus-processing/docs/contracts/fundamental/scientific/experiment-map)
- [Contrato de CanonicalEvidence](/repos/victus-processing/docs/contracts/fundamental/scientific/canonical-evidence)
- [Operación](/repos/victus-processing/docs/200-OPERATIONS)
- [CLI local](/repos/victus-processing/docs/operations/cli)
- [Runbooks](operations/runbooks/)
