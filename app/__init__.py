from app.config import config
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from app.config.cache_config import cache_config
from flask_caching import Cache




db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cache = Cache()

def create_app() -> None:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cache.init_app(app, config=cache_config)

    from app.resources import home
    app.register_blueprint(home, url_prefix='/api/v1')
    from app.resources import purchase
    app.register_blueprint(purchase)
    
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app

