# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox" do |v|
    v.name = "puppetmaster"
    v.memory = 4096
    v.cpus = 2
  end
  config.vm.box = "centos/7"
  config.vm.network "private_network", ip: "192.168.10.10"
  config.vm.hostname = "puppetmaster.local"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "puppetmaster.yml"
    ansible.verbose = "v"
  end
end
