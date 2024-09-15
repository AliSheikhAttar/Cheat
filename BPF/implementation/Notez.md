# notes

- Limited loops: Loops are allowed in eBPF programs, but they must have a known, fixed upper-bound to prevent infinite loops.
- No global variables: eBPF programs cannot use global variables; instead, they rely on eBPF maps for data storage and sharing.
- No floating-point arithmetic: eBPF programs do not support floating-point arithmetic, as they can introduce non-deterministic behaviour.
- Limited function calls: eBPF programs can only call a specific set of kernel functions, known as “helper functions.”