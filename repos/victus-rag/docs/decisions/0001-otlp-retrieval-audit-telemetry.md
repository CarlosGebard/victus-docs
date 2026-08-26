# ADR 0001: OTLP Retrieval Audit Telemetry

## Status

Accepted

## Context

The project needs first-version RAG audit telemetry for retrieval queries. The
scope excludes LLM answer generation and should keep Phoenix outside application
code.

## Decision

The application emits standard OpenTelemetry traces through OTLP gRPC to
`http://localhost:4317`. Phoenix runs as a collector container and receives
those traces. Application code must not depend on Phoenix SDKs.

Retrieval spans record:

- `app.pipeline_stage`
- `dataset.name`
- `user.query.length_words`
- retrieval backend, top-k, and result count
- retrieved claim ids, ranks, scores, source locators, grounding, metadata, and full claim text

## Consequences

- The app can send traces to Phoenix or any OTLP-compatible collector.
- Local audit requires Phoenix or another collector listening on port `4317`.
- Full claim text is present in telemetry because claims are expected to be short atomic nodes.
- LLM instrumentation remains out of scope.
