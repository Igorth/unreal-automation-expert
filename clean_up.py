import unreal
import os

# Instances of Unreal classes
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

# Get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
cleaned = 0

# Hard code parent path
parent_dir = "\\Game\\Python"

if num_assets > 0:
    asset_path = editor_asset_lib.get_path_name_for_loaded_asset(selected_assets[0])
    parent_dir = os.path.dirname(asset_path)

# Iterate through each selected asset
for asset in selected_assets:
    # Get the class instance and the clear text name
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    # Define new_path before
    new_path = ""

    # Assemble new path and relocate assets
    try:
        new_path = os.path.join(parent_dir, class_name, asset_name)
        editor_asset_lib.rename_loaded_asset(asset, new_path)
        cleaned += 1
        unreal.log(f"Cleaned {asset_name} to {new_path}")
    except (RuntimeError, ValueError) as err:
        unreal.log_warning(f"Could not move {asset_name} to new location {new_path} due to: {err}")
    except Exception as err:
        unreal.log_error(f"Unexpected error occurred while moving {asset_name} to new location {new_path}: {err} ")


unreal.log(f"Cleaned up {cleaned} of {num_assets} assets.")

