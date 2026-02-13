# Gemini Project Memory

## Project: GhostWriter (Mobile Input Bridge)

### Current State
- **Core Connection**: WebSocket (sio4lite) stable.
- **Phase 1**: Stream-based text injection working.
- **Phase 2**: Context Awareness (Current App Name & Caret Context) UI/Logic implemented.
- **UI/UX**: Dark mode theme with glassmorphism (style.css).

### Tech Notes
- **Server**: Python backend (server.py) with keyboard/win32 interaction (injector.py).
- **Frontend**: Vanilla JS, Socket.IO (lite version).
- **Diagnostics**: Compatibility warnings for `theme-color` and `autocapitalize` are expected; handled via `color-scheme` fallback and mobile-first prioritization.

### Critical Rules
- **Perfectionist Mode**: Active.
- **Data Integrity**: Absolute priority.
- **Checklist**: Maintained at local root.
