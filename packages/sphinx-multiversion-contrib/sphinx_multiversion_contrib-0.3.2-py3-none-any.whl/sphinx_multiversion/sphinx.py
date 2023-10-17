# -*- coding: utf-8 -*-
"""Helper functions for working with sphinx"""

from collections import namedtuple
from collections.abc import Iterator
import datetime
import json
import logging
import os
import posixpath
from typing import Any, Union

from sphinx.addnodes import document as sphinx_doc
from sphinx.application import Sphinx as sphinx_app
from sphinx.config import Config as sphinx_config
from sphinx.locale import _
from sphinx.util import i18n as sphinx_i18n

logger = logging.getLogger(__name__)

DATE_FMT = "%Y-%m-%d %H:%M:%S %z"
DEFAULT_TAG_WHITELIST = r"^.*$"
DEFAULT_BRANCH_WHITELIST = r"^.*$"
DEFAULT_REMOTE_WHITELIST = None
DEFAULT_RELEASED_PATTERN = r"^tags/.*$"
DEFAULT_OUTPUTDIR_FORMAT = r"{ref.name}"

Version = namedtuple(
    "Version",
    [
        "name",
        "url",
        "version",
        "release",
        "is_released",
    ],
)


class VersionInfo:
    """Represents information of the available versions of documentation"""

    def __init__(self, app: sphinx_app, context: dict[str, Any], metadata: dict[str, Any], current_version_name: str):
        self.app = app
        self.context = context
        self.metadata = metadata
        self.current_version_name = current_version_name

    def _dict_to_versionobj(self, v: dict[str, Any]) -> Version:
        return Version(
            name=v["name"],
            url=self.vpathto(v["name"]),
            version=v["version"],
            release=v["release"],
            is_released=v["is_released"],
        )

    @property
    def tags(self) -> list[Version]:
        """Documentation version information by tag"""
        return [self._dict_to_versionobj(v) for v in self.metadata.values() if v["source"] == "tags"]

    @property
    def branches(self) -> list[Version]:
        """Documentation version information by branch"""
        return [self._dict_to_versionobj(v) for v in self.metadata.values() if v["source"] != "tags"]

    @property
    def releases(self) -> list[Version]:
        """Documentation version information of the released versions"""
        return [self._dict_to_versionobj(v) for v in self.metadata.values() if v["is_released"]]

    @property
    def in_development(self) -> list[Version]:
        """Documentation version information of the versions under development"""
        return [self._dict_to_versionobj(v) for v in self.metadata.values() if not v["is_released"]]

    def __iter__(self) -> Iterator[Version]:
        for item in self.tags:
            yield item
        for item in self.branches:
            yield item

    def __getitem__(self, name: str) -> Union[Version, None]:
        v = self.metadata.get(name)
        if v:
            return self._dict_to_versionobj(v)
        return None

    def vhasdoc(self, other_version_name: str) -> bool:
        """Return True if the current document exists in another version"""
        if self.current_version_name == other_version_name:
            return True

        other_version = self.metadata[other_version_name]
        return self.context["pagename"] in other_version["docnames"]

    def vpathto(self, other_version_name: str) -> str:
        """Get the relative URL to the current page in the other version of
        documentation. If the current page does not exist in that version, the
        relative URL to its root document is returned instead"""
        if self.current_version_name == other_version_name:
            return f"{posixpath.split(self.context['pagename'])[-1]}.html"

        # Find relative outputdir paths from common output root
        current_version = self.metadata[self.current_version_name]
        other_version = self.metadata[other_version_name]

        current_outputroot = os.path.abspath(current_version["outputdir"])
        other_outputroot = os.path.abspath(other_version["outputdir"])
        outputroot = os.path.commonpath((current_outputroot, other_outputroot))

        current_outputroot = os.path.relpath(current_outputroot, start=outputroot)
        other_outputroot = os.path.relpath(other_outputroot, start=outputroot)

        # Ensure that we use POSIX separators in the path (for the HTML code)
        if os.sep != posixpath.sep:
            current_outputroot = posixpath.join(*os.path.split(current_outputroot))
            other_outputroot = posixpath.join(*os.path.split(other_outputroot))

        # Find relative path to root of other_version's outputdir
        current_outputdir = posixpath.dirname(posixpath.join(current_outputroot, self.context["pagename"]))
        other_outputdir = posixpath.relpath(other_outputroot, start=current_outputdir)

        if not self.vhasdoc(other_version_name):
            return posixpath.join(other_outputdir, "index.html")

        return posixpath.join(other_outputdir, f"{self.context['pagename']}.html")


def html_page_context(
    app: sphinx_app,
    pagename: str,  # pylint: disable=unused-argument
    templatename: str,  # pylint: disable=unused-argument
    context: dict[str, Any],
    doctree: Union[sphinx_doc, None],  # pylint: disable=unused-argument
) -> None:
    """Set HTML page context"""
    versioninfo = VersionInfo(app, context, app.config.smv_metadata, app.config.smv_current_version)
    context["versions"] = versioninfo
    context["vhasdoc"] = versioninfo.vhasdoc
    context["vpathto"] = versioninfo.vpathto

    context["current_version"] = versioninfo[app.config.smv_current_version]
    context["latest_version"] = versioninfo[app.config.smv_latest_version]
    context["html_theme"] = app.config.html_theme


def config_inited(app: sphinx_app, config: sphinx_config) -> None:
    """Update the Sphinx builder.
    :param sphinx.application.Sphinx app: Sphinx application object.
    """

    if not config.smv_metadata:
        if not config.smv_metadata_path:
            return

        with open(config.smv_metadata_path, mode="r", encoding="utf-8") as f:
            metadata = json.load(f)

        config.smv_metadata = metadata  # type: ignore[attr-defined]

    if not config.smv_current_version:
        return

    try:
        data = app.config.smv_metadata[config.smv_current_version]
    except KeyError:
        return

    app.connect("html-page-context", html_page_context)

    # Restore config values
    old_config = sphinx_config.read(data["confdir"])
    old_config.pre_init_values()
    old_config.init_values()
    config.version = data["version"]  # type: ignore[attr-defined]
    config.release = data["release"]  # type: ignore[attr-defined]
    config.rst_prolog = data["rst_prolog"]  # type: ignore[attr-defined]
    config.today = old_config.today  # type: ignore[attr-defined]
    if not config.today:
        config.today = sphinx_i18n.format_date(  # type: ignore[attr-defined]
            format=config.today_fmt or _("%b %d, %Y"),
            date=datetime.datetime.strptime(data["creatordate"], DATE_FMT),
            language=config.language,
        )


def setup(app: sphinx_app) -> dict[str, Union[str, bool]]:
    """Setup sphinx"""
    app.add_config_value("smv_metadata", {}, "html")
    app.add_config_value("smv_metadata_path", "", "html")
    app.add_config_value("smv_current_version", "", "html")
    app.add_config_value("smv_latest_version", "master", "html")
    app.add_config_value("smv_tag_whitelist", DEFAULT_TAG_WHITELIST, "html")
    app.add_config_value("smv_branch_whitelist", DEFAULT_BRANCH_WHITELIST, "html")
    app.add_config_value("smv_remote_whitelist", DEFAULT_REMOTE_WHITELIST, "html")
    app.add_config_value("smv_released_pattern", DEFAULT_RELEASED_PATTERN, "html")
    app.add_config_value("smv_outputdir_format", DEFAULT_OUTPUTDIR_FORMAT, "html")
    app.connect("config-inited", config_inited)

    return {
        "version": "0.2",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
