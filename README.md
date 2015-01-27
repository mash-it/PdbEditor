# PdbEditor
Edit PDB (Protein Data Bank) files.

とりあえず Molecule というクラスがある。以下のようにファイル名を指定することで PDB file を開く。

```python
from PdbEditor import Molecule
mol = Molecule("sample.pdb")
```

こうすればリスト `mol.atoms` の中に全ての原子の情報が入っている。たとえばX軸方向に100だけ平行移動したい場合は

```python
for atom in mol.atoms:
  atom['x'] += 100
```

とすれば良い。この操作は頻繁に使いそうなのでメソッド化しており、

```python
mol.shift('x', 100)
```

としても同じである。編集結果を出力するときは

```python
mol.output("shifted.pdb")
```

である。
