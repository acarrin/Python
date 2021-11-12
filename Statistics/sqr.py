#############################################################
# Program Name: Exercise 2.8                                #
#															#
# Date: 2020-09-01                                          #
#															#
# Descrption: my square roots function						#
#															#
# Author: AceITnow                                          #
#############################################################

import math


def calculateSqr(n, terms):    

    Xk = 1

    for i in range(terms):
        Xk = 1/2.0 * (Xk + float(n)/Xk)

    return Xk
