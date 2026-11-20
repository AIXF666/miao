@miao = private constant [4 x i8] c"\E5\96\B5\00"
declare i32 @printf(ptr, ...)
define i32 @main() {
entry:
  br label %loop
loop:
  %i = phi i32 [0, %entry], [%next, %loop]
  %call = call i32 (ptr, ...) @printf(ptr @miao)
  %next = add i32 %i, 1
  %done = icmp eq i32 %next, 10000
  br i1 %done, label %exit, label %loop
exit:
  ret i32 0
}
