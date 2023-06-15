from matplotlib import pyplot

print("*** Welcome to the loan calculator app ***\n")

def get_loan_info():
    dict = {}
    dict['loan_amount'] = float(input("Enter the loan amount : "))
    dict['interest_rate'] = float(input("Enter the interest rate : ")) / 100
    dict['monthly_payment_amount'] = float(input("Enter the monthly payment amount : "))
    dict['paid_money'] = 0
    return dict

loan = get_loan_info()
def show_loan_info(dict , m = 0):
    print("\n-------------- Loan information after " + str(m) + " months --------------")
    print("Principal : " + str(dict['loan_amount']))
    print("Rate : " + str(dict['interest_rate']))
    print("Monthly payment : " + str(dict['monthly_payment_amount']))
    print("Monthly payment : " + str(dict['paid_money']))

show_loan_info(loan)

def collect_interest(dict):
    dict['loan_amount'] += dict['loan_amount'] * loan['interest_rate'] / 12

def make_monthly_payment(dict):
    dict['loan_amount'] -= dict['monthly_payment_amount']
    if dict['loan_amount'] > 0:
        dict['paid_money'] += dict['monthly_payment_amount']
    else:
        dict['paid_money'] += dict['monthly_payment_amount'] + dict['loan_amount']
        dict['loan_amount'] = 0

def summarize_loan(dict , m , sv):
    print("\nCongratulations! You paid off your loan in", m , "months!")
    print("Your initial loan was $" + str(sv) + " at a rate of " + str(dict['interest_rate'] * 100) + "%")
    print("Your monthly payment was $" + str(dict['monthly_payment_amount']))
    print("You spent $" + str(round(dict['paid_money'] , 2)) + " in total!")
    print("You spent $" + str(round(dict['paid_money'] - sv, 2)) + " on interest!")

def create_graph(data , dict):
    xValues = []
    yValues = []
    for p in data:
        xValues.append(p[0])
        yValues.append(p[1])
    pyplot.plot(xValues , yValues)
    pyplot.title(str(100*dict['interest_rate']) + '% Interest With $' + str(dict['monthly_payment_amount']) + ' Monthly Payment.')
    pyplot.xlabel('Month Numbers')
    pyplot.ylabel('Principal Of Loan')
    pyplot.show()

input("\nPress ENTER to begin paying off your loan.")

initialLoan = loan['loan_amount']
months = 0
data = []
while loan['loan_amount'] > 0:
    points = []
    points.append(months)
    points.append(loan['loan_amount'])
    data.append(points)
    months += 1
    collect_interest(loan)
    make_monthly_payment(loan)
    show_loan_info(loan , months)
    if initialLoan < loan['loan_amount']:
        print("\nYou will never pay off your loan!")
        print("You cannot go ahead of the interest :-(")
        break
if loan['loan_amount'] <= 0:
    summarize_loan(loan, months, initialLoan)
    create_graph(data , loan)