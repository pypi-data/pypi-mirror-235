# sphinx-yaml-table

A version of Sphinx's/docutil's
[csv-table](https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table)
but reads YAML to make a table instead of Sphinx.  There should be a
list of rows similar to a ListTable.  Embedded RST is OK.



## Installation

Normal Python package, `pip install sphinx-yaml-table`.

Add `sphinx_yaml_table` to the conf.py extensions.



## Example

```
.. yaml-table::

   - - a
     - b
   - - 1
     - 2
   - - test **bold**
     - test *italic*

```



## Status

This was made some time ago and is being published separately now
since it seems to work.  Changes welcome but many more changes aren't
expected.



## See also

- ???
