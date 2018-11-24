import subprocess, os, socket

class Wifi():
    def __init__(self, interface=None, confname='wpa_supplicant.conf', ssid=None, password = None, driver = 'wext'):
        print(ssid, password)
        self.ssid = ssid
        self.password = password
        self.driver = driver
        self.interface = interface
        self.confname = confname
        self._create_wpa_conf()

    def _create_wpa_conf(self):
        conf = open('{}{}{}'.format(os.getcwd(), '/', self.confname), 'w')
        conf.write('network=' + '{' + '\n\tssid="{}"\n\tpsk="{}"\n'.format(self.ssid, self.password) + '}')
        conf.close()

    def _reload_interface(self):
        self._execute('ifconfig {} down'.format(self.interface))
        self._execute('ifconfig {} up'.format(self.interface))

    def connect(self):
        self._reload_interface()
        self._execute('sudo killall wpa_supplicant')
        self._execute('sudo wpa_supplicant -B -i{} -c{}'.format(
            self.interface,
            os.getcwd()+'/'+self.confname,
        ))
        self._execute('dhclient wlp3s0')

    def check_connection(self):
        try:
            sock = socket.gethostbyaddr('8.8.8.8')
        except:
            return False
        return True

    def _dhclient_on(self):
        self._execute('dhclient {}'.format(self.interface))

    def _execute(self, command):
        output = subprocess.Popen(command, shell=True)
        output.communicate()
        return output.communicate()