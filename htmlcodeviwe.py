import mechanize

b = raw_input("inter the traget url:-")
a = mechanize.urlopen(b)
c = a.read()
print(c)
