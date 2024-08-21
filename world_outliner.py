import unreal

# Instances of Unreal Classes
editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

# Get all actors and filter down to specific elements
actors = editor_level_lib.get_all_level_actors()

static_meshes = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)
reflection_cap = editor_filter_lib.by_class(actors, unreal.ReflectionCapture)
blueprints = editor_filter_lib.by_id_name(actors, "BP_")

moved = 0

# Create a mapping between folder names and arrays
mapping = {
    "StatickMeshActors": static_meshes,
    "ReflectionCaptures": reflection_cap,
    "Blueprints": blueprints
}

for folder_name in mapping:
    for actor in mapping[folder_name]:
        actor_name = actor.get_fname()
        # actor.set_folder_path(folder_name)
        unreal.log(f"Moved {actor_name} to {folder_name}")

        moved += 1


unreal.log(f"Moved {moved} actors into respective folders.")
