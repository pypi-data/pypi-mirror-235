"""Executable for running motley_cue in development.
"""
import uvicorn


# def main(*args, **kwargs):
def main():
    """run alise with uvicorn"""
    uvicorn.run("alise.api:api", host="0.0.0.0", port=4711, log_level="info")


if __name__ == "__main__":
    main()
