from azure.storage.blob import BlobServiceClient

# Replace with your actual values
account_name = "your_account_name"
sas_token = "your_sas_token"
container_name = "your_container_name"

# Create a BlobServiceClient using the SAS URL
blob_service_client = BlobServiceClient(
    account_url=f"https://{account_name}.blob.core.windows.net/?{sas_token}"
)

try:
    # Get a container client
    container_client = blob_service_client.get_container_client(container_name)

    # List all blobs in the container
    blob_list = container_client.list_blobs()

    # Generate AzCopy commands for each blob
    print("AzCopy commands to download each blob:")
    for blob in blob_list:
        if blob.name.endswith('.zip'):
            azcopy_command = f'azcopy copy "https://{account_name}.blob.core.windows.net/{container_name}/{blob.name}?{sas_token}" "C:\\Downloads\\{blob.name}"'
            print(azcopy_command)

except Exception as e:
    print(f"An error occurred: {e}")
