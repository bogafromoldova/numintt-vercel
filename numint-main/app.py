"""Vercel entrypoint: exposes the FastAPI web UI as a module-level `app`."""
import os
import pathlib
import sys

# Vercel's filesystem is read-only except /tmp: send cache/config there.
os.environ.setdefault("XDG_CACHE_HOME", "/tmp/.cache")
os.environ.setdefault("XDG_CONFIG_HOME", "/tmp/.config")

# Make the src/ layout importable without installing the package.
sys.path.insert(0, str(pathlib.Path(__file__).parent / "src"))

from numint.web.app import create_app  # noqa: E402

app = create_app()
