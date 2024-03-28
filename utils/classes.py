class Transaction:
    def __init__(self, version, vin, vout, locktime):
        self.version = version
        self.vin = vin
        self.vout = vout
        self.locktime = locktime

    @classmethod
    def from_dict(cls, data):
        version = data.get("version", 0)
        vin = data.get("vin", [])
        vout = data.get("vout", [])
        locktime = data.get("locktime", 0)
        return cls(version, vin, vout, locktime)

    def to_dict(self):
        return {
            "version": self.version,
            "vin": self.vin,
            "vout": self.vout,
            "locktime": self.locktime
        }

    def __repr__(self):
        return f"Transaction(version={self.version}, vin={self.vin}, vout={self.vout}, locktime={self.locktime})"
