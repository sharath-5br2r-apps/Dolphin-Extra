#!/bin/sh

echo "Setup Discord rich presence"
for i in {0..9}; do
    test -S $XDG_RUNTIME_DIR/discord-ipc-$i ||
    ln -sf {app/com.discordapp.Discord,$XDG_RUNTIME_DIR}/discord-ipc-$i;
done

echo "Make directory /var/data/dolphin-emu/user/Wii if it doesn't exist"
mkdir -p /var/data/dolphin-emu/Wii

echo "Make directory /var/config/dolphin-emu if it doesn't exist"
mkdir -p /var/config/dolphin-emu

echo "Copy user directory to Flatpak user data directory"
cp -ru /app/share/dolphin-emu/user /var/data/dolphin-emu/

# Launch Dolphin and point it to the user directory
dolphin-emu -u /var/data/dolphin-emu/user "$@"
