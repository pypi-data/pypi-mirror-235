import sys
from urllib.parse import urljoin

import requests
import typer
from rich import print

from chatfaq_cli import config, conversations, data, rag_pipeline, reviews, senders
from chatfaq_cli.helpers import CONFIG_FILE_PATH, get_config

app = typer.Typer()
app.add_typer(config.app, name="config")
app.add_typer(conversations.app, name="conversations")
app.add_typer(data.app, name="data")
app.add_typer(rag_pipeline.app, name="rag_pipeline")
app.add_typer(senders.app, name="senders")
app.add_typer(reviews.app, name="reviews")


class Requester:
    API_HOST = urljoin(get_config().get("host"), "/back/api/")

    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"Token {token}"}

    @staticmethod
    def response(fun):
        """
        Decorator to handle response from API.
        """

        def wrapper(*args, json=True, **kwargs):
            res = fun(*args, **kwargs)
            if json and res.status_code < 400:
                return res.json()
            if res.status_code >= 400:
                return res.text
            return res

        return wrapper

    @response
    def get(self, url):
        return requests.get(self.API_HOST + url, headers=self.headers)

    @response
    def post(self, url, data=None, files=None):
        if files:
            return requests.post(
                self.API_HOST + url, headers=self.headers, files=files, data=data
            )
        else:
            return requests.post(self.API_HOST + url, headers=self.headers, json=data)

    @response
    def patch(self, url, data=None, files=None):
        if files:
            return requests.patch(
                self.API_HOST + url, headers=self.headers, files=files, data=data
            )
        else:
            return requests.patch(self.API_HOST + url, headers=self.headers, json=data)

    @response
    def delete(self, url, data=None):
        return requests.delete(self.API_HOST + url, headers=self.headers, json=data)


@app.callback()
def main(ctx: typer.Context):
    """
    ChatFAQ CLI
    """

    if not ("config" in sys.argv or "--help" in sys.argv or "-h" in sys.argv):
        if not get_config().get("token"):
            print(
                "Token not configured. Run `chatfaq config auth <YOUR_TOKEN>` to configure it."
            )
            print("You can obtain a token by visiting your endpoint: /back/api/login/.")
            raise typer.Exit(code=1)
        if not get_config().get("host"):
            print(
                "Host not configured. Run `chatfaq config host <HOST>` to configure it."
            )
            raise typer.Exit(code=1)

        ctx.ensure_object(dict)
        ctx.obj["r"] = Requester(get_config()["token"])
