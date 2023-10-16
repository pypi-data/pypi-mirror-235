# Splits a list into sublists based on either a list of indices or a number of sections.

## Tested against Windows / Python 3.11 / Anaconda

## pip install splitlistatindex

```python
from splitlistatindex import list_split
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [3, 5, 7, 8, 12]

# Split `l1` using a list of indices
result1 = list_split(l=l1, indices_or_sections=l2)
# result1 will be: [[0, 1, 2], [3, 4], [5, 6], [7], [8, 9]]

# Split `l1` into 3 sections
result2 = list_split(l=l1, indices_or_sections=3)
# result2 will be: [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9]]

```

