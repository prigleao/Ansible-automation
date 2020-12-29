
from cli import configure, execute
USER="cisco"
PASSWORD="cisco"
ENABLE="cisco"
    
def base_config():
    configure(['hostname ztp-server'])
    configure(['username {} privilege 15 password {}'.format(USER,PASSWORD)])
    configure(['enable secret {}'.format(ENABLE)])
    configure(['line vty 0 4', 'login local'])
    execute('write memory')
    
base_config()