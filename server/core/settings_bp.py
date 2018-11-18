from flask import Blueprint, render_template, request

blueprint = Blueprint('settings', __name__, template_folder='templates')

@blueprint.route('/settings')
def settings():
    return render_template('settings.html')

@blueprint.route('/setset', methods = ['POST', 'GET'])
def setset():
    if request.method == 'POST':
        settings = request.form
        print(settings)
        return 'YEP'