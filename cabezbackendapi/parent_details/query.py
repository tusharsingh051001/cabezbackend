import requests
from config import get_hasura_endpoint, get_secret_key


def query_hasura(username: str, start_time, request_id, timestamp, role, x_hasura_user_id):
    """
    Queries Hasura for Parent details based on the provided account number.
    """
        # Define the GraphQL query to get Parent details
    query = """
        query getParentDetails($accountNumber: String!) {
                
        }
        """
        
    # Set the query variables
    variables = {"username": username}

    # Set the headers for the HTTP request, including the Hasura admin secret
    headers = {
            'x-hasura-admin-secret': get_secret_key(),
            'Content-Type': 'application/json'
        }

    # Make the POST request to Hasura
    response = requests.post(
            get_hasura_endpoint(),
            headers=headers,
            json={"query": query, "variables": variables},
            timeout=50,  #Timeout for the request
        )
        
    # Raise an HTTPError if one occurred during the request
    response.raise_for_status()

    # Parse the response as JSON
    response_json = response.json()
    return response_json
