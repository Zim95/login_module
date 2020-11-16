from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

# these models are imported in order to make sure
# models are imported before creating Migrate object.
# from open_oauth.models.user import User


migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
