from flask_restful import Resource


class Ping(Resource):

    def get(self):
        return 'Ping:get it now'
    
    def post(self):
        return 'Ping:post'
    
    def put(self):
        return 'Ping:put'
    
    def delete(self):
        return 'Ping:delete'