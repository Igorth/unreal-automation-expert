import unreal
import os

# Instances of Unreal Classes
editor_util = unreal.EditorUtilityLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

# Get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
removed = 0

# Instantly delete assets or move to Trash Folder
instant_delete = False
trash_folder = os.path.join(os.sep, "Game", "Trash")
to_be_deleted = []

# Iterate through each selected asset
for asset in selected_assets:
    asset_name = asset.get_fname()
    asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)

    # Get a list of references for this asset
    asset_references = editor_asset_lib.find_package_referencers_for_asset(asset_path)

    if len(asset_references) == 0:
        to_be_deleted.append(asset)

for asset in to_be_deleted:
    asset_name = asset.get_fname()

    # Instantly delete the asset
    if instant_delete:
        deleted = editor_asset_lib.delete_loaded_asset(asset)

        if not deleted:
            unreal.log_warning(f"Asset {asset_name} could not be deleted.")
            continue

        removed += 1
    # Move the assets to the trash folder
    else:
        new_path = os.path.join(trash_folder, str(asset_name))
        moved = editor_asset_lib.rename_loaded_asset(asset, new_path)

        if not moved:
            unreal.log_warning(f"Asset {asset_name} could not be moved to trash folder.")
            continue

        removed += 1

output_test = "removed" if instant_delete else "moved to trash folder"
unreal.log(f"{removed} of {len(to_be_deleted)} to be deleted assets, of {num_assets} selected, removed.")
