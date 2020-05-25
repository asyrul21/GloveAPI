# import Flask
from SupportClasses.WordEmbedderSpacy import WordEmbedderSpacy
from flask import Flask
from flask_restful import Resource, Api, reqparse

# using resource to limit memory
# https://www.geeksforgeeks.org/python-how-to-put-limits-on-memory-and-cpu-usage/
import resource
# import resources
from Resources.Index import Index
from Resources.GetVector import GetVector

maxMemory = 5.12e+8


def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


# from SupportClasses.WordEmbedder import WordEmbedder
we = WordEmbedderSpacy()

# create app instance
app = Flask(__name__)
# restful
api = Api(app)


# add resource to route
api.add_resource(Index, '/')
api.add_resource(GetVector, '/GetVector/',
                 resource_class_kwargs={
                     'wordEmbedder': we})

# enable ro disable debugging here
if __name__ == '__main__':
    limit_memory(maxMemory)
    app.run(debug=True)
