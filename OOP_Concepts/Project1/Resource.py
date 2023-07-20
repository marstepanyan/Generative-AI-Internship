class Resource:
    def __init__(self, name, manufacturer, total=0, allocated=0):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, count):
        self._total = count

    @property
    def allocated(self):
        return self._allocated

    @allocated.setter
    def allocated(self, count):
        self._allocated = count

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', '{self._manufacturer}', {self._total}, {self._allocated})"

    def claim(self, count):
        self.validate_non_negative_int(count, "Count for claiming")
        if self.total - self.allocated >= count:
            self.allocated += count
            return f"Claimed {count} successfully"
        return "Claiming failed"

    def freeup(self, count):
        self.validate_non_negative_int(count, "Count for freeing up")
        if self.allocated >= count:
            self.allocated -= count
            return f"Freeing up {count} successfully"
        return "Freeing up failed"

    def died(self, count):
        self.validate_non_negative_int(count, "Count for return and permanently remove")
        if self.total - self.allocated >= count:
            self.total -= count
            return f"Returned and permanently removed {count} successfully"
        return "Return and permanently remove failed"

    def purchased(self, count):
        self.validate_non_negative_int(count, "Count for adding inventory")
        self.total += count
        return f"{count} purchased successfully"

    @property
    def category(self):
        return self.__class__.__name__.lower()

    @staticmethod
    def validate_non_negative_int(value, attr_name):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{attr_name} must be a non-negative integer.")
        return value
