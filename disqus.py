from jinja2 import Template
from IPython.display import (
    display,
    HTML,
)
from IPython.core import magic

tmpl = Template("""
<div id="disqus_thread"></div>

<script type="text/javascript">
    var disqus_shortname = "{{ shortname }}";
    {% if title %}
        var disqus_title = "{{ title }}";
    {% endif %}
</script>
<script src="https://{{ shortname }}.disqus.com/embed.js" async="true">
</script>

<noscript>
    Please enable JavaScript to view the
    <a href="https://disqus.com/?ref_noscript" rel="nofollow">
        comments powered by Disqus.
    </a>
</noscript>
""")

@magic.magics_class
class DisqusMagics(magic.Magics):
    @magic.line_magic
    def disqus(self, line):
        line = line.strip().split(" ", 1)
        title = line[1] if len(line) > 1 else None
        
        display(HTML(tmpl.render(shortname=line[0],
                                 title=title)))
def load_ipython_extension(ip):
    ip.register_magics(DisqusMagics)
