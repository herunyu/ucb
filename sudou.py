"""Generate input for sudou using SAT Solver (STP)"""

booleans = ""
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            booleans += "x" + str(i) + str(j) + str(k)
            if k != 9:
                booleans += ","
            booleans += " "
        booleans += ": BOOLEAN;\n"

""" Initialization """
existence = "ASSERT(x263 AND x288 AND x295 AND x331 AND x352 AND x445 AND x467 AND x534 AND x571 "
existence += "AND x629 AND x715 AND x787 AND x793 AND x832 AND x851 AND x954 AND x999);\n"

cells = ""
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            cells += "ASSERT(x" + str(i) + str(j) + str(k) + " <=> "
            for l in range(1,10):
                if l != k:
                    cells += "NOT(x" + str(i) + str(j) + str(l) + ") "
                    if k != 9 and l != 9 :
                        cells += "AND "
                    elif k == 9 and l != 8:
                        cells += "AND "
            cells += ");\n"

rows = ""
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            rows += "ASSERT(x" + str(i) + str(k) + str(j) + " <=> "
            for l in range(1,10):
                if l != k:
                    rows += "NOT(x" + str(i) + str(l) + str(j) + ") "
                    if k != 9 and l != 9 :
                        rows += "AND "
                    elif k == 9 and l != 8:
                        rows += "AND "
            rows += ");\n"

columns = ""
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            columns += "ASSERT(x" + str(k) + str(i) + str(j) + " <=> "
            for l in range(1,10):
                if l != k:
                    columns += "NOT(x" + str(l) + str(i) + str(j) + ") "
                    if k != 9 and l != 9 :
                        columns += "AND "
                    elif k == 9 and l != 8:
                        columns += "AND "
            columns += ");\n"

blocks = ""
for a in range(3):
    for i in range(1+a*3,4+a*3):
        for b in range(3):
            for j in range(1+b*3,4+b*3):
                for k in range(1,10):
                    blocks += "ASSERT(x" + str(i) + str(j) + str(k) + " <=> "
                    for l in range(1+a*3,4+a*3):
                        for m in range(1+b*3,4+b*3):
                            if i == 3+a*3 and j == 3+b*3 and (m != j or l != i):
                                blocks += "NOT(x" + str(l) + str(m) + str(k) + ") "
                                if m != 2+b*3 or l != 3+a*3:
                                    blocks += "AND "
                            elif m != j or l != i:
                                blocks += "NOT(x" + str(l) + str(m) + str(k) + ") "
                                if m != 3+b*3 or l != 3+a*3:
                                    blocks += "AND "
                    blocks += ");\n"

toInput = booleans + existence + cells + rows + columns + blocks

with open("Input.txt", "w") as text_file:
    text_file.write("{}".format(toInput))








