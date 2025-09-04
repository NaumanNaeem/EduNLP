import os
from huggingface_hub import HfApi, upload_folder

token = os.environ["HF_TOKEN"]        # from GitHub secret
space_id = os.environ["SPACE_ID"]     # from GitHub secret (username/space-name)
sid = os.environ["SPACE_ID"]
api = HfApi(token=token)
info = api.whoami()
print("Authenticated as:", info.get("name"))
print("Deploying to SPACE_ID:", sid)
# Ensure the Space exists and is Static
api.create_repo(repo_id=space_id, repo_type="space", exist_ok=True, space_sdk="static")

# Upload the compiled site (_site) to the root of the Space
upload_folder(
    repo_id=space_id,
    repo_type="space",
    folder_path="_site",
    path_in_repo="",
    token=token,
    commit_message="CI: Deploy Jekyll _site"
)