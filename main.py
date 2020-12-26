from app import create_app
from uvicorn import run


app = create_app()


if __name__ == "__main__":
    run(host="0.0.0.0", port=80, reload=True)
