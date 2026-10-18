"""Простой Flask-сервис для кейса «Автодеплой: GitHub Actions + Docker + GitFlow»."""

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        service="flask-autodeploy-case",
        status="ok",
        message="Привет! Образ собран через GitHub Actions и запущен из GHCR.",
    )


@app.get("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
