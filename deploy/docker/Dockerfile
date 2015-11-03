FROM ubuntu:14.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    python3-dev \
    build-essential \
    python3-pip \
    libffi-dev \
    libssl-dev \
    xmlsec1 \
    libyaml-dev

RUN pip3 install --src /tmp/src -e git+https://github.com/its-dirg/SATOSA@998c184#egg=SATOSA && \
    pip3 install -r /tmp/src/satosa/requirements.txt

COPY start.sh /tmp/saas/
WORKDIR /tmp/src/satosa/example/
ENTRYPOINT ["/tmp/saas/start.sh"]
