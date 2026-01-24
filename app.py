from flask import *
from Controllers.homeController import blueprintHome

def app():
    app = Flask(__name__)

    app.register_blueprint(blueprintHome)

    @app.route('/')
    
    def home():
        return {"message": "Hello, World!"}
    
    return app
    
app = app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True) 