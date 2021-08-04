
# We need to support
# if, else, while, or, and, print, input, int
# readSankya

#
#   if-then
#
#   ఒకవేల  (నెల == 2)   అయితే:
# ==>
#   if(నెల == 2):
#
regex = r"(?m)^(\s*)ఒకవేల(\s*)(\(.*\))(\s*)అయితే(\s*):"
# test_str = "	ఒకవేల  (నెల == 2)   అయితే:"
subst = "\\1if\\3:"


#
#   else
#
#   కాకపోతే  :
# ==>
#   else:
#
regex = r"(?m)^(\s*)కాకపోతే(\s*):"
# test_str = "	కాకపోతే  :"
subst = "\\1else:"

#
#   while
#
#   (సంఖ్య <= n)   అయ్యేవరకు     :
# ==>
#   while(సంఖ్య <= n):
#
regex = r"(?m)^(\s*)(\(.*\))(\s*)అయ్యేవరకు(\s*):"
# test_str = "    (సంఖ్య <= n)   అయ్యేవరకు     :\n"
subst = "\\1while\\2:"


#
#   conditional or - best గాని, other - లేద, కాని
#
#   ఒకవేల ((నెల == 4) గాని (నెల == 9) గాని (నెల == 11)) అయితే:
# ==>
#   ఒకవేల ((నెల == 4) or (నెల == 9) or (నెల == 11)) అయితే:
#
regex = r"(?m)\) గాని \("
# test_str = "ఒకవేల ((నెల == 4) గాని (నెల == 9) గాని (నెల == 11)) అయితే:\n"
subst = "\\) or \\("


#
#   conditional and - best ఇంకా, other - మరియు
#
#   ఒకవేల ((నెల % 4 == 0) ఇంకా (నెల % 100 == 0)) అయితే:
# ==>
#   ఒకవేల ((నెల % 4 == 0) and (నెల % 100 == 0)) అయితే:
#
regex = r"(?m)\) ఇంకా \("
# test_str = "ఒకవేల ((నెల % 4 == 0) ఇంకా (నెల % 100 == 0)) అయితే:\n"
subst = "\\) and \\("
