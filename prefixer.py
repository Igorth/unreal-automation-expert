import unreal
import json

# Instances of Unreal Classes
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()

# Prefix mapping
prefix_mapping = {}

# Load the prefix mapping from a JSON file
with open("prefix_mapping.json", "r") as json_file:
    prefix_mapping = json.loads(json_file.read())

# Get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
prefixed = 0

# Iterate through each selected asset
for asset in selected_assets:
    # Get the class instance and the clear text name
    asset_name = system_lib.get_object_name(asset)
    class_instance = asset.get_class()
    class_name = system_lib.get_class_display_name(class_instance)

    # Get the prefix for the given class
    class_prefix = prefix_mapping.get(class_name, None)

    if class_prefix is None:
        unreal.log_warning(f"No mapping for asset {asset_name} of type {class_name}")
        continue

    if not asset_name.startswith(class_prefix):
        # Rename the asset and add prefix
        new_name = class_prefix + asset_name
        editor_util.rename_asset(asset, new_name)
        prefixed += 1
        unreal.log(f"Prefixed {asset_name} of type {class_name} with {class_prefix}.. ")
    else:
        unreal.log(f"Asset {asset_name} of type {class_name} already has prefix {class_prefix}. No changes made.")

unreal.log(f"Prefixed {prefixed} of {num_assets} assets.")
