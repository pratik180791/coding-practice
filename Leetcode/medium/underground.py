class UndergroundSystem:

    def __init__(self):
        self.register = {}
        self.checkout_stats = {}
        #self.
        self.avg_results = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.register:
            self.register[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        #if id not  in
        start_station, start_time = self.register[id]
        total_commute = t - start_time
        #if start_station not in
        self.checkout_stats[id] = [start_station, stationName, start_time, t, total_commute]
        caching_key = start_station+"|"+stationName
        if caching_key not in self.avg_results:
            self.avg_results[caching_key] = [total_commute]
        else:
            self.avg_results[start_station+"|"+stationName].append(total_commute)
        del self.register[id]

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        caching_key = start_station+"|"+end_station
        if caching_key not in self.avg_results:
            return 0.0
        return sum(self.avg_results[caching_key])/len(self.avg_results[caching_key])

# Your UndergroundSystem object will be instantiated and called as such:
undergroundSystem = UndergroundSystem()
""""
#obj.checkIn(45,'',t)
#UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)

#print(undergroundSystem.register)
undergroundSystem.checkOut(45, "Waterloo", 15)
#print(undergroundSystem.register)

undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
res = undergroundSystem.getAverageTime("Paradise", "Cambridge")
print(res)
res = undergroundSystem.getAverageTime("Leyton", "Waterloo")
print(res)
undergroundSystem.checkIn(10, "Leyton", 24)
res = undergroundSystem.getAverageTime("Leyton", "Waterloo")
print(res)
undergroundSystem.checkOut(10, "Waterloo", 38)
res = undergroundSystem.getAverageTime("Leyton", "Waterloo")
print(res)
print(undergroundSystem.register)
print(undergroundSystem.checkout_stats)
print(undergroundSystem.avg_results)
# obj.checkOut(id,stationName,t)
#param_3 = obj.getAverageTime(startStation,endStation)
"""
undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8);
undergroundSystem.getAverageTime("Leyton", "Paradise"); #// return 5.00000
undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16);
undergroundSystem.getAverageTime("Leyton", "Paradise"); #// return 5.50000
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30);
res = undergroundSystem.getAverageTime("Leyton", "Paradise"); #// return 6.66667
print(res)