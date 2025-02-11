# Data

- int
```go
a0 := 0 // decimal
a0 := _10_000 // decimal
a1 := 0b100 // binary
a1 := 0B100 // binary
a2 := 0  // octal
a2 := 0o72 // octal
a2 := 0O65 // octal
a3 := 0xaf // hex
a3 := 0XBC // hex
```

- float
```go
a:= 0.
a:= 72.40
a:= 072.40       // == 72.40
a:= 2.71828
a:= 1.e+0
a:= 6.67428e-11
a:= 1E6
a:= .25
a:= .12345E+5
a:= 1_5.         // == 15.0
a:= 0.15e+0_2    // == 15.0

a:= 0x1p-2       // == 0.25
a:= 0x2.p10      // == 2048.0
a:= 0x1.Fp+0     // == 1.9375
a:= 0X.8p-0      // == 0.5
a:= 0X_1FFFP-16  // == 0.1249847412109375

a:= 0x15e-2      // == 0x15e - 2 (integer subtraction)

0x.p1        // invalid: mantissa has no digits
1p-2         // invalid: p exponent requires hexadecimal mantissa
0x1.5e-2     // invalid: hexadecimal mantissa requires p exponent
1_.5         // invalid: _ must separate successive digits
1._5         // invalid: _ must separate successive digits
1.5_e1       // invalid: _ must separate successive digits
1.5e_1       // invalid: _ must separate successive digits
1.5e1_       // invalid: _ must separate successive digits
```

- imaginary
```go
a:= 0i
a:= 0123i         // == 123i for backward-compatibility
a:= 0o123i        // == 0o123 * 1i == 83i
a:= 0xabci        // == 0xabc * 1i == 2748i
a:= 0.i
a:= 2.71828i
a:= 1.e+0i
a:= 6.67428e-11i
a:= 1E6i
a:= .25i
a:= .12345E+5i
a:= 0x1p-2i       // == 0x1p-2 * 1i == 0.25i
```