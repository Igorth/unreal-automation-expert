import unreal

# Instances of Unreal Classes
editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

# Get all level actors and filter by StaticMeschActor
level_actors = editor_level_lib.get_all_level_actors()
static_mesh_actors = editor_filter_lib.by_class(level_actors, unreal.StaticMeshActor)
deleted = 0

for actor in static_mesh_actors:
    actor_name = actor.get_fname()

    # Get the static mesh component
    actor_mesh_comp = actor.static_mesh_component
    actor_mesh = actor_mesh_comp.static_mesh
    is_valid_actor = actor_mesh != None

    # if mesh not valid, destroy
    if not is_valid_actor:
        actor.destroy_actor()
        deleted += 1
        unreal.log(f"The Mesh Component of Actor {actor_name} is invalid and was deleted")

unreal.log(f"Deleted {deleted} Actors with invalid Mesh Component")
