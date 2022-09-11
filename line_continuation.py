gross_wages = 125000
taxable_interest = 6000
dividends = 500
qualified_dividends = 0
ira_deduction = 6000
student_loan_interest = 10000

# this is a long line: it is over 100 characters long
income = gross_wages + taxable_interest + (dividends - qualified_dividends) - ira_deduction - student_loan_interest

# same line wrapped over several lines using backslash
income2 = gross_wages \
          + taxable_interest \
          + (dividends - qualified_dividends) \
          - ira_deduction \
          - student_loan_interest

assert income == income2


# check this out:
x = 10
assert x == (x)

# same line can be wrapped in parenthesis
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

# the preferred approach is to break the
# line before the mathematical operators
income = (gross_wages
            + taxable_interest
            + (dividends - qualified_dividends)
            - ira_deduction
            - student_loan_interest)
