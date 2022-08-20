from flask import Flask, render_template
from controllers.controller import pets_blueprint

app = Flask(__name__)

app.register_blueprint(pets_blueprint)



if __name__ == '__main__':
    app.run(debug=True)