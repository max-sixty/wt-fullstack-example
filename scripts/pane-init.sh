#!/bin/bash
# Initialize a tmux pane: activate conda, source .env, clear screen

# Activate conda env (assumes shell integration already set up)
micromamba activate wt-fullstack 2>/dev/null || conda activate wt-fullstack 2>/dev/null || true

# Export environment variables
set -a
source .env 2>/dev/null
set +a

clear
