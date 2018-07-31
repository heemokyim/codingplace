# For csv
list_with_header <- read.csv('r_example/example_studentlist.csv')
list_without_header <- read.csv('r_example/example_studentlist.csv', header=F)

# For txt
table_without_header <- read.table('r_example/studentlist.txt')
table_with_header <- read.table('r_example/studentlist.txt', header=T)
table_sep <- read.table('r_example/studentlist2.txt', header=T, sep=';')

# read.csv() == header=T
# read.table() == header=F

install.packages('readxl')
library('readxl')

# For excel
df <- read_excel(path='r_example/studentlist.xlsx', sheet='Sheet1', col_names=TRUE)

# Ctrl C, Ctrl V
# 1. Ctrl C from Excel file's area
# 2. below
StudentList <- read.delim('clipboard')

# ---------------------------------

# Install library from Github, Follow below

# 1.
install.packages('devtools')
library('devtools')

# 2. install_github('PACKAGE_NAME')
install_github('yihui/knitr')

