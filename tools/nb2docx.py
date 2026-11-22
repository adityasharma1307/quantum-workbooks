#!/usr/bin/env python3
"""Turn workbook notebooks into Word (.docx) files and lay them out as

    Quantum_Workbooks/
      Workbook 1/
        Student/     WB01_student.ipynb  WB01_student.docx  WB01_student.pdf
        Instructor/  WB01_instructor.ipynb  ...
      Workbook 2/ ...

Usage:
    python nb2docx.py                      # uses ./out, writes ./Quantum_Workbooks
    python nb2docx.py --src out --dest MyFolder
    python nb2docx.py --single path/to/notebook.ipynb   # convert one notebook

Needs: pip install nbconvert pypandoc_binary
Code cells and their outputs (text and plots) are kept. Maths is converted
to editable Word equations.
"""
import argparse, re, shutil, tempfile
from pathlib import Path

import nbformat
import pypandoc
from nbconvert import MarkdownExporter


def notebook_to_docx(nb_path: Path, docx_path: Path) -> None:
    nb = nbformat.read(nb_path, as_version=4)
    body, res = MarkdownExporter().from_notebook_node(nb)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for name, data in res.get("outputs", {}).items():
            (tmp / name).write_bytes(data)
        md = tmp / "nb.md"
        md.write_text(body, encoding="utf-8")
        docx_path.parent.mkdir(parents=True, exist_ok=True)
        pypandoc.convert_file(
            str(md), "docx", format="markdown+tex_math_dollars",
            outputfile=str(docx_path),
            extra_args=[f"--resource-path={tmp}"],
        )


def build_tree(src: Path, dest: Path) -> list:
    made = []
    for edition, sub in (("student", "Student"), ("instructor", "Instructor")):
        for nb in sorted((src / edition).glob("WB*_" + edition + ".ipynb")):
            num = int(re.match(r"WB(\d+)", nb.name).group(1))
            folder = dest / f"Workbook {num}" / sub
            folder.mkdir(parents=True, exist_ok=True)
            shutil.copy2(nb, folder / nb.name)
            pdf = src / "pdf" / (nb.stem + ".pdf")
            if pdf.exists():
                shutil.copy2(pdf, folder / pdf.name)
            docx = folder / (nb.stem + ".docx")
            notebook_to_docx(nb, docx)
            made.append(docx)
            print("made", docx)
    return made


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="out")
    ap.add_argument("--dest", default="Quantum_Workbooks")
    ap.add_argument("--single")
    a = ap.parse_args()
    if a.single:
        p = Path(a.single)
        notebook_to_docx(p, p.with_suffix(".docx"))
        print("made", p.with_suffix(".docx"))
    else:
        build_tree(Path(a.src), Path(a.dest))
