# Worktrunk Full-Stack Example

This repo demonstrates a comprehensive worktrunk configuration for full-stack development with:

1. **Unique ports per worktree** — Backend and frontend get deterministic ports based on branch name
2. **Auto-generated .env files** — Environment files are generated with correct port numbers
3. **Tmux session per worktree** — 4-pane layout: shell, claude, backend, frontend
4. **Clean removal** — Generated files are cleaned up when removing worktrees

## Quick Start

```bash
# Create a new worktree for your feature
wt switch feature/my-feature --create

# A tmux session was created in the background
# Attach to it:
tmux attach -t feature-my-feature

# When done, remove the worktree
# This will clean up generated files and kill the tmux session
wt remove feature/my-feature
```

## What Happens on `wt switch --create`

1. **post-create** hooks run (blocking):
   - `.env`, `.env.backend`, `.env.frontend` are generated with unique ports

2. **post-start** hooks run (background):
   - A tmux session is created with 4 panes

## Tmux Session Layout

```
+----------+----------+
|  shell   |  claude  |
+----------+----------+
| backend  | frontend |
+----------+----------+
```

Each pane is:
- Set to the worktree directory
- Ready for you to start commands
- Can be configured to auto-start servers (see `.config/wt.toml`)

## Port Allocation

Ports are deterministic based on branch name using `hash_port`:

| Branch | Backend Port | Frontend Port |
|--------|--------------|---------------|
| main   | (default: 8000) | (default: 3000) |
| feature/auth | ~12XXX | ~15XXX |
| feature/api  | ~11XXX | ~14XXX |

The exact port depends on the hash, but it's stable — the same branch always gets the same ports.

## Conda Integration

To activate a conda environment in each tmux pane, uncomment the `conda activate` lines in `.config/wt.toml`.

Note: The conda activation happens *inside* tmux, not in your calling shell. This is because:
- post-start hooks run in a background subprocess
- They cannot modify the parent shell's environment
- The tmux session is independent and can have its own environment

## Customization

Edit `.config/wt.toml` to:
- Change the tmux layout
- Add conda activation
- Auto-start backend/frontend servers
- Add database setup
- Customize cleanup behavior
