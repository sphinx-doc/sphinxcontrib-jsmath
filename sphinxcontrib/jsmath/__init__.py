"""Set up everything for use of JSMath to display math in HTML via JavaScript."""

from __future__ import annotations

from os import path
from typing import TYPE_CHECKING, Any, cast

from docutils import nodes
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.domains.math import MathDomain
from sphinx.errors import ExtensionError
from sphinx.locale import get_translation
from sphinx.util.math import get_node_equation_number

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.environment import BuildEnvironment
    from sphinx.writers.html import HTMLTranslator

__version__ = '1.0.2'
__version_info__ = (1, 0, 2)

package_dir = path.abspath(path.dirname(__file__))

_ = get_translation(__name__)


def html_visit_math(self: HTMLTranslator, node: nodes.math) -> None:
    self.body.append(self.starttag(node, 'span', '', CLASS='math notranslate nohighlight'))
    self.body.append(self.encode(node.astext()) + '</span>')
    raise nodes.SkipNode


def html_visit_displaymath(self: HTMLTranslator, node: nodes.math_block) -> None:
    if node['nowrap']:
        self.body.append(self.starttag(node, 'div', CLASS='math notranslate nohighlight'))
        self.body.append(self.encode(node.astext()))
        self.body.append('</div>')
        raise nodes.SkipNode
    for i, part in enumerate(node.astext().split('\n\n')):
        part = self.encode(part)
        if i == 0:
            # necessary to e.g. set the id property correctly
            if node['number']:
                number = get_node_equation_number(self, node)
                self.body.append(f'<span class="eqno">({number})')
                self.add_permalink_ref(node, _('Permalink to this equation'))
                self.body.append('</span>')
            self.body.append(self.starttag(node, 'div', CLASS='math notranslate nohighlight'))
        else:
            # but only once!
            self.body.append('<div class="math">')
        if '&' in part or '\\\\' in part:
            self.body.append('\\begin{split}' + part + '\\end{split}')
        else:
            self.body.append(part)
        self.body.append('</div>\n')
    raise nodes.SkipNode


def install_jsmath(app: Sphinx, env: BuildEnvironment) -> None:
    if app.builder.format != 'html' or app.builder.math_renderer_name != 'jsmath':  # type: ignore[attr-defined]
        return
    if not app.config.jsmath_path:
        msg = 'jsmath_path config value must be set for the jsmath extension to work'
        raise ExtensionError(msg)

    builder = cast(StandaloneHTMLBuilder, app.builder)
    domain = cast(MathDomain, env.get_domain('math'))
    if domain.has_equations():
        # Enable jsmath only if equations exists
        builder.add_js_file(app.config.jsmath_path)


def setup(app: Sphinx) -> dict[str, Any]:
    app.require_sphinx('5.0')
    app.add_message_catalog(__name__, path.join(package_dir, 'locales'))
    app.add_html_math_renderer('jsmath',
                               (html_visit_math, None),
                               (html_visit_displaymath, None))

    app.add_config_value('jsmath_path', '', False)
    app.connect('env-updated', install_jsmath)
    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
