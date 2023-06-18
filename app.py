from flask import Flask
from models.utils import coll_users
from project_utils import setup_logging
log = setup_logging('current_log')
app = Flask(__name__)


# Create the admin blueprint
from admin.register import admin_blueprint
app.register_blueprint(admin_blueprint)


if __name__ == '__main__':
    app.run()

