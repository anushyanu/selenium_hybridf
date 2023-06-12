all: clean
	pytest testCases/test_login.py

clean: rmlog
	rm -f screenshots/*.png

rmlog: rmreport
	rm -f logs/*

rmreport:
	rm -f reports/assests/*

