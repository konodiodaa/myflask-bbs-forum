from flask import Flask
import config
from apps.cms import bp as cms_bp
from apps.front import bp as front_bp
from apps.common import bp as common_bp

# config.py/exts.py/modles.py/manage.py
# forward/backward(cms)/public(common) as three blueprint

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
app.register_blueprint(common_bp)

if __name__ == '__main__':
    app.run(port=8000)