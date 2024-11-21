# README

## Azure Blob Storage AzCopy Command Generator

This script lists all `.zip` files in an Azure Blob Storage container and generates AzCopy commands to download each file to a local directory.

---

## Prerequisites

1. **Python Environment**: Ensure you have Python installed on your system.
2. **Azure Blob Storage Account**: You need access to an Azure Blob Storage account with:
   - The **Account Name**
   - A **SAS Token** (Shared Access Signature) to access the container.
   - The **Container Name** where the blobs are stored.
3. **AzCopy**: Install the [AzCopy tool](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) to download blobs from Azure Storage.

---

## Setup

1. Install the required Python library:
   ```bash
   pip install azure-storage-blob
   ```

2. Replace the placeholder values in the script:
   - `account_name`: Your Azure Storage account name.
   - `sas_token`: The SAS token for accessing the container.
   - `container_name`: The name of the container holding your blobs.

---

## How It Works

1. **Connect to Azure Blob Storage**:  
   The script uses the `BlobServiceClient` class to connect to your Azure Storage account via the provided SAS URL.

2. **List `.zip` Files**:  
   It filters and lists all blobs ending with `.zip` in the specified container.

3. **Generate AzCopy Commands**:  
   For each `.zip` file, the script generates a command in the following format:
   ```bash
   azcopy copy "<source_blob_url_with_sas>" "<destination_path>"
   ```
   The destination path defaults to `C:\Downloads\<blob_name>`.

4. **Output Commands**:  
   The generated AzCopy commands are printed to the console, ready to be executed.

---

## Example Output

For example, if the container contains the blobs:
- `file1.zip`
- `file2.zip`

The script will output:
```plaintext
AzCopy commands to download each blob:
azcopy copy "https://your_account_name.blob.core.windows.net/your_container_name/file1.zip?your_sas_token" "C:\Downloads\file1.zip"
azcopy copy "https://your_account_name.blob.core.windows.net/your_container_name/file2.zip?your_sas_token" "C:\Downloads\file2.zip"
```

---

## Usage

1. Run the script:
   ```bash
   python generate_azcopy_commands.py
   ```

2. Copy the generated AzCopy commands from the console output.

3. Execute the AzCopy commands to download the `.zip` files to your local directory:
   ```bash
   azcopy copy "<source_blob_url_with_sas>" "<destination_path>"
   ```

---

## Error Handling

If an error occurs (e.g., invalid credentials or network issues), the script will output an error message indicating the problem.

---

## License

This script is provided "as is" without warranty of any kind. Use it at your own risk.
