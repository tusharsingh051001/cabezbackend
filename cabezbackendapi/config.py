HASURA_ENDPOINT = "https://apiengine.dataapi.ncb.vn"
SECRET_KEY= "f9V9&T2%0d$9E1*T"

ADMIN_API_KEY= "admin"
DATABASE_URL= "postgresql://postgres:postgres@10.222.1.26:5432/ncbdataapimetadata"

def get_hasura_endpoint():
    hasura_endpoint = HASURA_ENDPOINT + "/v1/graphql"
    return hasura_endpoint

def get_secret_key():
    return SECRET_KEY
