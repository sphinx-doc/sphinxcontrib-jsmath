"""Test for jsmath extension."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from sphinx.application import Sphinx


@pytest.mark.sphinx('html', testroot='basic')
def test_basic(app: Sphinx) -> None:
    app.builder.build_all()
    content = (app.outdir / 'math.html').read_text(encoding='utf-8')
    print(content)
    assert '<div class="math notranslate nohighlight">\nE = mc^2</div>' in content
    assert ('<span class="eqno">(1)<a class="headerlink" href="#equation-pythagorean" '
            'title="Permalink to this equation">¶</a></span>'
            '<div class="math notranslate nohighlight" id="equation-pythagorean">\n'
            'a^2 + b^2 = c^2</div>' in content)
    assert ('<span class="eqno">(2)<a class="headerlink" href="#equation-math-0" '
            'title="Permalink to this equation">¶</a></span>'
            '<div class="math notranslate nohighlight" id="equation-math-0">\n'
            '\\begin{split}y &gt; x \\in 2\\end{split}</div>' in content)
    assert '<a class="reference internal" href="#equation-pythagorean">(1)</a>' in content
    assert '<a class="reference internal" href="#equation-pythagorean">(1)</a>' in content


@pytest.mark.sphinx('html', testroot='basic',
                    confoverrides={'numfig': True, 'math_numfig': True})
def test_numfig_enabled(app: Sphinx) -> None:
    app.builder.build_all()

    content = (app.outdir / 'math.html').read_text(encoding='utf-8')
    assert '<div class="math notranslate nohighlight">\nE = mc^2</div>' in content
    assert ('<span class="eqno">(1.1)<a class="headerlink" href="#equation-pythagorean" '
            'title="Permalink to this equation">¶</a></span>'
            '<div class="math notranslate nohighlight" id="equation-pythagorean">\n'
            'a^2 + b^2 = c^2</div>' in content)
    assert ('<span class="eqno">(1.2)<a class="headerlink" href="#equation-math-0" '
            'title="Permalink to this equation">¶</a></span>'
            '<div class="math notranslate nohighlight" id="equation-math-0">\n'
            '\\begin{split}y &gt; x \\in 2\\end{split}</div>' in content)
    assert '<a class="reference internal" href="#equation-pythagorean">(1.1)</a>' in content
    assert '<a class="reference internal" href="#equation-pythagorean">(1.1)</a>' in content


@pytest.mark.sphinx('html', testroot='nomath')
def test_disabled_when_equations_not_found(app: Sphinx) -> None:
    app.builder.build_all()

    content = (app.outdir / 'index.html').read_text(encoding='utf-8')
    assert 'jsmath.js' not in content
