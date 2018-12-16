
pdf_txt = 'en-final-table9.txt'
openfile = open(pdf_txt, 'r')
double_lined_countries = [
    'Bolivia (Plurinational \n',
]

def turn_on_off(line, status, start, end='\n'):

    """
    この関数は、行が特定の領域の先頭または、末尾を表すものに
    なっているかどうかをチェックする。行がそのようなものなら、
    statusをオン/オフする（True/Falseをセットする）。

    """

    if line.startswith(start):
        status = True
    elif status:
        if line == end :
            status = False
    return status

def clean(line):
    """
    改行、スペース、特殊文字を取り除く。
    """
    line = line.strip()
    line = line.replace('\xe2\x80\x93', '-')
    line = line.replace('\xe2\x80\x99', '\'')

    return line

countries = []
totals = []
country_line = total_line = False
previous_line = ''

for line in openfile:

    if country_line:
        if previous_line in double_lined_countries:
            line = ' '.join([clean(previous_line),clean(line)])
            countries.append(line)
        elif line not in double_lined_countries:
            countries.append(clean(line))
    elif total_line:
        totals.append(clean(line))

    country_line = turn_on_off(line, country_line, 'and areas')
    total_line = turn_on_off(line, total_line,'total')

    previous_line = line
import pprint
test_data = dict(zip(countries, totals))
pprint.pprint(test_data)
