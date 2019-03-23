from myapp import get_module_logger, app


_logger = get_module_logger(__name__)


def main():
    """Entrypoint"""
    try:
        _logger.debug("Starting!")
        app.run(host='0.0.0.0', port=10000, debug=False)
    except Exception as exc:
        _logger.error("Fatal error. Could not start webserver due to: %s", exc)
