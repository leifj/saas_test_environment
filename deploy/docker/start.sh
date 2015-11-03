#!/bin/sh

# copy all config from mounted volume
cp -r /mnt/config/. /tmp/src/satosa/example/

# generate metadata for front- (IdP) and back-end (SP) and write it to mounted volume
python3 /tmp/src/satosa/tools/make_saml_metadata.py -o /mnt/config proxy_conf.yaml

# start the proxy
python3 proxy_server.py proxy_conf.yaml
