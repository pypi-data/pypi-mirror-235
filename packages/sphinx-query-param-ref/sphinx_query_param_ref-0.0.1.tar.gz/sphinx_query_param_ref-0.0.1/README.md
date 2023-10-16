# sphinx-query-param-ref
A Sphinx extension that adds the ability to create references with attached URL query parameters.

## Installation

Install via pip:

```
pip install sphinx-query-param-ref
```

or from source for the latest development version:

```
git clone https://github.com/peytondmurray/sphinx-query-param-ref
cd sphinx-query-param-ref
pip install .
```

## Usage

First, activate the extension by adding it to the list of extensions:

```
# conf.py

extensions = [
    "sphinx-query-param-ref",
]
```

This will add a new directive which adds references with URL query parameters to
an RST document:

```rst
.. query-param-ref:: project/examples
    :parameters: ?tags=fancy
    :ref-type: doc
    :classes: custom-link-class-name

    A fancy custom ref!
```

This node will resolve to a link to the `project/examples` document, but with
`?tags=fancy` appended to the URL. The `classes` parameter is optional, but will
add any custom html classes to the link that you want. The actual output of the
snippet above will be

```html
<div class="query-param-ref-wrapper">
    <a href="<whatever the reference to project/examples is resolved to>?tags=fancy">A fancy custom ref!</a>
</div>
```

### Documentation

The `query-param-ref` has three parameters, all of them optional:

- `parameters`: The string to append to the end of the ref URL.
- `classes`: A space-separated list of HTML classes to attach to the `<a>` element.
- `ref-type`: Type of reference this is; can be `any`, `ref`, `doc`, or `myst`.
