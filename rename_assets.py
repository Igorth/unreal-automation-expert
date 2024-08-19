import unreal


def rename_assets():
    # Instances of Unreal classes
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()

    # Get the selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0

    unreal.log(f"Selected {num_assets} assets")


rename_assets()

