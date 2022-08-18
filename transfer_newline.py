from antx import transfer
from pathlib import Path


src = Path("I75A88184/I75A88184.opf/base/E38A.txt").read_text()
trg = Path("O2FCA4A99/O2FCA4A99.opf/base/6ABB.txt").read_text()
annotations = [["newline","(endline)"]]
result = transfer(src, annotations, trg, output="txt")
Path("annoted_txt.txt").write_text(result,encoding="utf-8")