import math


class TinyStatistician():

    def mean(self, datas):
        m = len(datas)
        if m == 0:
            return None
        sum = 0
        for i in range(m):
            sum = sum + datas[i]
        return sum / m

    def median(self, datas):
        m = len(datas)
        if m == 0:
            return None
        elif m == 1:
            return datas[0]
        else:
            datas.sort()
            if m % 2:
                return datas[(m + 1) / 2]
            else:
                return (datas[m / 2] + datas[m / 2 + 1]) / 2

    def quartile(self, datas, percentile):
        pass

    def var(self, atas):
        m = len(datas)
        if m == 0:
            return None
        sum = 0
        the_mean = mean(datas)
        for i in range(m):
            sum = sum + (datas[i] - the_mean) * (datas[i] - the_mean)
        return sum / m

    def std(self, datas):
        m = len(datas)
        if m == 0:
            return None
        sum = 0
        the_mean = mean(datas)
        for i in range(m):
            sum = sum + (datas[i] - the_mean) * (datas[i] - the_mean)
        return sqrt(sum / m)

stat = TinyStatistician()
a = [1]
print(stat.mean(a)
print(stat.median(a))
print(stat.quartile(a, 25))
print(stat.var(a))
print(stat.std(a))



)