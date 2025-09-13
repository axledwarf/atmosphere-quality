#!/usr/bin/bash

# Path to your script
SCRIPT_PATH="/home/fooboo/scripts/particle_logger_the_second"
VENV_PATH="$HOME/.virtualenvs/pimoroni/bin/activate"
LOG_PATH="/home/fooboo/Logs/particle_monitor.log"

# Check if the script is running
if ! pgrep -f "$SCRIPT_PATH" > /dev/null; then
    echo "$(date): Script not running. Restarting..." >> "$LOG_PATH"
    source "$VENV_PATH"
    nohup python3 "$SCRIPT_PATH" >> "$LOG_PATH" 2>&1 &
else
    echo "$(date): Script is running." >> "$LOG_PATH"
fi
