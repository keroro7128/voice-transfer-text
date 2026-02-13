"""Keystroke injection engine for GhostWriter."""

from __future__ import annotations

import time
from typing import Any, Dict

import pyautogui
import pyperclip


def _is_ascii(text: str) -> bool:
    try:
        text.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False


def _inject_ascii(text: str) -> Dict[str, Any]:
    pyautogui.write(text, interval=0.01)
    return {"ok": True, "mode": "ascii", "text": text}


def _inject_clipboard(text: str) -> Dict[str, Any]:
    previous_clipboard = pyperclip.paste()
    try:
        pyperclip.copy(text)
        time.sleep(0.01)
        pyautogui.hotkey("ctrl", "v")
        return {"ok": True, "mode": "clipboard", "text": text}
    finally:
        pyperclip.copy(previous_clipboard)


def inject_text(text: str) -> Dict[str, Any]:
    """Inject text into active window and return structured result."""
    try:
        if not isinstance(text, str):
            return {"ok": False, "message": "Invalid text payload", "code": "INJECT_ERR"}
        if text == "":
            return {"ok": True, "mode": "noop", "text": ""}

        if _is_ascii(text):
            return _inject_ascii(text)
        return _inject_clipboard(text)
    except Exception as exc:  # pragma: no cover - hardware/system dependent
        return {
            "ok": False,
            "message": "注入失敗",
            "code": "INJECT_ERR",
            "detail": str(exc),
        }
