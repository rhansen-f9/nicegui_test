# 1. Use the official uv image to get the uv binary
FROM ghcr.io/astral-sh/uv:latest AS uv

# 2. Build stage
FROM python:3.14-slim-trixie
COPY --from=uv /uv /uvx /bin/

# 3. Set up workspace
WORKDIR /app

# 4. Install dependencies (separated for caching)
COPY uv.lock pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --no-install-project

# 5. Copy application code
COPY . .

# 6. Final sync (optional, if code depends on project installation)
RUN uv sync --no-dev

# 7. Run application
ENV PATH="/app/.venv/bin:$PATH"
CMD ["uv", "run", "main.py"]