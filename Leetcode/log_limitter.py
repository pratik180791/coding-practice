class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log_limitter = {}
        self.base_time_stamp = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.log_limitter:
            self.log_limitter[message] = self.base_time_stamp + timestamp
            return True
        if timestamp >= self.log_limitter[message]:
            return True
        else:
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
