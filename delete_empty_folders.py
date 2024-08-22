import unreal

# Instances of Unreal classes
editor_asset_lib = unreal.EditorAssetLibrary()

# Set source dir and options
source_dir = "/Game/Python"
include_subfolders = True
deleted = 0

# Get all assets in source dir
assets = editor_asset_lib.list_assets(source_dir, recursive=include_subfolders, include_folder=True)
folders = [asset for asset in assets if editor_asset_lib.does_directory_exist(asset)]


for folder in folders:
    # Check if folder has assets
    has_assets = editor_asset_lib.does_directory_have_assets(folder)

    if not has_assets:
        # Delete folder
        editor_asset_lib.delete_directory(folder)
        deleted += 1
        unreal.log(f"Folder {folder} without assets was deleted.")


unreal.log(f"Deleted {deleted} folders without assets.")
