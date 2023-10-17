# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from textwrap import dedent
from typing import List, Tuple


class GitConf:
    """Git Config."""

    branch_types: List[str] = ["feature", "bug", "hot"]

    # These branch names are not validated with this same rules
    # (permissions should be configured on the server if you want to prevent
    # pushing to any of these):
    branch_excepts: List[str] = [
        "feature",
        "dev",
        "main",
        "stable",
        # for quickly fixing critical issues, usually with a temporary solution.
        "hotfix",
        "bugfix",  # for fixing a bug
        "feature",  # for adding, removing or modifying a feature
        "test",  # for experimenting something which is not an issue
        "wip",  # for a work in progress
    ]

    regex_branch_types: str = "|".join(branch_types)

    regex_commit_msg: str = (
        r"(?P<prefix>\w+)(?:\((?P<topic>\w+)\))?: (?P<header>.+)"
    )

    commit_prefix: Tuple[Tuple[str, str, str]] = (
        ("feat", "Features", ":dart:"),  # 🎯, 📋 :clipboard:
        ("hotfix", "Fix Bugs", ":fire:"),  # 🔥
        ("fixed", "Fix Bugs", ":gear:"),  # ⚙️, 🛠️ :hammer_and_wrench:
        ("fix", "Fix Bugs", ":gear:"),  # ⚙️, 🛠️ :hammer_and_wrench:
        ("docs", "Documents", ":page_facing_up:"),  # 📄, 📑 :bookmark_tabs:
        ("styled", "Code Changes", ":art:"),  # 🎨, 📝 :memo:, ✒️ :black_nib:
        ("style", "Code Changes", ":art:"),  # 🎨, 📝 :memo:, ✒️ :black_nib:
        ("refactored", "Code Changes", ":construction:"),
        # 🚧, 💬 :speech_balloon:
        ("refactor", "Code Changes", ":construction:"),
        # 🚧, 💬 :speech_balloon:
        ("perf", "Code Changes", ":chart_with_upwards_trend:"),
        # 📈, ⌛ :hourglass:
        ("tests", "Code Changes", ":test_tube:"),  # 🧪, ⚗️ :alembic:
        ("test", "Code Changes", ":test_tube:"),  # 🧪, ⚗️ :alembic:
        ("build", "Build & Workflow", ":toolbox:"),  # 🧰, 📦 :package:
        ("workflow", "Build & Workflow", ":rocket:"),  # 🚀, 🕹️ :joystick:
    )

    commit_prefix_group: Tuple[Tuple[str, str]] = (
        ("Features", ":clipboard:"),  # 📋
        ("Code Changes", ":black_nib:"),  # ✒️
        ("Documents", ":bookmark_tabs:"),  # 📑
        ("Fix Bugs", ":hammer_and_wrench:"),  # 🛠️
        ("Build & Workflow", ":package:"),  # 📦
    )


class BumpVerConf:
    """Bump Version Config."""

    main: str = dedent(
        r"""
    [bumpversion]
    current_version = {version}
    commit = True
    tag = False
    parse = ^
        {regex}
    serialize =
        {{major}}.{{minor}}.{{patch}}.{{prekind}}{{pre}}.{{postkind}}{{post}}
        {{major}}.{{minor}}.{{patch}}.{{prekind}}{{pre}}
        {{major}}.{{minor}}.{{patch}}.{{postkind}}{{post}}
        {{major}}.{{minor}}.{{patch}}
    message = {msg}

    [bumpversion:part:prekind]
    optional_value = _
    values =
        _
        a
        b
        rc

    [bumpversion:part:postkind]
    optional_value = _
    values =
        _
        post

    [bumpversion:file:{file}]
    """
    ).strip()

    msg: str = (
        ":bookmark: Bump up to version {{current_version}} -> {{new_version}}."
    )

    regex: str = (
        r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"
        r"(\.(?P<prekind>a|alpha|b|beta|d|dev|rc)(?P<pre>\d+))?"
        r"(\.(?P<postkind>post)(?P<post>\d+))?"
    )

    v1: str = dedent(
        r"""
    {main}

    [bumpversion:file:{changelog}]
    search = {{#}}{{#}} Latest Changes
    replace = {{#}}{{#}} Latest Changes

        {{#}}{{#}} {{new_version}}
    """
    ).strip()

    v2: str = dedent(
        r"""
    {main}

    [bumpversion:file:{changelog}]
    search = {{#}}{{#}} Latest Changes
    replace = {{#}}{{#}} Latest Changes

        {{#}}{{#}} {{new_version}}

        Released: {{utcnow:%Y-%m-%d}}
    """
    ).strip()
