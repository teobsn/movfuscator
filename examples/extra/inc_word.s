.data
    x: .byte 15
    res: .space 4

.text

.global main

main:
    mov $0, %eax

    movw x, %ax
    incw %ax

    mov %eax, res

exit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80