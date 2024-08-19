import unreal


# Instances of Unreal Classes
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()

# Get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
prefixed = 0

# Iterate through each selected asset
for asset in selected_assets:
    # Get the class instance and the clear text name
    asset_name = asset.get_fname()
    class_instance = asset.get_class()
    class_name = system_lib.get_class_display_name(class_instance)

    unreal.log(f"Asset Name: {asset_name}, Class Name: {class_name}")
