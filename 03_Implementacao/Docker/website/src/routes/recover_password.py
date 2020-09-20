from . import app
from . import RegisterForm, LoginForm, ResendEmailForm, RecoverForm, RecoverPasswordForm, \
    dummy, request, render_template, session, redirect, \
    url_for, g, login, json, register, recoverPassword, resendEmail, flash, setNewPassword, getCategories

@app.route('/recover-password/{token}', methods=['GET', 'POST'])
def recover_password(token):
    formlog = LoginForm()
    formreg = RegisterForm()
    formresend = ResendEmailForm()
    formrecover = RecoverForm()
    formrecoverpass = RecoverPasswordForm()

    if formresend.submitresend.data:
        if formresend.validate():
            session.pop('user', None)
            email = request.form['email']
            message, type = resendEmail(email)
            flash(message, type)
        if not formresend.validate():
            flash('Wrong inputs, try to register again', 'danger')

    if formrecover.submitrec.data:
        if formrecover.validate():
            session.pop('user', None)
            email = request.form['email']
            message, type = recoverPassword(email)
            flash(message, type)
        if not formrecover.validate():
            flash('Wrong inputs, try to register again', 'danger')

    if formlog.submitlog.data and formlog.validate():
        session.pop('user', None)
        email = request.form['email']
        password = request.form['password']
        login_user = login(email, password)
        if login_user:
            g.user = session['user'] = json.loads(json.dumps(login_user.__dict__))
            return redirect(url_for('index'))
        else:
            flash('Wrong Email or Password', 'danger')

    if formreg.submitreg.data:
        if formreg.validate():
            session.pop('user', None)
            fname = request.form['fname']
            lname = request.form['lname']
            bdate = request.form['bdate']
            email = request.form['email']
            password = request.form['password_reg']
            message, type = register(fname, lname, email, password, bdate);
            flash(message, type)

        if not formreg.validate():
            flash('Wrong inputs, try to register again', 'danger')

    if formrecoverpass.submitnewpassword.data:
        if formrecoverpass.validate():
            session.pop('user', None)
            accepted = setNewPassword(token, password)
        if not formrecoverpass.validate() or not accepted:
            flash('Wrong inputs, try again', 'danger')



    return render_template('recover-password.html', title='Home',
                           categories=getCategories(),
                           formlog=formlog,
                           formreg=formreg,
                           formresend=formresend,
                           formrecover=formrecover,
                           formrecoverpass=formrecoverpass
                           )


