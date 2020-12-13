# Income_tax_simple_program


def no_tax():
    print("NO need to pay tax")
    answer()


def self():
    back_the_program = True
    while back_the_program:
        start = input("Typing 'RESTART' to restart the program ")
        if start == "RESTART":
            return pit()
        else:
            return self()


def answer():
    answer = input("Do you want enter other amount ? 'Y' or 'N' ").upper()
    print(answer)
    if answer == "Y":
        return pit()
    else:
        return self()


def pit():
    income = float(input("Enter the annual income: "))
    tax_backet_1 = 85528.00
    keep_continue = True
    while keep_continue:
        if income <= tax_backet_1:
            tax = income * 0.18 - 556.02
            tax = round(tax, 0)
            if tax < 0:
                return no_tax()
            print("The tax is $ :", format(tax, ",.2f") + " USD")
            # print("The tax is:", tax, "thalers")
            answer()

        elif income > tax_backet_1:
            tax = (income - tax_backet_1) * 0.32 + 14839.02
            tax = round(tax, 0)
            print("The tax is $ : ", format(tax, ",.2f") + " USD")

            answer()
pit()
M
