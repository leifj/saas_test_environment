The purpose of this project is to supply a test environment for running integration tests for 
the SaaS application. In order to get a platform independent platform Vagrant is used. 

NOTE: Currently the test environment is not complete.

Dependencies:
=============
In order to use this test environment please install:
    * Vagrant (https://www.vagrantup.com/downloads.html)
    * Ansible (http://docs.ansible.com/ansible/intro_installation.html)
    
Setup the environment:
======================
In order to setup and use the test environment please complete the following steps:
    * Open a terminal, go to the saas_test_environment folder
    * Run the command 
       * Vagrant up


Useful vagrant commands:
========================
vagrant up - sets up a virtual environment using for example VirtualBox.
vagrant ssh - Enters teh virtual virtual environment using ssh.
vagrant provision - In this case it reruns the Ansible script.
vagrant destroy - Removes the virtual environment
vagrant reload - restarts the virtual environment

Using the Test environment:
===========================
The test environment contains a SP, a PYFF discovery server and two 
IdPs. The SP could talk to the IdPs by contacting the discovery server. 
The environment should also contain the SaaS proxy. 

When the test environment is complete the SP should talk to the SaaS proxy and the proxy should
use the discovery server

Components setup:
    * The SP is running 127.0.0.1:9087. and publishes metadata at the endpoint **/metadata** 
    * The discovery server is running 127.0.0.1:9090.
    * The IdPs are running 127.0.0.1:9088 and 127.0.0.1:9089.

Open the browser and visit the url in order to test the complete flow.

    