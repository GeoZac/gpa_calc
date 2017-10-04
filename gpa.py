def gpa2per(gpa):
    per = 10 * gpa - 3.75
    return per


# set total credit
def setsem(sem):
    global totalcre
    if sem == 1:
        totalcre = float(22)
    if sem == 2:
        totalcre = float(19)
    if sem == 3:
        totalcre = float(14)
    if sem == 4:
        totalcre = float(12)
    return totalcre


def gpacalc1(sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sem):
    totalcre = setsem(sem)
    sub1 = float(sub1)
    sub2 = float(sub2)
    sub3 = float(sub3)
    sub4 = float(sub4)
    sub5 = float(sub5)
    sub6 = float(sub6)
    sub7 = float(sub7)
    sub8 = float(sub8)
    gpa = (sub1 * 3) + (sub2 * 4) + (sub3 * 4) + (sub4 * 3) + (sub5 * 3) + (sub6 * 2) + (sub7 * 2) + (sub8 * 1)
    gpa = gpa / totalcre
    return gpa


def gpacalc2(sub1, sub2, sub3, sub4, sub5, sub6, sub7, sem):
    totalcre = setsem(sem)
    sub1 = float(sub1)
    sub2 = float(sub2)
    sub3 = float(sub3)
    sub4 = float(sub4)
    sub5 = float(sub5)
    sub6 = float(sub6)
    sub7 = float(sub7)
    gpa = (sub1 * 4) + (sub2 * 3) + (sub3 * 3) + (sub4 * 3) + (sub5 * 3) + (sub6 * 2) + (sub7 * 1)
    gpa = gpa / totalcre
    return gpa


def gpacalc3(sub1, sub2, sub3, sub4, sem):
    totalcre = setsem(sem)
    sub1 = float(sub1)
    sub2 = float(sub2)
    sub3 = float(sub3)
    sub4 = float(sub4)
    gpa = (sub1 * 3) + (sub2 * 3) + (sub3 * 2) + (sub4 * 6)
    gpa = gpa / totalcre
    return gpa


# sem4 with 1 sub
def gpacalc4(sub1, sem):
    totalcre = setsem(sem)
    sub1 = float(sub1)
    gpa = (sub1 * 12)
    gpa = gpa / totalcre
    return gpa
