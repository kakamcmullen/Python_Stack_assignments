my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

newList = []
for key, val in my_dict.iteritems():
    newList += [(key,val)]
print str(newList)