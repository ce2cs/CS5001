"""
Write a program that completes and prints out the following truth table.
Recall from this module that a truth table contains all of the possible combination of p, q, and r.
You should use the |, -, and + to build the lines in the table.
p	q	r	A	B
F	F	F	?	?
F	F	T	?	?
F	T	F	?	?
F	T	T	?	?
T	F	F	?	?
T	F	T	?	?
T	T	F	?	?
T	T	T	?	?
"""

FORMAT_TRUE = " T "
FORMAT_FALSE = " F "

def main():
    print("+---" * 5 + "+")
    print("|" + "|".join([" p ", " q ", " r ", " A ", " B "]) + "|")
    for p_str in [FORMAT_FALSE, FORMAT_TRUE]:
        for q_str in [FORMAT_FALSE, FORMAT_TRUE]:
            for r_str in [FORMAT_FALSE, FORMAT_TRUE]:
                p = p_str == FORMAT_TRUE
                q = q_str == FORMAT_TRUE
                r = r_str == FORMAT_TRUE
                A = (p and q) or not r
                A_str = FORMAT_TRUE if A else FORMAT_FALSE
                B = not(p and (q or not r))
                B_str = FORMAT_TRUE if B else FORMAT_FALSE
                print("+---" * 5 + "+")
                print("|" + "|".join([p_str, q_str, r_str, A_str, B_str]) + "|")
    print("+---" * 5 + "+")


if __name__ == '__main__':
    main()
