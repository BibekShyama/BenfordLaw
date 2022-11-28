from benfordCalculation import frequency, f
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(
    route_name="home",
    renderer="json"
)
def home(request):
    return ({
        "result": f
    })



if __name__=="__main__":
    with Configurator() as config:
        config.add_route('home','/')
        config.scan()
        app=config.make_wsgi_app()
    server=make_server('0.0.0.0', 8080,app)
    print("Run localhost:8080 on your browser")
    server.serve_forever()
