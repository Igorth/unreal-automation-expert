import unreal
import os
import time

start_time = time.time()

# Instances of unreal classes
editor_util = unreal.EditorUtilityLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

# Get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)

num_copies = 3
total_num_copies = num_assets * num_copies
text_label = "Duplicating Assets"
running = True

with unreal.ScopedSlowTask(total_num_copies, text_label) as slow_task:
    slow_task.make_dialog(True)

    # Iterate over the assets
    for asset in selected_assets:
        # Get the asset name and path to be duplicated
        asset_name = asset.get_fname()
        asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)
        source_path = os.path.dirname(asset_path)

        for i in range(num_copies):
            # If user pressed the cancel button
            if slow_task.should_cancel():
                running = False
                break

            new_name = f"{asset_name}_{i}"
            dest_path = os.path.join(source_path, new_name)
            duplicate = editor_asset_lib.duplicate_asset(asset_path, dest_path)
            slow_task.enter_progress_frame(1)

            if duplicate:
                unreal.log_warning(f"Duplicate from {source_path} at {dest_path} already exists.")
        if not running:
            break
    end_time = time.time()
    unreal.log(f"{num_assets} asset/s duplicated {num_assets} times in {end_time - start_time}.")
