import connexion
from myapp import get_module_logger


_logger = get_module_logger(__name__)


def main():
    """Entrypoint"""
    try:
        app = connexion.App(__name__, specification_dir='.')
        app.add_api('swagger.yaml', arguments={'title': 'My Title'})
        app.run(host='0.0.0.0', port=10000, debug=False)
    except Exception as exc:
        _logger.error("Fatal error. Could not start webserver due to: %s", exc)
