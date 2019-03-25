from gevent.pywsgi import WSGIServer
from myapp import get_module_logger, app


_logger = get_module_logger(__name__)


def main():
    """Entrypoint"""
    _logger.debug("Starting gevent server")

    http_server = WSGIServer(('', 10000), app)
    http_server.serve_forever()
