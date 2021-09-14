from flask import *
from flask_cors import CORS
from config import *
app = Flask(__name__)
CORS(app)
if __name__ == "__main__":    
   app.run()