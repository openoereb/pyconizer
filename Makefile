OPERATING_SYSTEM ?= LINUX

VENV_FLAGS ?=

REQUIREMENTS ?= requirements.txt

ifeq ($(CI),true)
  PYTHON_VENV = do-pip
  VENV_BIN =
else
  PYTHON_VENV=.venv/requirements-timestamp
  ifeq ($(OPERATING_SYSTEM), WINDOWS)
    VENV_BIN = .venv/Scripts/
    VENV_FLAGS += --system-site-packages
    PYTHON_BIN_POSTFIX = .exe
  else
    VENV_BIN ?= .venv/bin/
    PYTHON_BIN_POSTFIX =
  endif
endif

SPHINXOPTS =
SPHINXBUILD = $(VENV_BIN)sphinx-build$(PYTHON_BIN_POSTFIX)
SPHINXPROJ = PYCONIZER
SOURCEDIR = doc/source
BUILDDIR = doc/build

install: $(PYTHON_VENV)

.venv/timestamp:
	virtualenv $(VENV_FLAGS) .venv
	touch $@

.venv/requirements-timestamp: .venv/timestamp setup.py $(REQUIREMENTS)
	$(VENV_BIN)pip$(PYTHON_BIN_POSTFIX) install -r $(REQUIREMENTS)
	touch $@

.PHONY: do-pip
do-pip:
	pip install --upgrade -r $(REQUIREMENTS)

$(SPHINXBUILD): .venv/requirements-timestamp
	$(VENV_BIN)pip$(PYTHON_BIN_POSTFIX) install Sphinx sphinxcontrib-napoleon sphinx_rtd_theme

.PHONY: doc
doc: $(SPHINXBUILD)
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: checks
checks: git-attributes lint coverage-html

.PHONY: tests
tests: .coverage

.coverage: $(PYTHON_VENV) .coveragerc $(shell find -name "*.py" -print)
	$(VENV_BIN)py.test$(PYTHON_BIN_POSTFIX) -vv --cov-config .coveragerc --cov-report term-missing:skip-covered --cov pyconizer tests

.PHONY: lint
lint: $(PYTHON_VENV)
	$(VENV_BIN)flake8$(PYTHON_BIN_POSTFIX)

.PHONY: git-attributes
git-attributes:
	git --no-pager diff --check `git log --oneline | tail -1 | cut --fields=1 --delimiter=' '`

.PHONY: coverage-html
coverage-html: coverage_report/index.html

coverage_report/index.html: $(PYTHON_VENV) .coverage
	$(VENV_BIN)coverage$(PYTHON_BIN_POSTFIX) html

.PHONY: clean-all
clean-all:
	rm -rf .venv
	rm -rf $(BUILDDIR)

.PHONY: deploy
deploy:
	$(VENV_BIN)python setup.py sdist bdist_wheel upload
