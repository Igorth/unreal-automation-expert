import unreal
import math

# Instances of Unreal Classes
editor_util = unreal.EditorUtilityLibrary()

# Get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
not_powered = 0

# Iterate through each selected asset
for asset in selected_assets:
    asset_name = asset.get_name()
    asset_path = asset.get_path_name()
    x_size = asset.blueprint_get_size_x()
    y_size = asset.blueprint_get_size_y()

    # check if both values are power of two
    is_x_valid = math.log(x_size, 2).is_integer()
    is_y_valid = math.log(y_size, 2).is_integer()

    if not is_x_valid or not is_y_valid:
        unreal.log(f"{asset_name} is not a power of two ({x_size}, {y_size})")
        unreal.log(f"It's path is {asset_path}")
        not_powered += 1

unreal.log(f"{num_assets} checked, {not_powered} textures found problematic.")
