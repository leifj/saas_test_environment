Vagrant.configure(2) do |config|
  config.vm.box = "williamyeh/ubuntu-trusty64-docker"

  config.vm.network "forwarded_port", guest: 9090, host: 9090
  config.vm.network "forwarded_port", guest: 9087, host: 9087
  config.vm.network "forwarded_port", guest: 9088, host: 9088
  config.vm.network "forwarded_port", guest: 9089, host: 9089
  config.vm.network "forwarded_port", guest: 9091, host: 9091

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "deploy/ansible/test_env.yml"
    ansible.verbose = "vv"
  end
end