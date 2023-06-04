all: clean
	pytest testCases/test_login.py

clean: rmlog
	rm -f screenshots/*.png

rmlog:
	rm -f logs/*

