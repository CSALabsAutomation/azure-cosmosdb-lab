
## Log-in to the Azure Portal

1. In a new window, sign in to the **Azure Portal** (<https://portal.azure.com>).

1. Once you have logged in, you may be prompted to start a tour of the Azure portal. You can safely skip this step.

### Retrieve Account Credentials

The .NET SDK requires credentials to connect to your Azure Cosmos DB account. You will collect and store these credentials for use throughout the lab.

1. On the left side of the portal, select the **Resource groups** link.

   ![Resource groups is highlighted](./assets/02-resource_groups.jpg "Select resource groups")

1. In the **Resource groups** blade, locate and select the **cosmoslabs** _Resource Group_.

   ![The recently cosmosdb resource group is highlighted](../assets/02-lab_resource_group.jpg "Select the CosmosDB resource group")

1. In the **cosmoslabs** blade, select the **Azure Cosmos DB** account you recently created.

   ![The Cosmos DB resource is highlighted](../assets/02-cosmos_resource.jpg "Select the Cosmos DB resource")

1. In the **Azure Cosmos DB** blade, locate the **Settings** section and select the **Keys** link.

   ![The Keys pane is highlighted](../assets/02-keys_pane.jpg "Select the Keys Pane")

1. In the **Keys** pane, record the values in the **CONNECTION STRING**, **URI** and **PRIMARY KEY** fields. You will use these values later in this lab.

   ![The URI, Primary Key and Connection string credentials are highlighted](../assets/02-keys.jpg "Copy the URI, primary key and the connection string")
