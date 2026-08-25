"""Utilities for extracting and validating links in Markdown documents."""

import re

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^\s)]+)\)")


def extract_links(markdown: str) -> list[tuple[str, str]]:
    """Return a list of (label, url) pairs found in the markdown text."""
    return [(label, url) for label, url in LINK_RE.findall(markdown)]


def find_broken_links(markdown: str, available: set[str]) -> list[tuple[str, str]]:
    """Return links whose target is not present in ``available``."""
    return [(label, url) for label, url in extract_links(markdown) if url not in available]
