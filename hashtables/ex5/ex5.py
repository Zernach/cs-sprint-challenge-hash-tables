"""
# File Finder

Given a list of full paths to files, and a list of filenames to query,
report all the full paths that match that filename.

Example input:

```python
paths = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]

queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]
```

Example return value:

```
[ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]
```

because that's where the `foo.txt` and `ls` files are. 

The file `"nosuchfile.txt"` is ignored because it's not in the `paths`.

Return list can be in any order.

Limits:

* Up to approximately 1,000,000 paths.
* Up to approximately 1,000,000 queries.
"""

def finder(files, queries):

    file_cache = {}
    results = []

    # For each pathname in the list of files...
    for path in files:

        # Save just the filename from the path.
        filename = path.split('/')[-1]

        # If that filename is in the cache already, then add the path to the list.
        if filename in file_cache:
            file_cache[filename].append(path)

        # If not, then create it in the cache, and add the path as a new list-of-one.
        else:
            file_cache[filename] = [path]

    # For each filename in the list of queries...
    for filename in queries:

        # If the filename is in the cache, add each of its paths to the return results list.
        if filename in file_cache:
            for p in file_cache[filename]:
                results.append(p)

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
