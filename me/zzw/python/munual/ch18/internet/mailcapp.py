import mailcap
d = mailcap.getcaps()
print mailcap.findmatch(d, 'video/mpeg', filename='tmp1223')
