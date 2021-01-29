 
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
 
text = "this is string example....wow!!!";
print(text.translate(trantab));

