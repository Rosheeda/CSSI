#Exercise 1
def longest_word (p,q,r):
    if len(p) >= len(q) and len(p) >= len(r):
        return p
    elif len(q) >= len(p) and len(q) >= len(r):
        return q
    elif len(r) >= len(p) and len(r) >= len(q):
        return r
longest = longest_word("Miller", "Manikin", "Rumpelstilstkin")
print (longest)

#Exercise 2
string = input("Yensid")

def reverse(string):
    revstring = ''
    index = len(string)
    while index > 0:
        revstring += string[index -1]
        index = index -1
    return revstring

print(reverse(string))
