# Quantum Computing Workbooks

A beginner course in quantum computing, built as Jupyter notebooks you can run in your browser.
Prepared by Aditya Sharma.

Each workbook has three parts: theory notes, exercises (easy, medium, hard, then Qiskit tasks) and a short quiz.
The course is planned as 14 workbooks. Workbooks 1 to 4 are here now as a review draft (v0.9), and the rest will follow.

## Workbooks

| # | Workbook | Run it | PDF |
|---|---|---|---|
| 1 | Maths and physics prerequisites | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adityasharma1307/quantum-workbooks/blob/main/workbooks/WB01_prerequisites.ipynb) | [PDF](pdf/WB01_prerequisites.pdf) |
| 2 | The qubit | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adityasharma1307/quantum-workbooks/blob/main/workbooks/WB02_qubit.ipynb) | [PDF](pdf/WB02_qubit.pdf) |
| 3 | Single-qubit gates | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adityasharma1307/quantum-workbooks/blob/main/workbooks/WB03_gates.ipynb) | [PDF](pdf/WB03_gates.pdf) |
| 4 | Multiple qubits | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adityasharma1307/quantum-workbooks/blob/main/workbooks/WB04_multiqubit.ipynb) | [PDF](pdf/WB04_multiqubit.pdf) |

Coming next: protocols (no-cloning, teleportation, superdense coding, BB84), query algorithms, QFT and phase estimation, Shor and post-quantum cryptography, Grover, noise and density matrices, error correction, hardware and transpilation, VQE and QAOA, and a capstone.

## Running locally

The first cell of each notebook installs the tested versions (qiskit 2.6.2, qiskit-aer 0.18.4). Everything runs on a simulator; no quantum hardware account is needed.

## Word versions

`tools/nb2docx.py` turns a notebook into an editable Word file:

```
pip install nbconvert pypandoc_binary
python tools/nb2docx.py --single workbooks/WB01_prerequisites.ipynb
```

## References

Nielsen and Chuang, *Quantum Computation and Quantum Information*; Hidary, *Quantum Computing: An Applied Approach*; Ding and Chong, *Quantum Computer Systems*; IBM Quantum Learning and the Qiskit documentation.

## Licence

Content is shared under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): reuse and adapt it, with credit to Aditya Sharma. Code in `tools/` is MIT.
