## selenium_hybridf

nopcommerce.com/demo - backend testing

step 1: install packages

selenium - python library
pytest  - python unittest framework
pytest-html - pytest html reports
pytest-xdist - run test parallel
openpyxl - ms excel support
allure-pytest - to generate allure reports

step 2: create folder structure

pageObjects (package)
testcase - (package)
utilities - (package)
testdata - (folder)
configuration - (folder)
logs -     (folder)
reports -    (folder)
screenshots -   (folder)
run.bat

step 3: automating login testcase
create loginPage object class under pageobjects
create logintest under testcases
create conftest.py under testcases

step 4: capture screenshot under failures
update login test with screenshot under testcases

step 5: read common values from ini file
# such base url , username ,pwd are everytime needed for login to website
add "config.ini" file (is not a python file, no rules ) under configurations folder
create "readProperties.py" utility file under utility package to read common data
# utility file will read the data from ini file and provide the data to the testcases, it is resuability feature
replace hard coded values in login testcases

step 6 : add logs to test case
add customLogger.py under utilities package
add logs to login test

step 7 : run test on desired browser/cross browser/run parallel
update conftest.py with required fixtures which will accept command line argument(browser)
pass browser name as a argument in the command line

step 7.1 : to run tests on desired browser
pytest -s -v testCases/test_login.py --browser chrome
pytest -s -v testCases/test_login.py --browser firefox

step 7.2: to run tests parallel (max -n=3 , if more then it will be slower)
pytest -s -v -n=2 testCases/test_login.py --browser chrome
pytest -s -v -n=2 testCases/test_login.py --browser firefox

step 8: Generate  pytest HTML Reports
update conftest.py with html hooks
to generate html reports run the below command
pytest -s -v -n=2 --html=Reports/report.html testCases/test_login.py --browser chrome

step 9 : Automating Data Driven test case
prepare test data in excel sheet, place the excel inside the testData folder
create xlutils.py under utilities package
create login_data_driven_test under testCases
run the test case

step 10: add new testcases
add new customer
search customer by name
search customer by email

