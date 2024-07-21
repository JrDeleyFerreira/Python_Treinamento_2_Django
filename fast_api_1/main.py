import uvicorn
from modelo_endpoint import analyze_controller, router_controller 

from fastapi import FastAPI

app = FastAPI()

app.include_router(analyze_controller.router)
app.include_router(router_controller.router)

if __name__ == '__main__':
    uvicorn.run(app= app, host= '127.0.0.1', port= 3001)