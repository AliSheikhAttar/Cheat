## Modules

- new module
* takes dependencie for configing packages
```bash
go mod init <path>
```

- run main function in main package
```bash
go run .
```

- download library/package and add to project
* -u for latest version
* after running this, `require` codes will be appended to go.mod which are the libraries and their dependancies
* in go.sum, some hashes for security will be appended (like package.json in js)
```go
go get -u <library>
```


- synchronize the module's dependencies, adding those required by the code, but not yet tracked in the module
```bash
go mod tidy
```

- redirect the Go tools to the local directory where the specific module is
```bash
go mod edit -replace example.com/greetings=../greetings
```

- test functions
```bash
go test
```

- test functions with verbose output
```bash
go test -v
```

- compile to executable
```bash
go build
```

The install directory is controlled by the GOPATH and GOBIN environment variables. If GOBIN is set, binaries are installed to that directory. If GOPATH is set, binaries are installed to the bin subdirectory of the first directory in the GOPATH list. Otherwise, binaries are installed to the bin subdirectory of the default GOPATH ($HOME/go or %USERPROFILE%\go).

You can use the go env command to portably set the default value for an environment variable for future go commands:

```bash
go env -w GOBIN=/somewhere/else/bin
```

- To unset a variable previously set by go env -w, use go env -u:
```bash
go env -u GOBIN
```

- discover the install path 
```bash
go list -f '{{.Target}}'
```

- Add the Go install directory to system's shell path
```bash
echo 'export PATH=$PATH:/home/asa/go/bin' >> ~/.bashrc
source ~/.bashrc
```

- already have a directory like $HOME/bin in your shell path and 'd like to install Go programs there, change the install target by setting the GOBIN variable
```bash
go env -w GOBIN=/path/to/your/bin
```

- compile and install the package
```bash
go install
```

- Download the package and add dependency
```bash
go get golang.org/x/example/hello/reverse
```

- Initialize the workspace and add modules in dir
```bash
go work init ./<dir>/
```

- Add module to workspace
```bash
go work use <./example/hello>
```

- adds a use directive to the go.work file for dir, if it exists, and removes the use directory if the argument directory doesn’t exist.
The -r flag examines subdirectories of dir recursively.
```bash
go work use [-r] [dir]
```

- edits the go.work file similarly to go mod edit
```bash
go work edit
```

- syncs dependencies from the workspace’s build list into each of the workspace modules.
```bash
go work sync
```

- get dependencies for code in the current directory
```bash
go get .
```

---

## go env
- displays information about the Go environment configuration.
```
$ go env GOPATH
/home/user/go
```

## GOPATH
- an environment variable in Go that specifies the location of your Go workspace.
* **Purpose**: It tells Go where to find your source code, dependencies, and compiled binaries. 
* By default, it’s set to `~/go` (e.g., `/home/user/go`) if not explicitly defined.
- **Structure**: Typically contains three subdirectories:
  - `src/`: Where your Go source code lives (organized by package or project).
  - `pkg/`: Where compiled package objects are stored.
  - `bin/`: Where executable binaries are placed after running `go install`.

- `go env GOPATH` specifically shows the current value of `GOPATH`.
- Before modules, all Go projects had to live under `GOPATH`. Now, it’s more of a fallback or legacy setting unless you’re working without modules.
