# Test

- run all test
> in module dir
```bash
go test ./...
```

- run coverage test
> in module dir
```bash
go test -cover ./...
```

- create coverage test
> in module dir
```bash
go test -coverprofile=coverage.out <dir: ./internal/service/user/...>
```

- convert coverage output to html
```bash
go tool cover -html=coverage.out -o coverage.html
```