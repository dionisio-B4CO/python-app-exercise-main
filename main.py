#!/usr/bin/env python
import logging

from src.Application.App import App
from config import api_service


def run_app():
    try:
        app = App(api_service)
        app.run()
    except KeyboardInterrupt:
        logging.info("Application interrupted by user.")
    except Exception as e:
        logging.error(f"Error during application execution: {e}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting application...")
    run_app()
