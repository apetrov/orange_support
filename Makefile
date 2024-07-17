pip/install:
		pip install wheel setuptools


wheel/build:
		python setup.py bdist_wheel --universal


install:
		pip install orange_support-1.0-py2.py3-none-any.whl


clean:
	rm -rf dist/ build/


