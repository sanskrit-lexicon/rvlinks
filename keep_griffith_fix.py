# coding=utf-8
# The 2020 Griffith-stanza rearrangement (593b78c "rearrange griffith
# stanzas" + 6eceb5e, issue #2) fixed the English layer of rv08.049-103
# by hand in the generated pages; the source document was never updated.
# After regenerating rvhymns/ from the source, graft the committed bodies
# of those 55 pages back under the freshly generated heads, so the
# hand-approved fix survives every rebuild. Reads HEAD => idempotent.
# Usage: python3 keep_griffith_fix.py   (run from the repo root, after make_hymns_01.py)
import subprocess,sys

IDS = ['rv08.%03d' % n for n in range(49,104)]  # rv08.049 .. rv08.103

def main():
 for id_ in IDS:
  path = 'rvhymns/%s.html' % id_
  old = subprocess.run(['git','show','HEAD:'+path],
                       capture_output=True,encoding='utf-8',check=True).stdout
  if '<body>' not in old:
   print('no committed body for',id_)
   exit(1)
  with open(path,encoding='utf-8') as f:
   new = f.read()
  head_new = new[:new.index('<body>')]
  body_old = old[old.index('<body>'):]
  with open(path,'w',encoding='utf-8') as f:
   f.write(head_new + body_old)
 print('%s hand-fixed Griffith bodies grafted under new heads' % len(IDS))

if __name__ == '__main__':
 main()
