# Unreal Engine Asset Management Scripts
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Unreal Engine](https://img.shields.io/badge/Unreal%20Engine-5.x-blue.svg)

This repository contains Python scripts designed for managing assets in Unreal Engine. The scripts cover a range of tasks including renaming, organizing, and cleaning up assets to streamline the development process.

## Scripts

- **rename_assets.py**: Renames assets based on a search pattern.
- **power_of_two.py**: Ensures texture sizes are a power of 2 (e.g., 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, or 2048). [More info on power of two](https://dev.epicgames.com/documentation/en-us/uefn/resizing-textures-in-unreal-editor-for-fortnite).
- **prefixer.py**: Adds a prefix to asset names.
- **clean_up.py**: Organizes assets into separate folders based on their asset class.
- **duplicator.py**: Duplicates assets.
- **removed_unused.py**: Removes unused assets.
- **world_outliner.py**: Organizes actors in the world into folders.
- **delete_static_mesh.py**: Deletes invalid (None) static mesh components.
- **set_linear_color_tex.py**: Configures texture parameter settings.
- **delete_empty_folders.py**: Deletes empty folders.
- **actor_action_util.py**: Sets a material for a static mesh actor.

## Usage

To use these scripts, ensure you have the Unreal Engine Python API set up and configured. You can run each script individually from the command line, or integrate them into your development workflow.

## Getting Started

1. **Clone the repository:**
```commandline
git clone https://github.com/Igorth/unreal-automation-expert
```
2. Navigate to the scripts directory:
```commandline
cd unreal-automation-expert
```

3. Run a script:
```commandline
python <script_name>.py
```

## Acknowledgments
This course was completed on [Udemy](https://www.udemy.com/course/becoming-an-unreal-automation-expert/?campaigntype=Search&portfolio=Canada&language=EN&product=Course&test=&audience=DSA&topic=&priority=Beta&matchtype=&gad_source=1&couponCode=SKILLS4SALEA), focusing on Python and Unreal Engine integration.
