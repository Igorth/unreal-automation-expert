import unreal


def rename_assets(search_pattern, replace_pattern, use_case):
    # Instances of Unreal classes
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()

    # Get the selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0

    unreal.log(f"Selected {num_assets} assets")

    # Loop through each selected asset
    for asset in selected_assets:
        asset_name = system_lib.get_object_name(asset)

        # Check if the asset name contains a specific substring to be replaced
        if string_lib.contains(asset_name, search_pattern, use_case=use_case):
            search_case = unreal.SearchCase.CASE_SENSITIVE if use_case else unreal.SearchCase.IGNORE_CASE
            replaced_name = string_lib.replace(asset_name, search_pattern, replace_pattern, search_case)
            editor_util.rename_asset(asset, replaced_name)
            replaced += 1
            unreal.log(f"Renamed '{asset_name}' to '{replaced_name}'")
        else:
            unreal.log(f"No '{search_pattern}' found in '{asset_name}'")

    unreal.log(f"Replaced {replaced} of {num_assets} assets")


rename_assets("material", "Mat", True)

