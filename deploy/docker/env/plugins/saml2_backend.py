#!/usr/bin/env python
# -*- coding: utf-8 -*-
from saml2 import BINDING_HTTP_REDIRECT
from saml2 import BINDING_HTTP_POST
from saml2.extension.idpdisc import BINDING_DISCO

from satosa.backends.saml2 import SamlBackend
from satosa.plugin_base.endpoint import BackendModulePlugin

xmlsec_path = '/usr/bin/xmlsec1'

PROVIDER = "Saml2"
MODULE = SamlBackend


class Saml2BackendModulePlugin(BackendModulePlugin):
    def __init__(self, base_url):
        module_base = "%s/%s" % (base_url, PROVIDER)
        sp_config = {
            "entityid": "%s/proxy_saml2_backend.xml" % module_base,
            "description": "A SAML2 SP MODULE",
            "service": {
                "sp": {
                    "endpoints": {
                        "assertion_consumer_service": [
                            ("%s/acs/post" % module_base, BINDING_HTTP_POST),
                            ("%s/acs/redirect" % module_base, BINDING_HTTP_REDIRECT)
                        ],
                        "discovery_response": [
                            ("%s/disco" % module_base, BINDING_DISCO)
                        ]
                    },
                    "allow_unsolicited": True
                }
            },
            "key_file": "backend.key",
            "cert_file": "backend.crt",
            "metadata": {
                "remote": [{"url": "http://localhost/disco/role/idp.xml", "cert": None}],
            },
            "xmlsec_binary": xmlsec_path,
            "logger": {
                "rotating": {
                    "filename": "idp.log",
                    "maxBytes": 500000,
                    "backupCount": 5,
                },
                "loglevel": "debug",
            }
        }

        config = {"config": sp_config,
                  "encryption_key": "E0qmAYUkwQi4",
                  "disco_srv": "http://localhost/disco/role/idp.ds",
                  "publish_metadata": "%s/metadata" % module_base
                  }

        super(Saml2BackendModulePlugin, self).__init__(MODULE, PROVIDER, config)
