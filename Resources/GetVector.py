from flask_restful import Resource, reqparse
from flask_restful import fields, marshal_with
from markupsafe import escape


# define arguments parser
# reqparse is Resource specific
# i.e. args defined in here does not work in other Resources
parser = reqparse.RequestParser()
parser.add_argument('sentence', type=str,
                    help='Input sentence')

# define data format
# may be optional
resource_fields = {
    'vector': fields.String
}


class GetVector(Resource):
    @marshal_with(resource_fields)
    def get(self):
        # get input
        message = parser.parse_args()['sentence']

        # escape input message
        escapedMessage = escape(message)

        # return response as json
        return {
            "vector": escapedMessage,
        }
