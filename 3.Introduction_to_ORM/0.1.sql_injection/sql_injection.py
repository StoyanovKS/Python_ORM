from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.get('/test')
def test_func(payload: User):
    con = sqlite3.connect('injection.db')
    query = f"SELECT * FROM users where username = '{payload.username}' and password = '{payload.password}'" = f'p{payload.password}'
    print(query)
    cur = con.cursor()
    data = cur.execute(query).fetchone()
    if data is None:
        return {'message': 'invalid username or password'}
    else:
        return {
            'user': data[0]
            'password': data[1]
        }
    #return 'Hello test!'


if __name__ == '__main__':
    uvicorn.run('test:app', host='127.0.0.1', port=4557, reload=True)
