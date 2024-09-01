"""Helpers to create and use llms.txt files"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_core.ipynb.

# %% auto 0
__all__ = ['Sections', 'Project', 'parse_llms_file', 'Doc', 'Section', 'mk_ctx', 'get_sizes', 'llms_txt2ctx']

# %% ../nbs/01_core.ipynb
import re

# %% ../nbs/01_core.ipynb
from fastcore.utils import *
from fastcore.xml import *
from fastcore.script import *
import httpx

# %% ../nbs/01_core.ipynb
def _opt_re(s): return f'(?:{s})?'

def _parse_llms_txt(txt):
    pat = r"^#\s*(?P<title>[^\n]+)\n+"
    pat += _opt_re(r"^>\s*(?P<summary>.+?)\n+")
    pat += r"(?P<rest>.*)"
    match = re.search(pat, txt, flags=(re.DOTALL | re.MULTILINE))
    return match.groupdict() if match else None

# %% ../nbs/01_core.ipynb
def _split_on_h2(text):
    parts = re.split(r'\n?## ', text)
    details = parts[0].strip() if parts[0].strip() else None
    sections = [f"## {p.strip()}" for p in parts[1:] if p.strip()]
    return details, sections

# %% ../nbs/01_core.ipynb
def _parse_section(section):
    title = section.split('\n', 1)[0].strip('# ')
    links = re.findall(r'\[(.+?)\]\((.+?)\)(?:: (.+?))?(?=\n|$)', section)
    return title, [(t, u, d.strip() if d else None) for t, u, d in links]

# %% ../nbs/01_core.ipynb
def parse_llms_file(txt):
    parsed = _parse_llms_txt(txt)
    if not parsed: return None
    parsed['details'], sections = _split_on_h2(parsed['rest'])
    parsed['sections'] = dict(_parse_section(s) for s in sections)
    del parsed['rest']
    return dict2obj(parsed)

# %% ../nbs/01_core.ipynb
Sections = partial(ft, 'sections')
Project = partial(ft, 'project')

# %% ../nbs/01_core.ipynb
def Doc(url, **kw):
    "Create a `Doc` FT object with the text retrieved from `url` as the child, and `kw` as attrs."
    re_comment = re.compile('^<!--.*-->$', flags=re.MULTILINE)
    txt = [o for o in httpx.get(url).text.splitlines() if not re_comment.search(o)]
    return ft('doc', '\n'.join(txt), **kw)

# %% ../nbs/01_core.ipynb
def Section(nm, items):
    "Create a `Section` FT object containing a `Doc` object for each child."
    return ft(nm, *[Doc(title=title, url=url, detl=detl) for title,url,detl in items])

# %% ../nbs/01_core.ipynb
def mk_ctx(d, optional=True):
    "Create a `Project` with a `Section` for each H2 part in `d`, optionally skipping the 'optional' section."
    skip = '' if optional else 'Optional'
    sections = [Section(k, v) for k,v in d.sections.items() if k!=skip]
    return Project(title=d.title, summary=d.summary, details=d.details)(*sections)

# %% ../nbs/01_core.ipynb
def get_sizes(ctx):
    "Get the size of each section of the LLM context"
    return {o.tag:{p.title:len(p.children[0]) for p in o.children} for o in ctx.children}

# %% ../nbs/01_core.ipynb
@call_parse
def llms_txt2ctx(
    fname:str, # File name to read
    optional:bool_arg=True # Skip 'optional' section?
):
    "Print a `Project` with a `Section` for each H2 part in file read from `fname`, optionally skipping the 'optional' section."
    d = parse_llms_file(Path(fname).read_text())
    ctx = mk_ctx(d, optional=optional)
    print(to_xml(ctx, do_escape=False))