from fastapi import FastAPI, HTTPException
from parent_details.main import app as parent_app
from driver_details.main import app as driver_app
from admin.admin import router as admin_router

app = FastAPI()

# Include all routers
app.include_router(parent_app.router)
app.include_router(driver_app.router)
app.include_router(admin_router)

# Health check endpoint
@app.get("/health")
async def health_check():
    try:
        return {"status": "healthy"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}")
