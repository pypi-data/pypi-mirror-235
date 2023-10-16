import json
from typing import Optional
from keyring import get_credential, get_password, set_password, delete_password
import typer
from typing_extensions import Annotated


app = typer.Typer()

@app.command("cred")
def proxy_credential(service: str, username: Annotated[Optional[str], typer.Argument()] = None):
    p = get_credential(service, username)
    if p is None:
        print(json.dumps({"result": None}))
        return
    print(json.dumps({"result": {
        "username": p.username,
        "password": p.password
    }}))

@app.command("get")
def proxy_get_password(service: str, username: str):
    p = get_password(service, username)
    if p is None:
        print(json.dumps({"result": None}))
        return
    print(json.dumps({"result": p}))

@app.command("set")
def proxy_set_password(service: str, username: str, password: str):
    try:
        set_password(service, username, password)
        print(json.dumps({"result": True}))
    except Exception:
        print(json.dumps({"result": False}))
    
@app.command("del")
def proxy_del_password(service: str, username: str):
    try:
        delete_password(service, username)
        print(json.dumps({"result": True}))
    except Exception:
        print(json.dumps({"result": False}))

def main():
    app()


if __name__ == "__main__":
    main()