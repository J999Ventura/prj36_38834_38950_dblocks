from . import app
from . import RegisterForm, LoginForm, ResendEmailForm, RecoverForm, \
    dummy, request, render_template, session, redirect, \
    url_for, g, login, json, register, recoverPassword, resendEmail, flash, getProductDetails, getTopRated,getCategories


#@app.route("/product-details", methods=['GET', 'POST'])
@app.route("/product-details/<int:user_id>/<int:product_id>", methods=['GET', 'POST'])
def product_details(user_id, product_id):
    ######## Fazer downgrade da resolucao quando fizer download #### remover todas as resolucoes mais baixas #####

    formlog= LoginForm()
    formreg= RegisterForm()
    formresend = ResendEmailForm()
    formrecover = RecoverForm()

    if formresend.submitresend.data:
        if formresend.validate():
            session.pop('user', None)
            email = request.form['email']
            message, type = resendEmail(email);
            flash(message, type)
        if not formresend.validate():
            flash('Wrong inputs, try to register again', 'danger')

    if formrecover.submitrec.data:
        if formrecover.validate():
            session.pop('user', None)
            email = request.form['email']
            message, type = recoverPassword(email);
            flash(message, type)
        if not formrecover.validate():
            flash('Wrong inputs, try to register again', 'danger')

    if formlog.submitlog.data and formlog.validate():
        session.pop('user', None)
        email = request.form['email']
        password = request.form['password']
        login_user = login(email, password);
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

    return render_template('product-details.html', title='Product',
                           categories=getCategories(),
                           tags=dummy.tags,
                           formlog=formlog,
                           prod=getProductDetails(user_id, product_id),
                           formreg=formreg,
                           formresend=formresend,
                           formrecover=formrecover,
                           topRatedProds=getTopRated()
                           )
