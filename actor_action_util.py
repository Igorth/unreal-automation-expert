import unreal

# Instances of unreal classes
editor_util = unreal.EditorUtilityLibrary()
layer_sis = unreal.LayersSubsystem()
editor_filter_lib = unreal.EditorFilterLibrary()

# Get the selected material and selected static mesh actors
selected_assets = editor_util.get_selected_assets()
materials = editor_filter_lib.by_class(selected_assets, unreal.Material)

if len(materials) < 1:
    unreal.log_warning("Please select a material to be assigned")
else:
    material = materials[0]
    material_name = material.get_fname()
    unreal.log(f"Assigning material '{material_name}' to selected static meshes")

    actors = layer_sis.get_selected_actors()
    static_mesh_actors = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)

    for actor in static_mesh_actors:
        actor_name = actor.get_fname()

        # Get the static mesh component and assign the material
        actor_mesh_component = actor.static_mesh_component
        actor_mesh_component.set_material(0, material)

        unreal.log(f"Assigning material '{material_name}' to actor {actor_name}")
