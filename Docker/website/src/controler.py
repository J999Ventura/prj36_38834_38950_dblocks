from flask import render_template, Flask, flash, redirect, url_for
from forms import RegisterForm, LoginForm
app = Flask(__name__)

# Aplication key, to not allow xss, csrf, or injections on forms
app.config['SECRET_KEY'] = '22b9dac894bfa6b43fb78e8c14ef7ce058839cae87d38b31c893967343491ece'

newProds = [
    {
        'name': 'name1',
        'seller': 'seller1',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name2',
        'seller': 'seller2',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name3',
        'seller': 'seller3',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name4',
        'seller': 'seller4',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name5',
        'seller': 'seller6',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name6',
        'seller': 'seller6',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name7',
        'seller': 'seller7',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name8',
        'seller': 'seller8',
        'price': '€1,00',
        'image': 'path'
    }
]

paidPublsishProds = [
    {
        'name': 'name1',
        'seller': 'seller1',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name2',
        'seller': 'seller2',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name3',
        'seller': 'seller3',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name4',
        'seller': 'seller4',
        'price': '€1,00',
        'image': 'path'
    }
]

luckyWeekProds = [
    {
        'name': 'name1',
        'seller': 'seller1',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name2',
        'seller': 'seller2',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name3',
        'seller': 'seller3',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name4',
        'seller': 'seller4',
        'price': '€1,00',
        'image': 'path'
    }
]

topRatedProds = [
    {
        'name': 'name1',
        'seller': 'seller1',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name2',
        'seller': 'seller2',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name3',
        'seller': 'seller3',
        'price': '€1,00',
        'image': 'path'
    }
]

categories = [
    {
        'name': 'Category1'
    },
    {
        'name': 'Category2'
    },
    {
        'name': 'Category3'
    }
]

tags = [
    {
        'name': 'tag1'
    },
    {
        'name': 'tag2'
    },
    {
        'name': 'tag3'
    }
]

slideNews = [
    {
        'title': 'Title1',
        'subTitle': 'SubTitle1',
        'image': 'path',
        'link': 'link'
    },
    {
        'title': 'Title2',
        'subTitle': 'SubTitle2',
        'image': 'path',
        'link': 'link'
    },
    {
        'title': 'Title3',
        'subTitle': 'SubTitle3',
        'image': 'path',
        'link': 'link'
    }
]

newsOfTheDay = [
    {
        'title': 'Title1',
        'subTitle': 'SubTitle1',
        'image': 'path',
        'link': 'link'
    }
]

newProds = [
    {
        'name': 'name1',
        'seller': 'seller1',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name2',
        'seller': 'seller2',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name3',
        'seller': 'seller3',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name4',
        'seller': 'seller4',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name5',
        'seller': 'seller6',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name6',
        'seller': 'seller6',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name7',
        'seller': 'seller7',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name8',
        'seller': 'seller8',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name9',
        'seller': 'seller9',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name10',
        'seller': 'seller10',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name11',
        'seller': 'seller11',
        'price': '€1,00',
        'image': 'path'
    },
    {
        'name': 'name12',
        'seller': 'seller12',
        'price': '€1,00',
        'image': 'path'
    }
]

sizes = [
    {
        'name': '408p'
    },
    {
        'name': '720p'
    },
    {
        'name': '1080p'
    },
    {
        'name': '2160p'
    }
]



@app.route('/')
@app.route("/index", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def index():
    formlog= LoginForm()
    formreg= RegisterForm()
    if formreg.validate_on_submit():
        flash('Check your email, to validate your account', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', title='Home',
                           categories=categories,
                           newProds=newProds,
                           paidPublsishProds=paidPublsishProds,
                           luckyWeekProds=luckyWeekProds,
                           topRatedProds=topRatedProds,
                           slideNews=slideNews,
                           newsOfTheDay=newsOfTheDay,
                           formlog=formlog,
                           formreg=formreg
                           )


@app.route("/product-grid", methods=['GET', 'POST'])
def searchProduct():
    formlog = LoginForm()
    formreg = RegisterForm()
    if formreg.validate_on_submit():
        flash('Check your email, to validate your account', 'success')
        return redirect(url_for('index'))
    return render_template('product-grid.html', title='Home',
                           categories=categories,
                           tags=tags,
                           sizes=sizes,
                           allCategoryProducts=newProds,
                           formlog=formlog,
                           formreg=formreg
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

