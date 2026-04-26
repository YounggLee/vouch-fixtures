# vouch-fixtures

Test fixtures for [vouch](https://github.com/YounggLee/vouch) — a cmux-native AI diff reviewer.

This repo seeds 4 input modes:

| vouch mode | how to reproduce |
|---|---|
| **uncommitted** | `git apply pending.diff` then run `vouch` |
| **commit** | `vouch HEAD` on `feature/auth` branch (single commit) |
| **range** | `vouch main..feature/auth` |
| **pr** | `vouch --pr 1` (PR #1 is permanent fixture) |

## Layout

```
src/
  calc.py    # basic arithmetic
  store.py   # in-memory key-value store
  cli.py     # entry point
tests/
  test_calc.py
pending.diff  # patch for uncommitted mode test
```

## Don't merge PR #1

PR #1 (`feature/auth` → `main`) is intentionally kept open as a fixture for vouch's `--pr` mode. Do not merge or close.
