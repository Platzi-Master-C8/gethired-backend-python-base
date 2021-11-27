#! /usr/env python

import uvicorn


def main():
    """
    Main
    It runs a fastapi server using uvicorn
    """
    uvicorn.run(
        "config.app:application",
        host='0.0.0.0',
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
