import lua_re
from lua_read import read_file

class Statistics:
    def __init__(self, ext_npq):
        self.npq = ext_npq

    def total(self): 
        result = {}
        for name in self.npq:
            total_prc, total_qty = 0, 0
            prc_qty = self.npq[name]

            for (prc, qty) in prc_qty:
                prc, qty = map(int, (prc, qty))
                total_prc += prc*qty
                total_qty += qty
                total_avg = round(total_prc / total_qty)
            result[name] = (total_prc, total_qty, total_avg)

        return result