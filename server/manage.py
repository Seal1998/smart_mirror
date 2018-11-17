from server.core import factory
from flask import render_template

server = factory()

@server.route('/')
def test():
    return render_template('settings.html')

if __name__ == '__main__':
    server.run('10.81.5.244')