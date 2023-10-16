"""Docker handler."""

import json

import tornado

import docker

from jupyter_server.base.handlers import APIHandler
from jupyter_server.extension.handler import ExtensionHandlerMixin

from ..._version import __version__


client = docker.from_env()


# pylint: disable=W0223
class ImagesHandler(ExtensionHandlerMixin, APIHandler):
    """The handler for the devcontainers"""

    @tornado.web.authenticated
    @tornado.gen.coroutine
    def get(self):
        """Returns the devcontainers images."""
        images = map(lambda image: image.attrs, client.images.list())
        res = json.dumps({
            "success": True,
            "message": "List of Devcontainers.",
            "images": list(images),
        }, default=str)
        self.finish(res)


# pylint: disable=W0223
class ContainersHandler(ExtensionHandlerMixin, APIHandler):
    """The handler for devcontainers containers."""

    @tornado.web.authenticated
    @tornado.gen.coroutine
    def get(self):
        """Returns the devcontainers containers."""
        containers = map(lambda container: container.attrs, client.containers.list())
        res = json.dumps({
            "success": True,
            "message": "List of Devcontainers.",
            "containers": list(containers),
        }, default=str)
        self.finish(res)
