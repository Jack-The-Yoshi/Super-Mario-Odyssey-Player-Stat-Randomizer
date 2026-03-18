# Super Mario Odyssey Player Stat Randomizer

A tool for Super Mario Odyssey that randomizes Mario’s physics and movement values from `PlayerConst.byml`.

This tool allows you to create anything from slightly altered gameplay to extremely chaotic and unpredictable physics behavior.

---

## Features

- Randomizes player movement, gravity, jumps, and more
- Adjustable chaos level
- Seed system for reproducible results
- Advanced settings for additional control
- Standalone executable version available (no Python required)

---

## Download

Download the latest `.exe` from the Releases section.

---

## How to Use

### 1. Run the Tool

- Open the `.exe`
- Adjust the Randomization Strength
- Enter or generate a Seed
- Click "Randomize and Save"

---

### 2. Prepare the Output File

The tool will generate a file like:


PlayerConst_seed_XXXXXXXXX.byml


You must rename it to:


PlayerConst.byml


---

### 3. Install into the Game

1. Open Switch Toolbox

2. Navigate to your dumped game files:


ObjectData/


3. Locate this file:


PlayerActorHakoniwa.szs


4. Open `PlayerActorHakoniwa.szs` in Switch Toolbox

5. In the file tree, right-click:


PlayerActorHakoniwa.szs


6. Click:


Add File


7. Select your renamed file:


PlayerConst.byml


---

### 4. Save and Load

- Save the modified `.szs`
- Place it back into your mod/romfs folder
- Launch the game

---

## Result

Mario’s physics will now be randomized. This can result in a wide range of effects including altered movement, gravity changes, and unpredictable gameplay behavior.

---

## Notes

- Works best on Super Mario Odyssey Version 1.0.0
- High chaos levels may cause extreme or unstable gameplay
- Always keep backups of your original files before modifying them

---

## Permissions and Restrictions

- Redistribution of this tool is not allowed under any circumstances
- The creator is not responsible for any damage to the game, crashes, glitches, or other unintended effects caused by this tool

---

## Content Usage

You are allowed to create YouTube videos, livestreams (including Twitch or any other platform), or other content using this tool, provided that proper credit is given to:

Jack The Yoshi

---

## Credits

Created by Jack The Yoshi

---

## License

This project is provided for personal use only.
