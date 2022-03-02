from flask import render_template
from . import main

@main.app_errorhandler(404)
def not_found(error):
    '''
    Handle a Page not found Error
    '''

    return render_template('404.html'),404
