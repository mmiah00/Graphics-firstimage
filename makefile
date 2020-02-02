all: picmaker.py
	python picmaker.py
	convert pic.ppm pic.png
	
clean:
	rm pic.ppm
	rm pic.png
