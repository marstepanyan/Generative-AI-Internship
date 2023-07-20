from Resource import Resource


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = self.validate_non_negative_int(cores, "cores")
        self._socket = socket
        self._power_watts = self.validate_non_negative_int(power_watts, "power_watts")

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb):
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_gb = self.validate_non_negative_int(capacity_gb, "capacity_GB")

    @property
    def capacity_gb(self):
        return self._capacity_gb


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._size = size
        self._rpm = self.validate_non_negative_int(rpm, "rpm")

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._interface = interface

    @property
    def interface(self):
        return self._interface
