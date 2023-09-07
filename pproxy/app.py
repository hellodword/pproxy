import io
import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routes import main_router


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("VERSION")
    """
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


description = """
pproxy API helps you do awesome stuff. 🚀
"""

app = FastAPI(
    title="pproxy",
    description=description,
    version=read("VERSION"),
    terms_of_service="http://pproxy.com/terms/",
    contact={
        "name": "author_name",
        "url": "http://pproxy.com/contact/",
        "email": "author_name@pproxy.com",
    },
    license_info={
        "name": "The Unlicense",
        "url": "https://unlicense.org",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router)
