# miao 🐱

One world. Every language. 10,000 meows.

用尽可能多的语言输出 10,000 个 `喵`。

Every program outputs exactly 10,000 `喵` characters, with no separators or trailing newline. Markdown joins in with a literal [10,000 meows](markdown/miao.md).

## Run

| Language | Command |
| --- | --- |
| Python | `python3 languages/python/miao.py` |
| JavaScript | `node languages/javascript/miao.js` |
| Bash | `bash languages/bash/miao.sh` |
| Ruby | `ruby languages/ruby/miao.rb` |
| Go | `go run languages/go/miao.go` |
| C | `cc languages/c/miao.c -o /tmp/miao && /tmp/miao` |

Run `python3 scripts/verify.py` to check installed runtimes and Markdown. Unavailable runtimes are reported as skipped.

## Contributing

Add a directory under `languages/`, include the source and its run command in this README, and make sure its standard output is exactly 10,000 `喵` characters encoded as UTF-8. Please add its command to `scripts/verify.py` too. Pull requests for more languages are welcome! 🐾
