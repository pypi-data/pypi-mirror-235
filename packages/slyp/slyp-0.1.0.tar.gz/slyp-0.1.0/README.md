# SLYP

Stephen Lints Your Python

[![PyPI - Version](https://img.shields.io/pypi/v/click-type-test.svg)](https://pypi.org/project/click-type-test)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/click-type-test.svg)](https://pypi.org/project/click-type-test)

-----

**Table of Contents**

- [Hi](#Hi)
- [Installation](#installation)
- [Usage](#usage)
- [Implemented Rules](#implemented-rules)
- [License](#license)

## Hi

:wave:

I'm Stephen. I'm going to lint your Python code.

I wrote this linter because nothing else out there implemented these rules, and
some of them needed CST (rather than AST), so there was no plugin framework
(e.g. flake8 plugins) which I could use.
I hope it helps you catch slyp-ups.

## Installation

`slyp` is a python package and can be run as a pre-commit hook.

On supported python versions, it should be installed with

```console
pip install slyp
```

## Usage

Either use it as a CLI tool:

```console
slyp src/
```

Or as a pre-commit hook using the following `pre-commit-config.yaml`:

```yaml
- repo: https://github.com/sirosen/slyp
  rev: 0.0.3
  hooks:
    - id: slyp
```

### Options and Arguments

`[files...]`: If passed positional arguments, `slyp` will treat them as
filenames to check.
Otherwise, it will search the current directory for python files.

`-v/--verbose`: Enable more verbose output

`--use-git-ls`: Find files to check by doing a `git ls-files` call and filtering
the results to files which appear to be python.
This is mutually exclusive with any filename arguments.

`--disable CODES`: Pass a comma-delimited list of codes to turn off.

`--enable CODES`: Pass a comma-delimited list of codes to turn on.

## Implemented Rules

<!-- generate-reference-insert-start -->

E is for "error" (you should probably change this)

W is for "warning" (you might want to change this)

Some warnings are disabled by default; enable them with `--enable`.

### E100

'unnecessary string concat'

    x = "foo " "bar"

### W101

'unparenthesized multiline string concat in keyword arg'

    foo(
        bar="alpha "
        "beta"
    )

### W102

'unparenthesized multiline string concat in dict value'

    {
        "foo": "alpha "
        "beta"
    }

### W103

'unparenthesized multiline string concat in collection type'

    x = (  # a tuple
        "alpha "
        "beta",
        "gamma"
    )
    x = {  # or a set
        "alpha "
        "beta",
        "gamma"
    }

### E110

'returning a variable chedked as None, rather than returning None'

    if x is None:
        return x  # should be `return None`

### W200

'two AST branches have identical contents'

    if x is True:
        return y + 1
    else:
        # some comment
        return y + 1

### W201

_disabled by default_

'two AST branches have identical trivial contents'

    if x is True:
        return
    else:
        return

### W202

_disabled by default_

'two non-adjacent AST branches have identical contents'

    if x is True:
        return foo(bar())
    elif y is True:
        return 0
    elif z is True:
        return 1
    else:
        return foo(bar())

### W203

_disabled by default_

'two non-adjacent AST branches have identical trivial contents'

    if x is True:
        return None
    elif y is True:
        return 0
    elif z is True:
        return 1
    else:
        return None

<!-- generate-reference-insert-end -->

## License

`slyp` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
