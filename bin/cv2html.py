import sys, html, docx
from docx.oxml.ns import qn

def runs_html(p, doc):
    out=[]
    for child in p._p:
        if child.tag==qn('w:r'):
            out.append(run_html(child))
        elif child.tag==qn('w:hyperlink'):
            rid=child.get(qn('r:id')); url=None
            if rid and rid in doc.part.rels: url=doc.part.rels[rid].target_ref
            inner=''.join(run_html(r) for r in child.iter(qn('w:r')))
            out.append(f'<a href="{html.escape(url)}">{inner}</a>' if url else inner)
    return ''.join(out)

def run_html(r):
    txt=''
    for el in r:
        if el.tag==qn('w:t'): txt+=html.escape(el.text or '')
        elif el.tag==qn('w:tab'): txt+='\t'
        elif el.tag==qn('w:br'): txt+='\n'
    if not txt: return ''
    rpr=r.find(qn('w:rPr'))
    b=i=False
    if rpr is not None:
        bb=rpr.find(qn('w:b')); ii=rpr.find(qn('w:i'))
        b=bb is not None and bb.get(qn('w:val')) not in ('0','false')
        i=ii is not None and ii.get(qn('w:val')) not in ('0','false')
    if txt.strip()=='' : return txt
    if b: txt=f'<strong>{txt}</strong>'
    if i: txt=f'<em>{txt}</em>'
    return txt

def is_list(p):
    ppr=p._p.find(qn('w:pPr'))
    return ppr is not None and ppr.find(qn('w:numPr')) is not None

doc=docx.Document(sys.argv[1])
paras=doc.paragraphs
# skip header block (name, interests, contact) = until first Heading 1
start=next(i for i,p in enumerate(paras) if p.style.name=='Heading 1')
out=[]; in_list=False
def close_list():
    global in_list
    if in_list: out.append('</ul>'); in_list=False
for p in paras[start:]:
    h=runs_html(p,doc).strip()
    if not h.replace('\t','').strip(): continue
    st=p.style.name
    if st=='Heading 1':
        close_list(); out.append(f'<h2 class="cv-h1">{h}</h2>'); continue
    if st=='Heading 2':
        close_list(); out.append(f'<h3 class="cv-h2">{h}</h3>'); continue
    if is_list(p):
        if not in_list: out.append('<ul class="cv-list">'); in_list=True
        out.append(f'<li>{h.replace(chr(10),"<br>")}</li>'); continue
    close_list()
    lines=h.split('\n')
    rendered=[]
    for ln in lines:
        if '\t' in ln:
            left,right=ln.split('\t',1)
            right=right.replace('\t','').strip()
            if right:
                rendered.append(f'<div class="cv-row"><span>{left.strip()}</span><span class="cv-date">{right}</span></div>'); continue
            ln=left
        rendered.append(f'<div>{ln.strip()}</div>' if len(lines)>1 else ln.strip())
    body=''.join(rendered)
    out.append(f'<div class="cv-p">{body}</div>')
close_list()
print('\n'.join(out))
