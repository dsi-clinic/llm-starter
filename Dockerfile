# This is a basic docker image for use in the clinic
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Switch to root to update and install tools
USER root
RUN apt-get update && apt-get install -y curl

# Create working directory
WORKDIR /project

# Copy config for initial install
COPY pyproject.toml .

# Create venv in /opt so it won't be shadowed by volume mounts
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
RUN /usr/local/bin/uv venv $UV_PROJECT_ENVIRONMENT
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN uv sync --no-install-project

CMD ["/bin/bash"]
