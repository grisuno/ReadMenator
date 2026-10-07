#!/usr/bin/env python3
"""Launcher shim that runs the readmenator CLI from a source checkout."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from readmenator.__main__ import main

main()
