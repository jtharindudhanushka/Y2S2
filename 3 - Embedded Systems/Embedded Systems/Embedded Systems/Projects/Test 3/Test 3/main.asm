;
; Test 3.asm
;
; Created: 12/11/2024 12:14:02 AM
; Author : asus
;


; Replace with your application code
SBI DDRB, 5
CBI DDRB, 0
SBI PORTB, 0

START: SBIS PINB, 0
	   CALL blink_200

	   CALL blink_400
	   JMP START

blink_200: SBI PORTB, 5
		   CALL delay_200
		   CBI PORTB, 5
		   CALL delay_200
		   JMP START

blink_400: SBI PORTB, 5
		   CALL delay_400
		   CBI PORTB, 5
		   CALL delay_400
		   JMP START

delay_200: LDI R16,16
LOOP1_200: LDI R17,255
LOOP2_200: LDI R18,255
LOOP3_200: DEC R18
		   BRNE LOOP3_200
		   DEC R17
		   BRNE LOOP2_200
		   DEC R16
		   BRNE LOOP1_200
		   RET

delay_400: LDI R16,32
LOOP1_400: LDI R17,255
LOOP2_400: LDI R18,255
LOOP3_400: DEC R18
		   BRNE LOOP3_400
		   DEC R17
		   BRNE LOOP2_400
		   DEC R16
		   BRNE LOOP1_400
		   RET


