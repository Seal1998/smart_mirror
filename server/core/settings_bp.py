from flask import Blueprint, render_template, request
from database.db import db
from database.config import Session
from app.manager import manager
import os, signal, subprocess
from config import ROOT_DIR

blueprint = Blueprint('settings', __name__, template_folder='templates')

@blueprint.route('/settings')
def settings():
    return render_template('settings.html')

@blueprint.route('/test')
def testfunc():
    city = db.get_city()
    return city

@blueprint.route('/setset', methods = ['POST', 'GET'])
def setset():
    if request.method == 'POST':
        settings = request.form
        db.set_wifi_config(settings['ssid'], settings['password'])
        #print(db.get_wifi_config())
        #os.kill(int(db.get_pid()), signal.SIGKILL)#todo: в manager
        #subprocess.Popen('python3 {}/main.py'.format(ROOT_DIR), shell=True)
        return 'YEP'