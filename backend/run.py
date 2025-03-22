import uvicorn
from app.main import app
from app.db.init_db import init_db

if __name__ == "__main__":
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000) 