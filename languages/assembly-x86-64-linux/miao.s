.global _start
.section .rodata
miao: .ascii "喵"
.section .text
_start:
    mov $10000, %r12
loop:
    mov $1, %rax
    mov $1, %rdi
    lea miao(%rip), %rsi
    mov $3, %rdx
    syscall
    dec %r12
    jnz loop
    mov $60, %rax
    xor %rdi, %rdi
    syscall
