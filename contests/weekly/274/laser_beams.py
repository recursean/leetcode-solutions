from typing import *

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        devices = 0
        prev_devices = 0
        count_beams = False

        for row in bank:
            for c in row:
                if c == '1':
                    if prev_devices > 0:
                        count_beams = True

                    devices += 1

            if prev_devices > 0 and not count_beams:
                continue

            if count_beams:
                beams += devices * prev_devices
                count_beams = False

            prev_devices = devices    
            devices = 0

        return beams

sol = Solution()
s = ["000","111","000"]
print(sol.numberOfBeams(s))