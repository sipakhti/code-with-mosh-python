
def hailstone(number, step=1):
    if isinstance(number, str):
        number = int(number)
# HAILSTONE SEQUENCE PRINTING
    newline = " "
    if step % 10 == 0:
        newline = f"[{step}]\n"
    print(number, end=f"{newline}")
# RECURSION LIMITER
    if number == 1:
        print(f"\rSteps : {step} ")
        return 1
# HAILSTONE SEQUENCE CALCULATION
    elif number % 2 == 1:
        number = number * 3 + 1
    elif number % 2 == 0:
        number = number // 2

    hailstone(number,step+1)

    
hailstone(1215)

