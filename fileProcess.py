import re


def modifyFile(file):
    file.encode("UTF-8")
    temResult = re.split(r"[……、：\n]", file)
    temReturn = []
    for tem in temResult:
        if validParen(tem):
            temReturn.append(tem)
        else:
            tem = tem.replace('（', "")
            tem = tem.replace('）', "")
            temReturn.append(tem)
    temReturn = [x.strip() for x in temReturn if x.strip() != '']
    return temReturn

def validParen(str):
    a = {'（': '）'}
    l = [None]
    for i in str:
        if i in a and a[i] == l[-1]:
            l.pop()
        else:
            l.append(i)
    return len(l) == 1
