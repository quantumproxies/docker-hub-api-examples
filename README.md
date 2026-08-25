# Docker Hub images API — examples

Docker image search and repository stats — stars, pulls, official flag.

**Live page, full schema & pricing → [quanticdata.io/collectors/docker-hub-api/](https://quanticdata.io/collectors/docker-hub-api/)**

Reads Docker Hub's keyless v2 API in two modes: a query searches images (name, description, stars, pulls, official/automated flags), or a list of image references ("redis", "library/redis", "bitnami/postgresql") returns the full repository record with the last-updated date. References that don't resolve are reported under failed and never billed.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/docker_hub/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "postgres", "max_results": 10}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `query` (string) — Image search query (leave empty when passing images).
- `images` (array) — Exact references for detail lookups — "redis" or "namespace/name".
- `max_results` (integer) — How many images to deliver at most (1–100). You pay only for delivered images.

## Output — one row per image

| field | type | description |
|---|---|---|
| `rank` | integer | 1-based position. |
| `name` | string | Image name (namespace/name; officials bare). |
| `description` | string | Short description. |
| `stars` | integer | Stars. |
| `pulls` | integer | Total pulls. |
| `is_official` | boolean | Docker official image. |
| `is_automated` | boolean | Automated build. |
| `last_updated` | string | Last push (detail mode only). |
| `url` | string | Docker Hub page. |

## Pricing

**$0.0003 per delivered image** ($0.3 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 6,666 images — no card required.

## Links

- This collector: https://quanticdata.io/collectors/docker-hub-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
