
.venv:
	# creating environ
	python3 -m venv .venv
	.venv/bin/pip install -U pip setuptools wheel

install:
	.venv/bin/pip install -e .

clean:
	# remove environ
	-rm -rf .venv
	# remove logs
	-rm *.log