from time import sleep, time


def ft_progress(lst):
    for x in lst:
        yield x / len(lst)


listy = range(3333)
ret = 0
eta = 0
beginTime = time()
for fraction in ft_progress(listy):
    # ret += (fraction + 3) % 5
    percentage = fraction * 100
    bar = '=' * int(percentage / 5) + '>'
    elapsed_time = time() - beginTime
    if fraction > 0:
        eta = elapsed_time / fraction - elapsed_time
    print("\rETA: {:5.2f}s [{:3.2f}%][{:20}] {:4}/{:4} | elapsed time {:.2f}s"
          .format(eta, percentage, bar, int(fraction * len(listy)), len(listy),
                  elapsed_time), end='')
    sleep(0.01)

print()
# print(ret)
