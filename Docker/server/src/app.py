from flask_migrate import Migrate
from api.models import db
from api import create_app

app = create_app()

# Database Management  ('flask db migrate' & 'flask db upgrade')
migrate = Migrate(app, db)

if __name__ == '__main__':
    #	app.run(host='0.0.0.0', port=80, debug=True)
    app.run(debug=True)