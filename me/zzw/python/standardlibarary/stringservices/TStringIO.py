import StringIO

output = StringIO.StringIO()
output.write("First line.\n")
print >> output, 'Second line.'

contents = output.getvalue()
output.close()
print contents
