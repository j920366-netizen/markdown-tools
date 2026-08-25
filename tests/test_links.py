import pytest

from markdown_tools.links import extract_links, find_broken_links


def test_extract_links_returns_label_and_url():
    md = "See [docs](https://example.com/docs) for details."
    assert extract_links(md) == [("docs", "https://example.com/docs")]


def test_extract_links_ignores_plain_text():
    assert extract_links("no links here") == []


def test_find_broken_links_filters_available_targets():
    md = "[a](https://a.dev) [b](https://b.dev)"
    broken = find_broken_links(md, available={"https://a.dev"})
    assert broken == [("b", "https://b.dev")]
