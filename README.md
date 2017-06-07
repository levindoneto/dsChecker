# Dangling Suffix Checker

__Author:__ Levindo Gabriel Taschetto Neto

## Basic Theory

The dangling suffix checking is a technique which might be used to test the unique decodability of a code.

## Examples

### Example 1

#### Code: A

| Symbols     | Code A  |
| ----------- |:-------:|
| A           | 0       |
| B           | 10      |
| C           | 001     |

##### High-Level execution

```python
["0", "10", "001"]
["0", "10", "001", "01"] # Because "0" is suffix of "001"
["0", "10", "001", "01", "1"] # Because "0" is suffix of "01", so the rest "1" ought be added in the list
["0", "10", "001", "01", "1", "0"] # Because "1" is suffix of "10", so the rest "0" ought be added in the list
```

Thus, during the execution, two elements with the same value were found. In this case, the code A is labeled as "not uniquely decodable"

### Example 2

## Technology used to build this checker

Python 3.6.1 which can be download [here](https://www.python.org/downloads/release/python-361/)

## License

MIT License. Click [here](LICENSE.md) for more information about this license.
