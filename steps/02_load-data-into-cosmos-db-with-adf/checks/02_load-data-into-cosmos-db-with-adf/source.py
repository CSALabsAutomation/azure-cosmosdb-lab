
from azure.identity import ClientSecretCredential
from azure.mgmt.loganalytics import LogAnalyticsManagementClient
from azure.mgmt.monitor import MonitorManagementClient

def handler(event, context):
    credentials, subscription_id = get_credentials(event)
    resource_group = event['environment_params']['resource_group']
    la_client = LogAnalyticsManagementClient(credentials, subscription_id)
    mon_client = MonitorManagementClient(credentials, subscription_id)

    try:
        list_monitors = list(la_client.workspaces.list_by_resource_group(resource_group))
        if list_monitors and any(list_monitors):
            diag_settings = list(mon_client.diagnostic_settings.list(list_monitors[0].id))
            if diag_settings and any(diag_settings):
                collection_type = ""
                for i in diag_settings[0].logs:
                    collection_type = collection_type + i.category_group + ", "
                
                if "audit" in collection_type and "allLogs" in collection_type:
                    return True
                return False
            return False
        return False
    except:
        return False

def get_credentials(event):
    subscription_id = event['environment_params']['subscription_id']
    credentials = ClientSecretCredential(
        client_id=event['credentials']['credential_id'],
        client_secret=event['credentials']['credential_key'],
        tenant_id=event['environment_params']['tenant']
    )
    return credentials, subscription_id
