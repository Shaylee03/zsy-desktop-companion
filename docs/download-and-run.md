# Moqi for Windows

## Product Form

The desktop product is a packaged Windows application with a system tray and a dedicated control center. It does not require users to launch Codex, PowerShell, or a system Python environment.

The control center includes:

- Home: local, cloud, and robot health; current presence mode; latest safe understanding.
- Understanding: 7-day rhythm timeline and semantic understanding.
- Privacy & Data: visual consent, excluded apps, retention, pause, and deletion.
- Device: pairing, connection test, local data path, and diagnostics.

## Packaging

The implementation uses `pystray`, `pywebview`, PyInstaller `onedir/windowed`, and an Inno Setup installer. A Windows scheduled task launches `Moqi.exe --background` at login with one-minute restart recovery and a single-instance mutex.

```text
Moqi Setup.exe
  -> %LOCALAPPDATA%\Programs\Moqi\Moqi.exe
  -> Windows scheduled task: Moqi
  -> %LOCALAPPDATA%\Moqi\config.json
  -> %LOCALAPPDATA%\Moqi\moqi.sqlite3
  -> %LOCALAPPDATA%\Moqi\logs\
```

## Connection Flow

```text
One-time pairing code
  -> POST /api/v1/pair/claim
  -> installation credential
  -> POST /api/v1/desktop/context
  -> Moqi Cloud policy
  -> compatible robot command
  -> robot feedback
```

ActivityWatch is optional. Native foreground, input rhythm, AFK, and local SQLite tracking continue when ActivityWatch is absent or the cloud is offline.

## Development Compatibility

The earlier `Start-ZSY-Desktop-Agent.ps1` and `Stop-ZSY-Desktop-Agent.ps1` scripts remain available as development-only compatibility tools while the packaged app becomes the default product entry.
