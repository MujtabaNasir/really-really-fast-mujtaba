import logging

import uvicorn
from fastapi import FastAPI
from mujtaba_charm.utils.sample import hello

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/hello")
async def get_hello(name: str = None):
    """
    Prints a greeting message. If a name is provided, it greets the name;
    otherwise, it greets the world.

    Args:
        name (str, optional): The name to greet. Defaults to None.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    logger.info(f"Handling /hello request")
    message = hello(name or "World")
    logger.info(f"Returning message: {message}")
    return {"message": message}


@app.get("/health")
async def health_check():
    """
    Returns the health check status of the API.
    """
    logger.info("Handling /health request")
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
