from . import app
from . import request, redirect, \
    url_for, flash, setConfirmEmail

@app.route('/confirm-email', methods=['GET', 'POST'])
def confirm_email():
    token = request.args['token']
    if token:
        message, type =setConfirmEmail(token)
    else:
        message = "Error, try to resend email confirmation"
        type = "danger"

    flash(message, type)

    return redirect(url_for('index'))


