import re
import os

from fabric.api import *
from fabric.contrib.files import *
from fabric.network import ssh

env.use_ssh_config = True
env.disable_known_hosts = True
env.skip_bad_hosts = True

env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'gardenbuzz.pem')]

ssh.util.log_to_file("paramiko.log", 10)

@hosts('ec2-user@gardenbuzz.com')
def dev_release():
    with cd("/var/www/sites/ditch"):
        run("./siteupdate.sh")



