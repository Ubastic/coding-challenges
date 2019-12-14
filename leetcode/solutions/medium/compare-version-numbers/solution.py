class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v_1 = [*map(int, v1.split('.')), *([0] * (v2.count('.') - v1.count('.')))]
        v_2 = [*map(int, v2.split('.')), *([0] * (v1.count('.') - v2.count('.')))]

        return (v_1 > v_2) - (v_1 < v_2)
