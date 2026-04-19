"""Tiny Flask app used as an integration target.

Routes:
  GET /       -> "ok"
  GET /health -> "ok"
  GET /error  -> 500 (for failure-injection tests)
"""

from __future__ import annotations

import os

from flask import Flask

app = Flask(__name__)


@app.get("/")
def root() -> str:
    return "ok"


@app.get("/health")
def health() -> str:
    return "ok"


@app.get("/error")
def error():
    return "boom", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "3000")))
