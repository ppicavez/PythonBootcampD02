import math

class TinyStatistician
    def mean(datas):
        m = len(datas)
        if m == 0:
            return None
        sum = 0
        for i in range(m):
            sum = sum + datas[i]
        return = sum / m

    def median(datas):
         m = len(datas)
        if m == 0:
            return None
        elif m == 1:
            return datas[0]    
        else:    
            datas.sorted()
            if m % 2:
                return datas[(m + 1) / 2]
            else:
                return  (datas[m / 2] + datas[m/2 +1] ) / 2

    def quartile(datas,percentile):
        pass

    def var(datas):
        m = len(datas)
        if m == 0:
            return None
        sum = 0
        the_mean = mean(datas)
        for i in range(m):
            sum = sum + (datas[i] - the_mean) * (datas[i] - the_mean)
        return = sum / m
    

    def std(datas):
        m = len(datas)
        if m == 0:
            return None
        sum = 0
        the_mean = mean(datas)
        for i in range(m):
            sum = sum + (datas[i] - the_mean) * (datas[i] - the_mean)
        return = sqrt(sum / m)
