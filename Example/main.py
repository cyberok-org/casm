green = 3.9
yellow = 6.99
orange = 8.99
red = 9.49


with open("cve.csv") as file:
    lines = file.readlines()
lines.sort()

ip = "0"
data = dict()

f = open("score.csv", "w")

score = ts_storm = ts_red = ts_orange = ts_yellow = ts_green = 0.0
n_storm = n_red = n_orange = n_yellow = n_green = 0

for i in lines:
    ls = i.split("|")

    if ip != ls[0]:
        if ip != "0":
            f.write(ip + "|")

            if ts_storm != 0:
                f_storm = round(1000-7600/(ts_storm+28.5))
            else:
                f_storm = 0
            f.write(str(n_storm) + "|" + str(round(ts_storm, 1)) + "|" + str(f_storm) + "|")

            if ts_red != 0:
                f_red = round(799-7092.36/(ts_red+26.64))
            else:
                f_red = 0
            f.write(str(n_red) + "|" + str(round(ts_red, 1)) + "|" + str(f_red) + "|")

            if ts_orange != 0:
                f_orange = round(599-5516.28/(ts_orange+20.72))
            else:
                f_orange = 0
            f.write(str(n_orange) + "|" + str(round(ts_orange, 1)) + "|" + str(f_orange) + "|")

            if ts_yellow != 0:
                f_yellow = round(399-3152.16/(ts_yellow+11.84))
            else:
                f_yellow = 0
            f.write(str(n_yellow) + "|" + str(round(ts_yellow, 1)) + "|" + str(f_yellow) + "|")

            if ts_green != 0:
                f_green = round(199-950.4/(ts_green+3.6))
            else:
                f_green = 0
            f.write(str(n_green) + "|" + str(round(ts_green, 1)) + "|" + str(f_green) + "|")

            score = 1000-max([f_storm, f_red, f_orange, f_yellow, f_green])

            f.write(str(round(score)) + "|")

            if score <= 200:
                f.write("Шторм\n")
            elif score <= 500:
                f.write("Низкий\n")
            elif score < 800:
                f.write("Средний\n")
            else:
                f.write("Высокий\n")



        ip = ls[0]
        score = ts_storm = ts_red = ts_orange = ts_yellow = ts_green = 0.0
        n_storm = n_red = n_orange = n_yellow = n_green = 0

    ts = float(ls[2])

    if ts > red:
        ts_storm += ts
        n_storm += 1
    elif ts > orange:
        ts_red += ts
        n_red += 1
    elif ts > yellow:
        ts_orange += ts
        n_orange += 1
    elif ts > green:
        ts_yellow += ts
        n_yellow += 1
    else:
        ts_green += ts
        n_green += 1
