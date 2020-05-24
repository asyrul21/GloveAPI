# import Flask
from flask import Flask
# Flask restful
from flask_restful import Resource, Api, reqparse


# import resources
from Resources.Index import Index
from Resources.GetVector import GetVector

# create app instance
app = Flask(__name__)
# restful
api = Api(app)


# add resource to route
api.add_resource(Index, '/')
api.add_resource(GetVector, '/GetVector/')

# enable ro disable debugging here
if __name__ == '__main__':
    app.run(debug=True)