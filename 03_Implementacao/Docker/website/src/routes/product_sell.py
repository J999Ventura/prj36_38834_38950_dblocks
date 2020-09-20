from . import app, APP_ROOT, os
from . import RegisterForm, LoginForm, ResendEmailForm, RecoverForm, UploadForm, \
    dummy, request, render_template, session, redirect, url_for, g, login, json, register, \
    recoverPassword, resendEmail, flash, sellProduct, getProductsForsale, getCategories
from . import water_mark_image
from PIL import Image


@app.route('/product-sell', methods=['GET', 'POST'])
def product_sell():
        formlog= LoginForm()
        formreg= RegisterForm()
        formresend = ResendEmailForm()
        formrecover = RecoverForm()
        formupload = UploadForm()

        if formresend.submitresend.data:
            if formresend.validate():
                session.pop('user', None)
                email = request.form['email']
                message, type = resendEmail(email);
                flash(message, type)
            else:
                flash('Wrong inputs, try to register again', 'danger')

        if formrecover.submitrec.data:
            if formrecover.validate():
                session.pop('user', None)
                email = request.form['email']
                message, type = recoverPassword(email);
                flash(message, type)
            else:
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
                message, type = register(fname, lname, email, password, bdate);
                flash(message, type)
            else:
                flash('Wrong inputs, try to register again', 'danger')

        if g.user:
            target = os.path.join(APP_ROOT, 'images\\users\\'+str(g.user["id"]))
            target_water_mark = os.path.join(APP_ROOT, 'static\\users\\' + str(g.user["id"]))

            if not os.path.isdir(target):
                os.mkdir(target)

            if not os.path.isdir(target_water_mark):
                os.mkdir(target_water_mark)

            if formupload.submitupload.data:
                if formupload.validate():
                    product_name = request.form['prodname']
                    product_description = request.form['proddesc']
                    product_price = request.form['prodprice']
                    product_category_id = request.form['prodcatg']
                    for file in request.files.getlist("prodimage"):
                        photo = Image.open(file)
                        #product_w, product_h = photo.size
                        message, type, product_id = sellProduct(product_name, product_description, product_price, g.user["id"], product_category_id)
                        if type == "success":
                            filename = product_id+".jpg"
                            destination = "\\".join([target, filename])
                            file.save(destination)
                            water_mark_image(file, "\\".join([target_water_mark, filename]))

                    flash(message, type)
                else:
                    flash('Wrong inputs, try again', 'danger')

            return render_template('product-sell.html', title='Product Sale',
                                   categories=getCategories(),
                                   userProducts=getProductsForsale(3),
                                   formlog=formlog,
                                   formreg=formreg,
                                   formresend=formresend,
                                   formrecover=formrecover,
                                   formupload=formupload
                                   )

        return redirect(url_for('index'))