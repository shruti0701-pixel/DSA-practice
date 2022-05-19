class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums = []
        for i, row in enumerate(mat):
            sums.append((sum(row), i))

        sorted_sums = sorted(sums)

        k_rows = sorted_sums[:k]

        res = []
        for val in k_rows:
            res.append(val[1])

        return res