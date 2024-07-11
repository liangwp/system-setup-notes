# Complex Commands on Bash

A collection of useful things that can be done in bash but may be a bit
difficult/troublesome.

## Counting lines of code

* Total lines of code in python code base
    ```
    find . -type f -name '*.py' -not -path '*/.venv/*' -exec awk 1 {} + | wc -l
    ```

* Total lines of code in javascript code base
    ```
    find . -type f -name '*.js' -not -path '*/node_modules/*' -exec awk 1 {} + | wc -l
    ```

Reference:

* https://stackoverflow.com/questions/62556953/trying-to-do-total-word-count-on-all-files-recursively-but-the-sum-is-not-right