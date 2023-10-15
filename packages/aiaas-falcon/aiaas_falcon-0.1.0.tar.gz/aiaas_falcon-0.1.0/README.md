
# AIaaS Falcon

## Description

A Python client to interact with a specific API, allowing operations such as listing models, creating embeddings, and generating text based on certain configurations.

## Installation

Ensure you have the `requests` and `google-api-core` libraries installed:

```bash
pip install requests
pip install google-api-core
```

## Usage

1. **Initialization:**

   ```python
   from falcon_client import Falcon  # Assuming the class is saved in a file named falcon_client.py
   
   falcon_client = Falcon(api_key="<Your_API_Key>", host_name_port="<Your_Host_Name_Port>")
   ```

2. **Listing Models:**

   ```python
   models = falcon_client.list_models()
   print(models)
   ```

3. **Creating an Embedding:**

   ```python
   response = falcon_client.create_embedding(file_path="<Your_File_Path>")
   print(response)
   ```

4. **Generating Text:**

   ```python
   response = falcon_client.generate_text(chat_history=[], query="<Your_Query>")
   print(response)
   ```

## Methods

- `list_models(self)` - Retrieves available models.
- `create_embedding(self, file_path)` - Creates embeddings from a provided file.
- `generate_text(self, chat_history=[], query="", use_default=1, conversation_config={}, config={})` - Generates text based on provided parameters.

## Conclusion

The Falcon API Client simplifies interactions with the specified API, providing a straightforward way to perform various operations such as listing models, creating embeddings, and generating text.
