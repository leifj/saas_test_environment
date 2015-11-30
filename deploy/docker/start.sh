#!/bin/sh

if [ ! -f /mnt/config/backend.key -o ! -f /mnt/config/backend.crt ]; then
   openssl genrsa 4096 > /mnt/config/backend.key
   openssl req -x509 -sha256 -new -subj "/CN=${HOSTNAME}" -key /mnt/config/backend.key -out /mnt/config/backend.crt
fi

if [ ! -f /mnt/config/frontend.key -o ! -f /mnt/config/frontend.crt ]; then
   openssl genrsa 4096 > /mnt/config/frontend.key
   openssl req -x509 -sha256 -new -subj "/CN=${HOSTNAME}" -key /mnt/config/frontend.key -out /mnt/config/frontend.crt
fi

# copy all config from mounted volume
cp -r /mnt/config/. /tmp/src/satosa/example/

# generate metadata for front- (IdP) and back-end (SP) and write it to mounted volume
python3 /tmp/src/satosa/tools/make_saml_metadata.py -o /mnt/config proxy_conf.yaml

# start the proxy
python3 proxy_server.py proxy_conf.yaml
