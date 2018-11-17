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
                 macaddr_acl = '0',
                 gateway = '192.168.0.1',):
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
        self.gateway = gateway

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
        #output.wait()
        return output.communicate()

    def start(self):
        self._execute('killall wpa_supplicant')
        self.start_dhcp_server()
        self.reload_interface()
        self.static_srv_addr('add')
        self._execute('hostapd -B {}'.format(self.confname))

    def static_srv_addr(self, mode):
        self._execute('ip addr {} {}/24 dev {}'.format(mode, self.gateway, self.interface))

    def start_dhcp_server(self):
        self._execute('systemctl stop dnsmasq')
        self._execute('systemctl start dnsmasq')
        #self._execute('ip addr add {}/24 dev {}'.format(self.gateway, self.interface))

    def stop(self):
        self._execute('killall hostapd')
        self._execute('killall dnsmasq')
        self.static_srv_addr('del')
        self._execute('systemctl start wpa_supplicant')

    def reload_interface(self):
        self._execute('ifconfig {} down'.format(self.interface))
        self._execute('ifconfig {} up'.format(self.interface))

point = AccessPoint(ssid='SMIRROR', wpa_passphrase='shittymirror225', interface='wlp0s20u1', driver='rtl871xdrv')

#point.start()
#point.stop()

while 1:
    ch = input('(1) ON\n(2) OFF\n')
    if ch == '1':
        point.start()
    else:
        point.stop()
