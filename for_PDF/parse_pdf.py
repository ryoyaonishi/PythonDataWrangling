import slate3k as slate
import warnings

pdf = 'EN-FINAL Table 9.pdf'

with open(pdf, 'rb') as f:
    doc = slate.PDF(f)

for page in doc[:2]:
    print(type(page))
