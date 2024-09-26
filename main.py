from fastapi import FastAPI
import asyncio
import uvicorn
from contextlib import asynccontextmanager

import bot  # Import the bot module

app = FastAPI()

async def main():
    config = uvicorn.Config(app, host='0.0.0.0', port=8000)
    server = uvicorn.Server(config)
    
    application = bot.run()
    
    # Run application and webserver together
    async with application:
        await application.start()
        await server.serve()
        await application.stop()


if __name__ == '__main__':
    asyncio.run(main())
