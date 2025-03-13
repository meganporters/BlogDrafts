from __future__ import annotations

from html import escape
from . import storage


def render_index(tag: str | None = None) -> str:
    drafts = storage.list_by_tag(tag)
    items = []
    for d in drafts:
        items.append(
            """
<li>
  <article>
    <header>
      <h2>{title}</h2>
      <small>{ts}</small>
    </header>
    <p><em>{tags}</em></p>
    <p>{body}</p>
  </article>
</li>
""".format(
                title=escape(d.title),
                ts=escape(d.created_at),
                tags=escape(", ".join(d.tags)),
                body=escape(d.body),
            )
        )
    return "<ul>" + "\n".join(items) + "</ul>"

