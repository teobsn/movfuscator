.data
    x: .long 16         # 2^4
    y: .long 0x80000000 # 2^31

.text

.global main

main:
    movl x, %eax
    movl y, %ebx
    mul %ebx

et_exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80