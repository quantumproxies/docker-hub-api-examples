"""Minimal Docker Hub images API call — one typed row per image.

Docs & schema: https://quanticdata.io/collectors/docker-hub-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/docker_hub/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "query": "postgres",
        "max_results": 10
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("name"), row.get("description"), row.get("stars"))
print(f"{len(data['results'])} images, cost ${data['cost']}")
