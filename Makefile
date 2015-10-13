# This file is part of portolan.
# http://github.com/fitnr/portolan

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

README.rst: README.md
	pandoc $< -o $@ || cp $< $@

.PHONY: deploy
deploy: README.rst
	rm -r dist
	python3 setup.py bdist_wheel
	twine upload dist/*
