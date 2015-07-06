VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT
cd /vagrant
python manage.py migrate
su -c "bower install" vagrant
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.provider "virtualbox" do |v|
      v.memory = 2048
    end
    config.vm.box = "meatballs/djaxelrod"
    config.vm.network :forwarded_port, host: 8000, guest: 8001
    config.vm.network :forwarded_port, host: 8432, guest: 5432
    config.vm.provision "shell", inline: $script
end
