from open_oauth import app_factory, resources


factory = app_factory.create_app()
app = factory['app']
api = factory['api']
oauth = factory['oauth']
db = factory['db']


api.add_resource(resources.Ping, '/ping')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)