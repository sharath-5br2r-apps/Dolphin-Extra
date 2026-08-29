## Dolphin Extra
Dolphin Extra incorporates aspects of [DolphinCS](https://github.com/JoeysRetroHandhelds/DolphinCS) and [Better Wii Menu DE](https://github.com/Gavin-S-Dev/Better-Wii-Menu-DE) but instead syncs to pull requests. All branding is removed and the apk is optionally spoofed to Game for Peace`com.tencent.tmgp.pubgmhd`  for performance.
Additionally Linux and Windows builds of Dolphin Extra is also available.
Better Wii Menu DE is also ported to Android using AI to replicate the behaviour in Qt UI.

## Releases

Releases are built here automatically whenever Dolphin merges a PR into master. This fork
tracks upstream Dolphin's PR in form of virtual tags, not commits or release tags. See
[Releases page](../../releases) for builds. It is also visible in my [catalog](https://sharath-5br2r.github.io/catalog) of all projects
with more clarity and Obtainium Instructions for Android.

## Original Readmes

<details>
<summary>DolphinCS</summary>
DolphinCS is an unofficial fork of [Dolphin](https://github.com/dolphin-emu/dolphin), the
GameCube/Wii emulator. It is **not affiliated with the Dolphin Emulator project**.

The only thing this fork changes is **where Dolphin stores its user data on Android**. Everything
else is identical to upstream Dolphin.

## What's different

A settings toggle lets you choose where Dolphin's user data (settings, saves, game paths, etc.)
lives:

- **Scoped Storage** (default, same as official Dolphin)
- **Internal Storage** (`/sdcard/dolphin-emu`)
- **SD Card**, if a removable card is detected

Switching locations offers to migrate your existing data to the new location automatically.

Nothing else is added, removed, or changed.

## Releases

Releases here are built automatically whenever Dolphin publishes a new stable release. This fork
tracks upstream Dolphin's release tags, not individual commits or dev builds. See the
[Releases page](https://github.com/JoeysRetroHandhelds/DolphinCS/releases) for builds.

## License

DolphinCS is licensed under the GNU GPL version 2 (or any later version), same as upstream
Dolphin. See [COPYING](COPYING) for the full license text.

</details>

<details>
<summary>Better Wii Menu - For Dolphin Emulator</summary>

A custom Dolphin build that lets disc image files (.rvz, .iso, .wbfs, .gcz, .ciso, .wia) work as channels on the Wii System Menu.

Switching between games has never been easier!
### Features

- Automatically syncs users' Dolphin game library with the Wii Menu

- Switching between games is now possible with only the Wii Remote

- Right-click or Hold(Android) any game in the Dolphin menu to manually add/remove games from the Wii Menu

- Visually replicates the same experiences as if game files are .wad in Wii Menu

### How to use

#### Desktop

1. Extract the zip
2. Run `BetterWiiMenuDE.exe`
3. Load up the Wii Menu or head straight into a game and enjoy easier game switching!

#### Android

1. Install the APK
2. Open Dolphin
3. Load up the Wii Menu or head straight into a game and enjoy easier game switching!

</details>
