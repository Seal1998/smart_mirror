from server.core import factory


server = factory()

if __name__ == '__main__':
    server.run('192.168.0.1')