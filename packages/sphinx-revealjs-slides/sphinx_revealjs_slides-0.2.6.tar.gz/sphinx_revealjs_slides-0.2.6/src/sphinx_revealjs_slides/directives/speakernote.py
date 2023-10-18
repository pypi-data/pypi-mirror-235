"""sphinxext.revealjs.directives.speakernote

The `.. speakernote::` directive. Add speaker notes to slide deck.
"""

from typing import TYPE_CHECKING, List

from docutils import nodes
from docutils.parsers.rst import Directive

if TYPE_CHECKING:
    from sphinx.application import Sphinx


class speakernote(nodes.General, nodes.Element):
    pass


class Speakernote(Directive):
    has_content = True

    def run(self) -> List[nodes.Node]:
        self.assert_has_content()
        node = speakernote("\n".join(self.content))
        node["classes"] += ["notes"]
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def visit_speakernote(self, node: speakernote) -> None:
    classes = " ".join(node["classes"])
    self.body.append(f'<aside class="{classes}">')


def depart_speakernote(self, node: speakernote) -> None:
    self.body.append("</aside>")


def ignore_speakernote(self, node: speakernote) -> None:
    raise nodes.SkipNode


def setup(app: "Sphinx") -> None:
    app.add_node(
        speakernote,
        html=(ignore_speakernote, None),  # type: ignore
        revealjs=(visit_speakernote, depart_speakernote),
    )
    app.add_directive("speaker", Speakernote)
