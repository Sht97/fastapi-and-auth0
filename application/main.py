"""FastAPI starter sample
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/public")
def public():
    """No access token required to access this route"""

    return {
        "status": "success",
        "msg": (
            "Hello from a public endpoint! "
            "You don't need to be authenticated to see this."
        ),
    }


@app.get("/api/private")
def private():
    """A valid access token is required to access this route"""

    return {
        "status": "success",
        "msg": (
            "Hello from a private endpoint! "
            "You need to be authenticated to see this."
        ),
    }
