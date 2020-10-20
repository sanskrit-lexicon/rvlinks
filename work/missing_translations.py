# coding=utf-8
""
import sys,re,codecs
import glob
hymn_template =u"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>%s</title>
<link rel="stylesheet" type="text/css" href="rvhymns.css">
</head>
<body>
%s
<div>
<hr/>
<span style="font-size:smaller">
Translations compiled by Dr. Mārcis Gasūns.
</span>
<br/>
</div>
<div style="height:900px"></div> <!-- a trick for proper anchor scrolling -->
</body>
</html>
"""
class Hymnprev(object):
 def __init__(self,hymnid,verses):
  self.hymnid = hymnid
  self.verses = verses
 def write(self,fileout):
  with codecs.open(fileout,"w","utf-8") as f:
   html = self.html()
   f.write(html + '\n')
 def html(self):
  mandala,hymnnum = self.hymnid
  title = "rv%s.%s" %(mandala,hymnnum)
  bodylines = []
  for verse in self.verses:
   (_,_,versenum) = verse.verseid
   verselines = verse.verselines
   #print title, len(verselines)
   for iline,line in enumerate(verselines):
    if iline == 0:
     # use id attribute for html5
     a = "<a id='rv%s.%s.%s'/>" %(mandala,hymnnum,versenum)
     bodylines.append(a + line)
    else:
     bodylines.append(line)
  bodystring = '\n'.join(bodylines)
  htmlstring = hymn_template %(title,bodystring)
  return htmlstring

class Verse(object):
 def __init__(self,verseid,verselines):
  self.verseid = verseid
  self.verselines = verselines

def init_verses(lines):
 verses = []
 inverse = False
 for idx,line in enumerate(lines):
  m = re.search(r'^<br /><p class="stamp">rv([0-9]+)[.]([0-9]+)[.]([0-9]+)</p>$',line)
  if idx == 0:
   # first verse
   if not m:
    print("init_verses problem",idx,line.encode('utf-8'))
    exit(1)
   verseid = (m.group(1),m.group(2),m.group(3)) # keep as tuple for later
   verselines = [line]
   inverse = True
   continue
  if m:
   # first line of next verse found
   verse = Verse(verseid,verselines)
   verses.append(verse)
   # Start new verse
   verseid = (m.group(1),m.group(2),m.group(3)) # keep as tuple for later
   verselines = [line]
   inverse = True
   continue
  else:
   # add next line of current verse
   verselines.append(line)
 # install last verse
 verse = Verse(verseid,verselines)
 verses.append(verse)
 return verses

def init_hymns(verses):
 hymns = []
 for iverse,verse in enumerate(verses):
  (mandala,hymnnum,versenum) = verse.verseid
  if iverse == 0:
   # first hymn
   hymnid = (mandala,hymnnum)
   hymnverses = [verse]
  elif versenum == '01':
   # first line of next hymn
   hymn = Hymn(hymnid,hymnverses)
   hymns.append(hymn)
   # start next hymn
   hymnid = (mandala,hymnnum)
   hymnverses = [verse]
  else:
   # add another verse to current hymn
   hymnverses.append(verse)
 # install last hymn
 hymn = Hymn(hymnid,hymnverses)
 hymns.append(hymn)
 return hymns

def adjust_lines1(lines):
 out = []
 flag = False
 for idx,line in enumerate(lines):
  if line.startswith('</td>'):
   print("last line #",(idx-1)+1)
   break  # ending table code skipped.
  if line.startswith('<br /><p'):
   if not flag: print("first line #",idx+1)
   flag = True
  if flag:
    out.append(line)
 return out
class Verse(object):
 def __init__(self,verseid,tranlines):
  self.verseid = verseid
  self.tranlines = tranlines

def find_bodylines(lines):
 inbody = None
 bodylines = []
 for line in lines:
  if line.startswith('<body>'):
   inbody = True
   continue
  #if line.startswith('</body>'):
  if line.startswith('<div>'):
   break
  if inbody:
   bodylines.append(line)
 return bodylines

def parse_verse(idx,lines):
 # <a id='rvxx.yyy.zz'
 i = idx
 # rv(..)[.](...)[.](..)
 m = re.search(r"^<a id='(.*?)'/>",lines[i])
 #(mandala,hymnnum,versenum) = (m.group(1),m.group(2),m.group(3))
 if m == None:
  print('parse_verse error 1:',idx,lines[i])
  exit(1)
 verseid = m.group(1)
 ntran = 0
 tranlines=[]
 i = i + 1
 
 while (ntran < 5):
  # most lines start with <p class="...">
  # by in rv08.091, we have extra spaces at beginning of line
  if re.search(r'^ *<p class="(.*?)">(.*)$',lines[i]):
   tranlines.append(lines[i])
   ntran = ntran + 1
   if ntran == 5:
    break
  i = i + 1
 if lines[i] == '</p>':
  pass
 elif lines[i].endswith('</p>'):
  pass
 else:
  while not lines[i].endswith('</p>'):
   i = i + 1
   #i = i + 1
 verse = Verse(verseid,tranlines)
 if verseid == 'rv08.049.95':
  for x in tranlines:
   print('check',verseid,': ',x)
  print(' next i:',i,lines[i])
 return i,verse

class Hymn(object):
 def __init__(self,filename):
  self.filename = filename
  with codecs.open(filename,"r","utf-8") as f:
   self.lines = [x.rstrip('\r\n') for x in f]
   bodylines = find_bodylines(self.lines)
   #print(filename,len(bodylines))
   verses = []
   idx = 0
   while idx < len(bodylines):
    idxnew,verse = parse_verse(idx,bodylines)
    if filename.endswith('rv01.012.html'):
     #print(idx,verse.verseid)
     pass
    verses.append(verse)
    idx = idxnew + 1
   self.verses = verses
  #print(self.filename,len(self.verses))

def analyze_hymns(recs,fileout):
 outarr = []
 trancodes = ['sa','hn','ru','de','en']  # hn = IAST
 for rec in recs:
  # rec is a Hymn object
  verses = rec.verses
  
  for verse in verses:
   verseid = verse.verseid
   transtatus = []
   verse_status = True   # ALL translations present
   for idx,tranline in enumerate(verse.tranlines):
    trancode = trancodes[idx]
    m = re.search(r'^<p class="%s">(.*)' %trancode,tranline)
    if not m:
     print('Anomaly at',verseid)
    text = m.group(1)  # the beginning of translation
    if text.startswith('-%s-'%trancode):
     transtatus.append('No')  # no translation for this language
     verse_status = False  # this translation absent
    else:
     transtatus.append('Yes')
   # print only those verses with some missing translation
   if not verse_status:
    outverse = [verseid]
    for idx,tranline in enumerate(verse.tranlines):
     trancode = trancodes[idx]
     outverse.append('%s=%s' % (trancode,transtatus[idx]))
    out = ':'.join(outverse)
    outarr.append(out)
 # write to text file
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out + '\n')
 print(len(outarr),"lines written to",fileout)
 
if __name__ == "__main__":
 dirin=sys.argv[1]
 fileout = sys.argv[2]
 pattern = "%s/rv*.html" %dirin
 #print(pattern)
 rvhymns = glob.glob(pattern)
 recs = []
 for idx,filename in enumerate(rvhymns):
  recs.append(Hymn(filename))
  if idx == 10: 
   #print('dbg quit at idx=',idx)
   #break
   pass
 analyze_hymns(recs,fileout)
 print(len(rvhymns),"rvhymn files")
 nverses = sum(len(h.verses) for h in recs)
 print('Total number of verses:',nverses)

