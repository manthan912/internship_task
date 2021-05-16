import mysql.connector
# python_sql connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="manthan@12",
    database=" manthan "
)
ans = 0
a = 0

Mycur = mydb.cursor()
# select with a filter
s = "select Department.TOTAL_EMPLOYEES from Department LEFT JOIN Company ON Department.COMPANY_CODE = Company.CODE where Company.COUNTRY = 'INDIA'"
Mycur.execute(s)
myresult = Mycur.fetchall()

for x in myresult:
    ans = sum(list(x))
    a = a + ans
print(a)  # displaying the final result


