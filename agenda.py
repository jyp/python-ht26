
def load_agenda(file_name):
    result = []
    with open(file_name) as f:
        for line in f:
            fields = line.split()
            result.append((int(fields[0]),int(fields[1]),fields[2]))
    return result

def tabulate_agenda(agenda):
    # assumption: a day has 24 hours.
    result = []
    for i in range(24):
        empty_agenda_for_one_hour = []
        result.append(empty_agenda_for_one_hour)
    for (start,stop,task) in agenda:
        for hour in range(start,stop+1):
            result[hour].append(task)
    return result

def pretty_print_agenda(a):
    for i in range(len(a)):
        print(i,a[i])
pretty_print_agenda(tabulate_agenda(load_agenda("agenda.txt")))
