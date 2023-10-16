# Copyright (c) Datalayer, Inc. https://datalayer.io
# Distributed under the terms of the MIT License.

FROM python:3.11

RUN mkdir /opt/jupyter-devcontainers

WORKDIR /opt/jupyter-devcontainers

RUN pip install kazoo

COPY jupyter_devcontainers /opt/jupyter_devcontainers
RUN pip install -e ./jupyter_devcontainers

# COPY frontplane/dist.html /opt/jupyter-devcontainers/index.html

WORKDIR /opt/jupyter-devcontainers/editor

EXPOSE 9300

CMD ["python", "-m", "jupyter_devcontainers"]
