
# Go language notes

## To create a go module

```bash
mkdir foldername && cd foldername
go mod init something.something.com/modulename
```

- That would expect the module to be downloadable from the location `https://something.something.com/modulename`.

You can also force go to load the module from local filesystem by doing something like this

```bash
go mod edit -replace something.something.com/modulename=../modulename
```

## Standard files in a module folder

Each module has some pre-defined files under it.

- `go.mod` -> contains details about this module and the modules it is dependent on using a bunch of directives. More info can be found [here](https://go.dev/doc/modules/gomod-ref).
  - `go` directive is used to specify the minimum version of go that need.
- `go.sum` -> checksum file. Could it be considered conceptually similar to `yarn.lock` file used by Yarn package manager.

## Tips

- If you don't want to run `go get github.com/google/uuid` for every import you add in your source file, use `go mod tidy`. This will fix download the dependencies and update `go.mod` file.

## Notable differences from other langs

- Type definition goes after the name.
- Interfaces are implemented implicitly i.e. inheritence is not called out explictly in the definition using some special keyword like `implements`.

## References

- [How To Code in Go - Tutorial from DigitalOcean](https://www.digitalocean.com/community/tutorial_series/how-to-code-in-go)
