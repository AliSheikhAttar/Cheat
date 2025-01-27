# Modules

- new module
```bash
go mod init <path>
```

- run main function in main package
```bash
go run .
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

- add dependency and download the package
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