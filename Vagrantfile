VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.provider "virtualbox" do |v|
      v.memory = 2048
    end
    config.vm.box = "ubuntu/trusty64"
    config.vm.network :forwarded_port, host: 8000, guest: 8001
    config.vm.network :forwarded_port, host: 8432, guest: 5432
    config.vm.provision "fix-no-tty", type: "shell" do |s|
        s.privileged = false
        s.inline = "sudo sed -i '/tty/!s/mesg n/tty -s \\&\\& mesg n/' /root/.profile"
    end
    config.vm.provision :shell, path: "provision/initial.sh"
    config.vm.provision :shell, path: "provision/zsh/install_zsh.sh"
    config.vm.provision :shell, path: "provision/postgresql/install_postgresql.sh"
    config.vm.provision :shell, inline: "apt-get install -y libfreetype6-dev libpng12-dev redis-server"
    config.vm.provision :shell, path: "provision/django/install_django.sh", args: "'djaxelrod'"
    config.vm.provision :shell, path: "provision/sass/install_sass.sh"
end
