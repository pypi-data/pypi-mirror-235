from __future__ import annotations

import shutil
import pathlib
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class BuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        NOT_COMPONENT = [
            "app",
            "node_modules",
            "storybook",
            "playwright-report",
            "workbench",
            "tooltils",
        ]
        for entry in (pathlib.Path(self.root) / "js").iterdir():
            if (
                entry.is_dir()
                and not str(entry.name).startswith("_")
                and not str(entry.name) in NOT_COMPONENT
            ):
                shutil.copytree(
                    str(entry),
                    str(pathlib.Path("gradio") / "_frontend_code" / entry.name),
                    ignore=lambda d, names: ["node_modules"],
                    dirs_exist_ok=True,
                )
        shutil.copytree(
            str(pathlib.Path(self.root) / "client" / "js"),
            str(pathlib.Path("gradio") / "_frontend_code" / "client"),
            ignore=lambda d, names: ["node_modules"],
            dirs_exist_ok=True,
        )
