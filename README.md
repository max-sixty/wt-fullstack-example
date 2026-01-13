# Worktrunk Full-Stack Example

Demonstrates worktrunk hooks for full-stack development:

- **Unique ports per worktree** — deterministic, no collisions
- **Auto-generated .env files** — with correct ports
- **Tmux 4-pane session** — shell, claude, backend, frontend
- **Conda activation** — in all panes
- **Clean removal** — stops servers, removes generated files

## Try It

```bash
wt switch --create -x 'tmux attach -t {{ branch | sanitize }}' feature/demo
```

Detach with `Ctrl-b d`. Remove with `wt remove feature/demo`.

## What You Get

```
+----------+----------+
|  shell   |  claude  |
+----------+----------+
| backend  | frontend |
+----------+----------+
```

Each pane has conda activated and `.env` sourced. Backend/frontend servers start automatically on unique ports.

## Prerequisites

- [Worktrunk](https://github.com/max-sixty/worktrunk) 0.13+ (for `--execute` templates)
- tmux
- micromamba or conda:

```bash
micromamba create -n wt-fullstack python=3.11 -y
```

## Customization

The config is ~60 lines. Key files:

- `.config/wt.toml` — hook definitions
- `scripts/pane-init.sh` — pane setup (conda, .env, clear)

To use real servers instead of `python -m http.server`, edit the `tmux send-keys` lines in `.config/wt.toml`:

```diff
 # Pane 1: Backend server
-tmux send-keys -t "$S:dev.1" 'source scripts/pane-init.sh && set -a && source .env.backend && set +a && cd backend && python -m http.server -b localhost $PORT' Enter
+tmux send-keys -t "$S:dev.1" 'source scripts/pane-init.sh && set -a && source .env.backend && set +a && cd backend && uvicorn main:app --port $PORT' Enter
 # Pane 3: Frontend server
-tmux send-keys -t "$S:dev.3" 'source scripts/pane-init.sh && set -a && source .env.frontend && set +a && cd frontend && python -m http.server -b localhost $PORT' Enter
+tmux send-keys -t "$S:dev.3" 'source scripts/pane-init.sh && set -a && source .env.frontend && set +a && cd frontend && npm run dev -- --port $PORT' Enter
```

Use `wt list` to see worktree URLs — bright means the port is listening.
