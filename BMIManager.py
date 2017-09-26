# -*- coding: utf-8 -*-
class ZeroEnterError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def enterHight():
    try:
        hight = float(raw_input('>>'))
        print isinstance(hight,float)
        print hight <= 0
        if isinstance(hight,float) and hight <= 0:
            print "test"
            raise ZeroEnterError(hight)
        return hight
    except ZeroEnterError as e:
        print e.value
    except:
        print "Error enter !! Please enter again your hight !"
        enterHight()
    


def enterWeight():
    try:
        weight = float(raw_input('>>'))
        if weight <= 0:
            raise ZeroEnterError(weight)
        return weight
    except:
        print "Error enter !! Please enter again your weight !"
        enterWeight()


while True:
    print "Please enter your hight"
    print ""
    hight = enterHight()

    print "Please enter your body weight"
    print ""
    weight = enterWeight()

    try:
        bmi = weight / ((hight / 100) ** 2)
    except:
        print "Error Culateor ! Please Check Your Enter !!"
        print ""
        print "Do you restart again ? [Y/N]"
        print ""
        is_again = str(raw_input('>>'))
        if is_again == "Y":
            continue
        else:
            break
    else:
        print "Body weight normal range is BMI=18.5～24"
        print ""
        print "Your BMI is %f" % bmi
        print ""

        if 18.5 <= bmi <= 24:
            print "Your body weight is normal !!"
            print ""
        else:
            print "You must control your weight"
            print ""

        print "Do you restart again ? [Y/N]"
        print ""
        is_again = str(raw_input('>>'))
        if is_again == "Y":
            continue
        else:
            break
