; Archivo: sumas.asm

section .data              ; Sección de datos
    mensaje1 db 'Proporcione un valor: ', 0xA  ; 0xA es \n en ASCII
    mensaje2 db 'Proporcione el segundo valor: ', 0xA
    mensaje3 db 'El resultado es: ', 0
    mensaje1_len equ $ - mensaje1    ; Calcula la longitud del mensaje 1
    mensaje2_len equ $ - mensaje2    ; Calcula la longitud del mensaje 2
    mensaje3_len equ $ - mensaje3    ; Calcula la longitud del mensaje 3

    DATO1 db 0               ; Variables para los datos
    DATO2 db 0
    RESULTADO db 0

section .text               ; Sección de código
    global _start           ; Punto de entrada principal

_start:                     
    ; ==============================
    ; Mostrar "Proporcione un valor"
    ; ==============================
    mov eax, 4              ; Llamada a sys_write
    mov ebx, 1              ; Salida estándar (stdout)
    mov ecx, mensaje1       ; Dirección del mensaje
    mov edx, mensaje1_len   ; Longitud del mensaje
    int 0x80

    ; ==============================
    ; Leer entrada del usuario (DATO1)
    ; ==============================
    mov eax, 3              ; Llamada a sys_read
    mov ebx, 0              ; Entrada estándar (stdin)
    mov ecx, DATO1          ; Dirección para guardar la entrada
    mov edx, 2              ; Leer 2 bytes (carácter + salto de línea)
    int 0x80
    sub byte [DATO1], '0'   ; Convierte ASCII a número

    ; ==============================
    ; Mostrar "Proporcione el segundo valor"
    ; ==============================
    mov eax, 4              ; Llamada a sys_write
    mov ebx, 1              ; Salida estándar (stdout)
    mov ecx, mensaje2       ; Dirección del mensaje
    mov edx, mensaje2_len   ; Longitud del mensaje
    int 0x80

    ; ==============================
    ; Leer entrada del usuario (DATO2)
    ; ==============================
    mov eax, 3              ; Llamada a sys_read
    mov ebx, 0              ; Entrada estándar (stdin)
    mov ecx, DATO2          ; Dirección para guardar la entrada
    mov edx, 2              ; Leer 2 bytes (carácter + salto de línea)
    int 0x80
    sub byte [DATO2], '0'   ; Convierte ASCII a número

    ; ==============================
    ; Sumar los valores
    ; ==============================
    mov al, [DATO1]         ; Mueve el valor de DATO1 a AL
    add al, [DATO2]         ; Suma DATO2 a AL
    add al, '0'             ; Convierte de número a ASCII
    mov [RESULTADO], al     ; Almacena el resultado

    ; ==============================
    ; Mostrar el mensaje "El resultado es: "
    ; ==============================
    mov eax, 4              ; Llamada a sys_write
    mov ebx, 1              ; Salida estándar (stdout)
    mov ecx, mensaje3       ; Dirección del mensaje
    mov edx, mensaje3_len   ; Longitud del mensaje
    int 0x80

    ; ==============================
    ; Mostrar el resultado
    ; ==============================
    mov eax, 4              ; Llamada a sys_write
    mov ebx, 1              ; Salida estándar (stdout)
    mov ecx, RESULTADO      ; Dirección del resultado
    mov edx, 1              ; Mostrar solo 1 carácter
    int 0x80

    ; ==============================
    ; Salida del programa
    ; ==============================
    mov eax, 1              ; Llamada a sys_exit
    xor ebx, ebx            ; Estado de salida (0)
    int 0x80

