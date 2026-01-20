.data
    x: .long 15
    res: .space 4

.text

.global main

main:
    mov x, %eax
    inc %eax
    mov %eax, res

exit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80