import lua_re
from lua_read import read_file

class Statistics:
    def __init__(self, ext_npq):
        self.npq = ext_npq

    def rm_outlier(self):
        f1, f3 = 0.25, 0.75
#        ## <tmp>
#        print('BEFORE REMOVING OUTLIER:\n',
#        self.npq)
#        print('='*100)
#        ## </tmp>
        for key in self.npq:
            prc_qty = self.npq[key]

            tmp = []
            for (prc, qty) in prc_qty: tmp.append(int(prc))
            
            tmp.sort()
            n = len(tmp)
#            med = 0
#            if n % 2 == 0: med = (tmp[n/2 - 1] + tmp[n/2]) / 2
#            else: med = tmp[(n-1) / 2]
            
            i1, i3 = 0, 0
            q1, q3 = 0, 0
            l_outlier, u_outlier = 0, 0

            i1 = int(f1 * (n - 1))
            i3 = int(f3 * (n - 1))

            q1, q3 = tmp[i1], tmp[i3]
            iqr = q3 - q1

            l_outlier = q1 - 1.5*iqr
            u_outlier = q3 + 1.5*iqr
#            ## <tmp>    
#            print('\nNAME, BTM_BOUNDARY, TOP_BOUNDARY\n', key, l_outlier, u_outlier)
#            print('='*100)
#            ## </tmp>
            tmp2 = []
            for (prc, qty) in prc_qty:
                if l_outlier <= int(prc) <= u_outlier:
                    tmp2.append((int(prc), int(qty)))

            self.npq[key] = tmp2
#        ## <tmp>
#        print('AFTER REMOVING OUTLIER:\n',
#        self.npq)
#        print('='*100)
#        ## </tmp>
    def total(self): 
        total_arr = []
        for name in self.npq:
            total = {}
            total_prc, total_qty = 0, 0
            prc_qty = self.npq[name]

            prc_top, prc_btm = 0, 10000000000
            for (prc, qty) in prc_qty:
                prc, qty = map(int, (prc, qty))
                total_prc += prc*qty
                total_qty += qty
                total_avg = round(total_prc / total_qty)
            
                if prc >= prc_top: prc_top = prc
                if prc <= prc_btm: prc_btm = prc

            total = {'NAME':name, 'QUANTITY':total_qty, 'AVERAGE':total_avg,
                    'TOP_PRICE':prc_top, 'BTM_PRICE':prc_btm}
            total_arr.append(total)
        return total_arr

