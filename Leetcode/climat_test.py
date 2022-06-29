"""
["abi", "Soyabean", 130]
["abi2", "Soyabean", 180]
["whe1", "Wheat", 30]
["whe2", "Wheat", 10]
["whe3", "Wheat", 100]
"""

from typing import List


class Farm:
    def __init__(self):
        self.farm_info = {}

    def add_farm(self, farm_name: str, crop_type: str, size: int):
        if crop_type not in self.farm_info:
            self.farm_info[crop_type] = [[farm_name, crop_type, size]]
        else:
            curr_val = [farm_name, crop_type, size]
            insert_pos = self._insert_pos(self.farm_info[crop_type], curr_val)
            self.farm_info[crop_type].insert(insert_pos, curr_val) #insert in place

    def _insert_pos(self, farm_list: List[List], curr_val: List, low=0, high=None):
        if high is None:
            high = len(farm_list)
        while low < high:
            mid = (low+high)//2
            if farm_list[mid][2] < curr_val[2]: #Reverse insert logic
                high = mid
            else:
                low = mid + 1
        return low

    def get_top_farms(self, n: int):
        res = {}
        for key, val in self.farm_info.items():
            res[key] = val[:n]
        return res


farm = Farm()
farm.add_farm("abi", "Soyabean", 130)
farm.add_farm("abi2", "Soyabean", 180)
farm.add_farm("whe1", "Wheat", 30)
farm.add_farm("whe2", "Wheat", 10)
farm.add_farm("whe3", "Wheat", 100)
res = farm.get_top_farms(1) #{'Soyabean': [['abi2', 'Soyabean', 180]], 'Wheat': [['whe3', 'Wheat', 100]]}
print(res)
