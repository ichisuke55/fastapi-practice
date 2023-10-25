import uvicorn
import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


@strawberry.type
class User:
    name: str
    note: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="hoge", note="fuga")

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

app = FastAPI()

@app.get('/')
def get_hello():
    return {'message': 'Hello World'}

app.add_route("/graphql", graphql_app)

if __name__ == '__main__':
    uvicorn.run(app)
