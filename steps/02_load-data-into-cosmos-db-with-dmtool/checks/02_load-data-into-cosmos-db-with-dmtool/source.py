import logging
from urllib import response
from azure.identity import ClientSecretCredential
from azure.mgmt.cosmosdb import CosmosDBManagementClient
from azure.cosmos import CosmosClient

def handler(event, context):
    try:        
        credentials, subscription_id = get_credentials(event)
        url = event['environment_params']['url']
        database_name = event['environment_params']['database_name']
        container_name = event['environment_params']['container_name']
        resource_group_name = event['environment_params']['resource_group_name']    
        account_name = event['environment_params']['account_name']    
        query = event['environment_params']['query']
        item_count = event['environment_params']['item_count']
        cosmos_mgmt_client = CosmosDBManagementClient(credentials, subscription_id)
        keys = cosmos_mgmt_client.database_accounts.list_keys(resource_group_name, account_name).as_dict()
        cosmos_client = CosmosClient(url, {'masterKey': keys['primary_readonly_master_key']})
        db_list = cosmos_client.list_databases()
        for db in db_list:
            if (db['id'] == database_name):                
                db_client = cosmos_client.get_database_client(db['id'])
                container_list = db_client.list_containers()
                for container in container_list:
                    if (container['id'] == container_name):
                        container_client = db_client.get_container_client(container_name)
                        response = list(container_client.query_items(query, enable_cross_partition_query=True))                    
                        if (response[0] >= item_count):
                            return True
        return False
    except Exception as e:
        logging.error(e)
        return False

def get_credentials(event):
    subscription_id = event['environment_params']['subscription_id']
    credentials = ClientSecretCredential(
        client_id=event['credentials']['credential_id'],
        client_secret=event['credentials']['credential_key'],
        tenant_id=event['environment_params']['tenant']
    )
    return credentials, subscription_id