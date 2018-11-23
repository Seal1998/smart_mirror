import subprocess, os

class WifiConnect():
    def __init__(self, interface=None, confname='wpa_supplicant.conf', ssid=None, password = None, driver = 'nl80211'):
        self.ssid = ssid
        self.password = password
        self.driver = driver
        self.interface = interface
        self.confname = confname
        self.create_wpa_conf()

    def create_wpa_conf(self):
        conf = open('{}{}{}'.format(os.getcwd(), '/', self.confname), 'w')
        conf.write('network=' + '{' + '\n\tssid="{}"\n\tpsk="{}"\n'.format(self.ssid, self.password) + '}')
        conf.close()

    def reload_interface(self):
        self._execute('ifconfig {} down'.format(self.interface))
        self._execute('ifconfig {} up'.format(self.interface))

    def connect(self):
        self.reload_interface()


    def test(self):
        self._execute('nmcli d wifi connect {} password {} iface {}'.format(self.ssid,
                                                                            self.password,
                                                                            self.interface))
    def _execute(self, command):
        output = subprocess.Popen(command, shell=True)
        output.communicate()
        return output.communicate()

point = WifiConnect(interface='wlp3s0', ssid='Samsung-TV', password='jojolover225')
point.test()