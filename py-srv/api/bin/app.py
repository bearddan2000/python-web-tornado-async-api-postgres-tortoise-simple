from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

import settings
from model import Dog
    
app = FastAPI()

register_tortoise(
    app,
    db_url= '{engine}://{username}:{password}@{host}/{db_name}'.format(
    **settings.POSTGRESQL),
    modules={'models': ['model']}
)

@app.get('/dog')
async def get_all_dog():
    pops = pydantic_model_creator(Dog)
    return await pops.from_queryset(Dog.all())
    
if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0')
