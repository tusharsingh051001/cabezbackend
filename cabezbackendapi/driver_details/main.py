from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
import time
import datetime
import logging
from pytz import timezone
import uuid
from driver_details.query import query_hasura
from config import get_hasura_endpoint, get_secret_key

app = FastAPI()

class driverRequest(BaseModel):
    """
    Request model for driver details.
    """
    username: str

@app.post("/driver/",summary="Retrieves driver details")
async def validate_driver(driver_req: driverRequest): #request: Request, api_key: APIKey = Depends(get_api_key)):
    """
    Endpoint to validate and fetch driver details for a given account.
    """
    start_time = time.process_time()  # Start the timer to measure processing time

    # Generate unique request ID and epoch_time
    request_id = str(uuid.uuid4())
    utc_time = datetime.datetime.now(timezone('UTC'))  
    epoch_time = int(time.mktime(utc_time.timetuple())) 

    # role = api_key.role 
    # x_hasura_user_id = api_key.x_hasura_user_id
    
    # Query Hasura for account details based on account number
    response_data = query_hasura(driver_req.account_number, start_time, request_id, epoch_time)

    # Calculate the time taken for processing the request
    elapsed_time = (time.process_time() - start_time) * 1000
    logging.info(f"Request successfully processed. Request ID: {request_id}, Time Taken: {elapsed_time:.4f} ms")
    logging.debug(f"Final response structure: {response_data}")

    # Return the successful response with account details
    return {
        "responseCode": 200,
        "timeTaken": f"{elapsed_time:.4f}",
        "responseData": response_data
    }

__all__ = ["app"]