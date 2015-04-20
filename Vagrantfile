VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.network :forwarded_port, host: 8000, guest: 8001
    config.vm.network :forwarded_port, host: 8432, guest: 5432
    config.vm.provision :shell, path: "provision/initial.sh"
    config.vm.provision :shell, path: "provision/zsh/install_zsh.sh"
    config.vm.provision :shell, path: "provision/postgresql/install_postgresql.sh"
    config.vm.provision :shell, path: "provision/axelrod/install_axelrod.sh"
    config.vm.provision :shell, path: "provision/django/install_django.sh", args: "'djaxelrod'"
end
