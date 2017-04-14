for x in range(99,0,-1):
 print"{0}{1}{2}{0}{1}\nTake one down, pass it around\n{3}{1}{2}\n".format(x," bottle"+("s","")[x==1]+" of beer"," on the wall\n",x-1 or'No')
