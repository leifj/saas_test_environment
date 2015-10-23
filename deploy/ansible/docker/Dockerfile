# build with 'tar -czh . | sudo docker build -'

FROM williamyeh/ansible:ubuntu14.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    libssl-dev

RUN groupadd -r vagrant && useradd -r -g vagrant vagrant

# ==> Copying Ansible playbook...
WORKDIR /tmp
COPY  .  /tmp

# ==> Creating inventory file...
RUN echo localhost > inventory

# ==> Executing Ansible...
RUN ansible-playbook -i inventory playbook.yml \
      --connection=local --sudo

WORKDIR /home/vagrant/saas/example/
ENTRYPOINT ["python3", "proxy_server.py", "proxy_conf.yaml"]
