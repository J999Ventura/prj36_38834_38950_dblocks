from . import app
from flask import send_file
from . import RegisterForm, LoginForm, ResendEmailForm, RecoverForm, PaymentForm, \
    dummy, request, render_template, session, redirect, \
    url_for, g, login, json, register, recoverPassword, resendEmail, checkoutPayment,\
    flash, getCategories


@app.route("/checkout", methods=['GET', 'POST'])
def checkout():
    formlog = LoginForm()
    formreg = RegisterForm()
    formresend = ResendEmailForm()
    formrecover = RecoverForm()
    formpayment = PaymentForm()

    if formpayment.submitPayment.data:
        if formpayment.validate():
            cardName = request.form['cardName']
            cardNumber = request.form['cardNumber']
            cvc = request.form['cvc']
            month = request.form['month']
            year = request.form['year']
            payment_state = checkoutPayment(cardName, cardNumber, cvc, month, year)
            if(payment_state):
                return redirect(url_for('profile')) #return send_file(path, as_attachment=True)
        if not formpayment.validate():
            flash('Wrong inputs!', 'danger')

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
            return redirect(url_for('profile'))
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
            message, type = register(fname, lname, email, password, bdate)
            flash(message, type)

        if not formreg.validate():
            flash('Wrong inputs, try to register again', 'danger')
    if g.user:
        return render_template('checkout.html', title='Contact',
                               categories=getCategories(),
                               tags=dummy.tags,
                               sizes=dummy.sizes,
                               formlog=formlog,
                               formreg=formreg,
                               formresend=formresend,
                               formrecover=formrecover,
                               formpayment=formpayment
                               )

    return redirect(url_for('index'))


