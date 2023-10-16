# Copyright (c) Datalayer, Inc. https://datalayer.io
# Distributed under the terms of the MIT License.

FROM python:3.11

RUN mkdir /opt/jupyter-ssh

WORKDIR /opt/jupyter-ssh

RUN pip install kazoo

COPY jupyter_ssh /opt/jupyter_ssh
RUN pip install -e ./jupyter_ssh

# COPY frontplane/dist.html /opt/jupyter-ssh/index.html

WORKDIR /opt/jupyter-ssh/editor

EXPOSE 9300

CMD ["python", "-m", "jupyter_ssh"]
