import subprocess, os

class AccessPoint():
    def __init__(self,
                 interface="wlan0",
                 driver = 'nl80211',
                 ssid = 'MyAccessPoint',
                 hw_mode = 'g',
                 channel='6',
                 wpa = '2',
                 wpa_passphrase = '11111111',
                 wpa_key_mgmt = 'WPA-PSK',
                 wpa_pairwise = 'CCMP',
                 macaddr_acl = '0'):
        self.interface = interface
        self.driver = driver
        self.ssid = ssid
        self.hw_mode = hw_mode
        self.channel = channel
        self.wpa = wpa
        self.wpa_passphrase=wpa_passphrase
        self.wpa_key_mgmt = wpa_key_mgmt
        self.wpa_pairwise = wpa_pairwise
        self.macaddr_acl = macaddr_acl

        self.confname = 'hostapd.conf'
        self.create_hostapd_conf()

    def create_hostapd_conf(self):
        conf = open('{}{}{}'.format(os.getcwd(),'/',self.confname), 'w')
        conf.write('interface={}\n'
                   'driver={}\n'
                   'ssid={}\n'
                   'hw_mode={}\n'
                   'channel={}\n'
                   'wpa={}\n'
                   'wpa_passphrase={}\n'
                   'wpa_key_mgmt={}\n'
                   'wpa_pairwise={}\n'
                   'macaddr_acl={}'.format(
            self.interface,
            self.driver,
            self.ssid,
            self.hw_mode,
            self.channel,
            self.wpa,
            self.wpa_passphrase,
            self.wpa_key_mgmt,
            self.wpa_pairwise,
            self.macaddr_acl,
        ))

    def _execute(self, command):
        output = subprocess.Popen(command, shell=True)
        output.wait()
        output.communicate()

    def start(self):
        try:
            self._execute('killall wpa_supplicant')
            self._execute('sleep 5')
            self._execute('hostapd -B {}'.format(self.confname))
        except:
            print('Error')

    def stop(self):
        self._execute('killall hostapd')
        self._execute('systemctl start wpa_supplicant')

point = AccessPoint(ssid='FREE_DRUGS', wpa_passphrase='shittymirror225', interface='wlp3s0')

#point.start()
point.stop()