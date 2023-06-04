all: clean rmlog
	pytest testCases/test_login.py

clean:
	rm -f screenshots/*.png

rmlog:
	rm -f logs/*

