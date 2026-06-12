from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]
    
@app.route("/present", ['GET', 'POST'])
async def give_present(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}  # f文字列というPythonの機能を使っている

from fastapi.responses import HTMLResponse

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html lang="ja">
        <meta charset="UTF-8">
        <head>
            <meta charset="UTF-8">
            <title>課題9-1</title>
        </head>
        <body>
            <h1>こんにちは！</h1>
            <img src="img/udon.jpg">
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)