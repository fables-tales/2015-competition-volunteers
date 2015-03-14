import csv
from collections import Counter

if __name__ == "__main__":

    reader = csv.reader(open("responses.csv"))
    reader.next()

    build = Counter()

    for r in reader:
        for time in r[6].split(","):
            time = time.strip()
            build[time] += 1


    def sorter(key):
        if "Thursday" in key:
            return 0
        elif "Friday" in key:
            if "9am" in key:
                return 1000
            else:
                return 1001
        elif "Saturday" in key:
            if "8am" in key:
                return 2000
            else:
                return 2001
        elif "Sunday" in key:
            if "onwards" in key:
                return 3500
            return 3000

    ml = max([len(x) for x in build.keys()])+1
    for key in sorted(build.keys(), key=sorter):
        value = build[key]
        print str(key).rjust(ml), value

    plt.show()
