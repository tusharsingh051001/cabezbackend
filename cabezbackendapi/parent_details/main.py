from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
import time
import datetime
import logging
from pytz import timezone
import uuid
from parent_details.query import query_hasura
from config import get_hasura_endpoint, get_secret_key

app = FastAPI()

class ParentRequest(BaseModel):
    """
    Request model for Parent details.
    """
    username: str

@app.post("/Parent/",summary="Retrieves Parent details")
async def validate_Parent(Parent_req: ParentRequest): #request: Request, api_key: APIKey = Depends(get_api_key)):
    """
    Endpoint to validate and fetch Parent details for a given account.
    """
    start_time = time.process_time()  # Start the timer to measure processing time

    # Generate unique request ID and epoch_time
    request_id = str(uuid.uuid4())
    utc_time = datetime.datetime.now(timezone('UTC'))  # Get current UTC time
    epoch_time = int(time.mktime(utc_time.timetuple()))  # Convert time to epoch format

    # role = api_key.role 
    # x_hasura_user_id = api_key.x_hasura_user_id
    
    # Query Hasura for account details based on account number
    response_data = query_hasura(Parent_req.account_number, start_time, request_id, epoch_time)

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