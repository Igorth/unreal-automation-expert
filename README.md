# Unreal Automation Expert

### Observation


Each object in Unreal inherits from the Object Base [unreal._ObjectBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/python-api/class/_ObjectBase?highlight=_objectbase&application_version=5.0)

## Repository Structure
- **rename_assets.py**: Rename assets based on search pattern
- **power_of_two.py**: Texture sizes need to be a power of 2
(for example, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, or 2048) [Power of two](https://dev.epicgames.com/documentation/en-us/uefn/resizing-textures-in-unreal-editor-for-fortnite).
- **prefixer.py**: Add a prefix in the assets
- **clean_up.py**: Put the assets in separate folders following the asset class name
- **duplicator.py**: Duplicate assets
- **removed_unused.py**: Remove unused assets