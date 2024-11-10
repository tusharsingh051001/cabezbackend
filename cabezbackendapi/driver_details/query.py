import requests
from config import get_hasura_endpoint


def query_hasura(username: str, start_time, request_id, timestamp):
    """
    Queries Hasura for driver details based on the provided account number.
    """
        # Define the GraphQL query to get driver details
    query = """
        query getDriverDetails($username: String!) {
            driver_details(where: {username: {_eq: $username}}) {
                account_expiry_date
                account_start_date
                blood_group
                email_id
                identification_type
                name
                password
                phone_number
                riders
                salary_amount
                username
                rider_details {
                drop_address
                pickup_address
                blood_group
                name
                email_id
                phone_number
                }
            }
        }
        """
        
    # Set the query variables
    variables = {"username": username}

    # Set the headers for the HTTP request, including the Hasura admin secret
    headers = {
            # 'x-hasura-admin-secret': get_secret_key(),
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
