# miao 🐱

One world. Every language. 10,000 meows.

Every program outputs exactly 10,000 `喵` characters as UTF-8, with no separators or trailing newline. Both README.md and markdown/miao.md contain exactly 10,000 literal meows.

## Running

Run a program from the repository root. Runtime versions may affect availability.

| Language / runtime | Command |
| --- | --- |
| Python | `python3 languages/python/miao.py` |
| JavaScript | `node languages/javascript/miao.js` |
| Bash | `bash languages/bash/miao.sh` |
| Ruby | `ruby languages/ruby/miao.rb` |
| Go | `go run languages/go/miao.go` |
| perl | `perl languages/perl/miao.pl` |
| swift | `swift languages/swift/miao.swift` |
| java | `java languages/java/Miao.java` |
| awk | `awk -f languages/awk/miao.awk` |
| tcl | `tclsh languages/tcl/miao.tcl` |
| php | `php languages/php/miao.php` |
| lua | `lua languages/lua/miao.lua` |
| python2 | `python2 languages/python2/miao.py` |
| kotlin | `kotlinc -script languages/kotlin/miao.kts` |
| r | `Rscript languages/r/miao.R` |
| julia | `julia languages/julia/miao.jl` |
| elixir | `elixir languages/elixir/miao.exs` |
| clojure | `clojure languages/clojure/miao.clj` |
| powershell | `pwsh -NoProfile -File languages/powershell/miao.ps1` |
| dart | `dart languages/dart/miao.dart` |
| groovy | `groovy languages/groovy/miao.groovy` |
| haskell | `runghc languages/haskell/miao.hs` |
| ocaml | `ocaml languages/ocaml/miao.ml` |
| javascript-deno | `deno run languages/javascript-deno/miao.ts` |
| fish | `fish languages/fish/miao.fish` |
| zsh | `zsh languages/zsh/miao.zsh` |
| common-lisp | `sbcl --script languages/common-lisp/miao.lisp` |
| scheme | `guile -s languages/scheme/miao.scm` |
| crystal | `crystal run languages/crystal/miao.cr` |
| nim | `nim r --hints:off languages/nim/miao.nim` |
| typescript | `bun languages/typescript/miao.ts` |
| C | `cc languages/c/miao.c -o /tmp/miao && /tmp/miao` |
| C++ | `c++ languages/cpp/miao.cpp -o /tmp/miao && /tmp/miao` |
| Rust | `rustc languages/rust/miao.rs -o /tmp/miao && /tmp/miao` |
| Fortran | `gfortran languages/fortran/miao.f90 -o /tmp/miao && /tmp/miao` |
| C# | `csc -out:/tmp/miao.exe languages/csharp/miao.cs && mono /tmp/miao.exe` |

## Verification

Run `python3 scripts/verify.py`. It compares the exact bytes for both Markdown files and every configured program whose runtime is installed. Missing runtimes are reported as skipped. C# currently needs manual verification.

## Contributing

Add a directory under `languages/`, include a source file and its run command above, and output exactly 10,000 `喵` characters encoded as UTF-8. Add the command to `scripts/commands.json` when possible. Pull requests for more languages are welcome! 🐾
