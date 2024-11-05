import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('programming_quiz.db')  # Use a generic name for the database file
c = conn.cursor()

# Create a table for the quiz questions
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS "DS 4220" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                answer TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS "DS 3850" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                answer TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS "FIN 3210" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                answer TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS "DS 4210" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                option1 TEXT,
                option2 TEXT,
                option3 TEXT,
                option4 TEXT,
                answer TEXT)''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS "ECON 4990" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            answer TEXT) ''')
    conn.commit()

# Create questions and a function to put them in a table
def insert_questions():
    ds4220questions = [
        ('What function is used to create a vector in R?', 'c()', 'v()', 'vec()', 'vector()', 'c()'),
        ('How do you assign a value to a variable in R?', '=', '<-', '->', '==', '<-'),
        ('Which function is used to calculate the mean of a numeric vector in R?', 'average()', 'sum()', 'mean()', 'median()', 'mean()'),
        ('What type of object is created by the data.frame() function in R?', 'List', 'Vector', 'Data frame', 'Matrix', 'Data frame'),
        ('What symbol is used for comments in R?', '//', '#', '/* */', '--', '#'),
        ('Which function is used to read a CSV file into R?', 'read()', 'read.csv()', 'csv.read()', 'import.csv()', 'read.csv()'),
        ('How can you display the structure of an R object?', 'str()', 'summary()', 'structure()', 'print()', 'str()'),
        ('Which function is used to create a sequence of numbers in R?', 'seq()', 'range()', 'sequence()', 'rep()', 'seq()'),
        ('What does the nrow() function return for a data frame in R?', 'The number of columns', 'The number of rows', 'The number of elements', 'The row names', 'The number of rows'),
        ('Which function is used to install a package in R?', 'install()', 'library()', 'install.packages()', 'download.packages()', 'install.packages()')
    ]
    ds3850questions = [
        ('Which function is used to output text to the console in Python?', 'print()', 'echo()', 'write()', 'output()', 'print()'),
        ('What is the correct way to create a variable in Python?', 'x = 10', 'int x = 10', 'let x = 10', 'x <- 10', 'x = 10'),
        ('Which of the following is a valid list in Python?', '[1, 2, 3]', '{1, 2, 3}', '(1, 2, 3)', '<1, 2, 3>', '[1, 2, 3]'),
        ('Which operator is used for exponentiation in Python?', '^', '**', 'pow()', '%', '**'),
        ('Which of these keywords is used to define a function in Python?', 'fun', 'function', 'def', 'define', 'def'),
        ('How do you get the length of a list in Python?', 'len(list)', 'length(list)', 'size(list)', 'count(list)', 'len(list)'),
        ('Which of the following is a correct way to write a loop in Python?', 'for i in range(5):', 'for (i = 0; i < 5; i++)', 'loop i in range(5)', 'foreach (i: 5)', 'for i in range(5):'),
        ('How do you create a comment in Python?', '# This is a comment', '// This is a comment', '/* This is a comment */', '-- This is a comment', '# This is a comment'),
        ('Which of the following data structures is mutable in Python?', 'Tuple', 'Set', 'String', 'List', 'List'),
        ('What will 5 // 2 return in Python?', '2.5', '2', '3', '1', '2')
    ]
    fin3210questions = [
        ('What is the primary goal of financial management?', 'Profit Maximization', 'Cost Reduction', 'Risk Avoidance', 'Maximization of shareholder wealth', 'Maximization of shareholder wealth'),
        ('What is the formula for the current ratio?', 'Current Assets / Current Liabilities', 'Total Assets / Total Liabilities', 'Net Income / Total Liabilities', 'Current Liabilities / Current Assets', 'Current Assets / Current Liabilities'),
        ('Which financial statement shows a firm’s revenues and expenses over a period of time?', 'Balance Sheet', 'Income Statement', 'Cash Flow Statement', 'Statement of Retained Earnings', 'Income Statement'),
        ('What is the time value of money principle?', 'Money today is worth less than money in the future', 'Money today is worth more than money in the future', 'Money today and in the future have the same value', 'Money value is independent of time', 'Money today is worth more than money in the future'),
        ('What is the formula for calculating the present value?', 'FV / (1 + r)^t', 'PV * (1 + r)^t', 'FV * (1 + r)^t', 'PV / r', 'FV / (1 + r)^t'),
        ('Which ratio is used to measure a company’s ability to meet short-term obligations?', 'Debt-to-equity ratio', 'Current ratio', 'Quick ratio', 'Return on equity', 'Current ratio'),
        ('What is the risk-return tradeoff?', 'Higher risk leads to lower returns', 'Higher risk leads to higher returns', 'Risk and returns are not related', 'Lower risk leads to higher returns', 'Higher risk leads to higher returns'),
        ('What is the purpose of a capital budget?', 'To determine daily expenses', 'To evaluate and plan for long-term investments', 'To reduce short-term debts', 'To calculate monthly profits', 'To evaluate and plan for long-term investments'),
        ('Which formula is used to calculate net working capital?', 'Current Assets - Current Liabilities', 'Total Assets - Total Liabilities', 'Net Income + Current Liabilities', 'Current Assets + Current Liabilities', 'Current Assets - Current Liabilities'),
        ('What does the debt-to-equity ratio indicate?', 'A company’s profitability', 'A company’s total revenue', 'A company’s liquidity', 'The proportion of a company’s funding that comes from debt versus equity', 'The proportion of a company’s funding that comes from debt versus equity')
    ]
    ds4210questions = [
        ('What is the primary purpose of data visualization?', 'To generate raw data', 'To display data in a graphical format for easier interpretation', 'To store data securely', 'To create complex algorithms', 'To display data in a graphical format for easier interpretation'),
        ('Which of the following is a common type of chart used in Tableau for showing relationships between two variables?', 'Bar Chart', 'Pie Chart', 'Scatter Plot', 'Line Chart', 'Scatter Plot'),
        ('In Power BI, which visual is used to show the composition of a whole?', 'Line Chart', 'Pie Chart', 'Table', 'Map', 'Pie Chart'),
        ('What feature in Tableau allows you to segment data into different categories for analysis?', 'Filters', 'Groups', 'Parameters', 'Calculated Fields', 'Groups'),
        ('Which of the following tools is primarily used for creating dashboards and reports in Power BI?', 'Power Query', 'Power Pivot', 'Power View', 'Power BI Desktop', 'Power BI Desktop'),
        ('What type of chart is best used to show trends over time in both Tableau and Power BI?', 'Bar Chart', 'Histogram', 'Line Chart', 'Scatter Plot', 'Line Chart'),
        ('In Tableau, what is the term for the visual representation of data based on filters, dimensions, and measures?', 'Dashboard', 'Worksheet', 'Story', 'Visualization', 'Worksheet'),
        ('Which feature in Power BI allows you to connect to multiple data sources?', 'Query Editor', 'Data Model', 'Report View', 'Power Query', 'Power Query'),
        ('What is the purpose of using a calculated field in Tableau?', 'To combine different data sources', 'To create new data from existing data', 'To import data', 'To export data', 'To create new data from existing data'),
        ('Which of the following visual types should be avoided when comparing more than five categories?', 'Bar Chart', 'Pie Chart', 'Line Chart', 'Scatter Plot', 'Pie Chart')
    ]
    econ4990questions = [
        ('What is the primary focus of industrial organization in the context of sports economics?', 'The study of labor markets', 'The analysis of market structures and competition in the sports industry', 'The evaluation of public funding for sports facilities', 'The examination of consumer behavior in sports', 'The analysis of market structures and competition in the sports industry'),
        ('In labor economics, what is the primary factor that influences player salaries in professional sports?', 'Market demand for sports', 'Player performance metrics', 'Team revenues and profitability', 'All of the above', 'All of the above'),
        ('What is the concept of "salary cap" in professional sports leagues?', 'A limit on the number of players a team can sign', 'A limit on the total salary a team can pay its players', 'A minimum salary requirement for players', 'A penalty for exceeding player salaries', 'A limit on the total salary a team can pay its players'),
        ('Which economic principle explains why some sports teams are able to generate higher revenues than others?', 'Price elasticity of demand', 'Competitive advantage', 'Opportunity cost', 'Market equilibrium', 'Competitive advantage'),
        ('What role does public finance play in the construction of sports facilities?', 'Governments provide funding to ensure teams remain competitive', 'Public funds are often used to finance stadiums to stimulate local economies', 'It helps determine ticket prices for sporting events', 'It regulates player contracts', 'Public funds are often used to finance stadiums to stimulate local economies'),
        ('How does the concept of externalities apply to professional sports?', 'They refer to the positive and negative effects that sports teams have on the local community', 'They are irrelevant in the context of sports economics', 'They only pertain to player performance', 'They are solely related to ticket pricing', 'They refer to the positive and negative effects that sports teams have on the local community'),
        ('In the context of sports economics, what does "monopoly" refer to?', 'A single team dominating the league', 'A market structure where a single entity controls the entire sports industry', 'A situation where multiple teams have equal market power', 'A competitive balance among teams', 'A market structure where a single entity controls the entire sports industry'),
        ('Which of the following factors can lead to wage discrimination in professional sports?', 'Player performance statistics', 'Gender and racial biases', 'Team market size', 'All of the above', 'All of the above'),
        ('What is the purpose of revenue sharing among teams in a sports league?', 'To reduce competitive balance', 'To ensure all teams have the financial means to compete', 'To lower ticket prices for consumers', 'To increase player salaries', 'To ensure all teams have the financial means to compete'),
        ('What economic concept explains the phenomenon of "winner-takes-all" in sports leagues?', 'Market competition', 'Inequality in revenue distribution', 'Public goods theory', 'Utility maximization', 'Inequality in revenue distribution')
    ]

    c.executemany('''INSERT INTO "DS 4220" (question, option1, option2, option3, option4, answer)
                     VALUES (?, ?, ?, ?, ?, ?)''', ds4220questions)
    c.executemany('''INSERT INTO "DS 3850" (question, option1, option2, option3, option4, answer)
                     VALUES (?, ?, ?, ?, ?, ?)''', ds3850questions)
    c.executemany('''INSERT OR IGNORE INTO "FIN 3210" (question, option1, option2, option3, option4, answer)
                     VALUES (?, ?, ?, ?, ?, ?)''', fin3210questions)
    c.executemany('''INSERT OR IGNORE INTO "DS 4210" (question, option1, option2, option3, option4, answer)
                     VALUES (?, ?, ?, ?, ?, ?)''', ds4210questions)
    c.executemany('''INSERT OR IGNORE INTO "ECON 4990" (question, option1, option2, option3, option4, answer)
                     VALUES (?, ?, ?, ?, ?, ?)''', econ4990questions)
    conn.commit()

# Create each table and insert the questions
create_table()
insert_questions()

# Close the connection
conn.close()

print("Questions and answers have been saved to the DS 4220 table in the database.")
print("Questions and answers have been saved to the DS 3850 table in the database.")
print("Questions and answers have been saved to the FIN 3210 table in the database.")
print("Questions and answers have been saved to the DS 4210 table in the database.")
print("Questions and answers have been saved to the ECON 4990 table in the database.")