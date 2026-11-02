/*
 * Pushbutton Interrupt.c
 *
 * Created: 12/13/2024 9:07:31 AM
 * Author : asus
 */ 

#include <avr/io.h>
#define F_CPU 16000000UL
#include <util/delay.h>
#include <avr/interrupt.h>

int main(void)
{
    DDRB = DDRB | 0b00100001;
	DDRD = DDRD & 0b11111011;
	PORTD = PORTD | 0b00000100;
	EICRA = (EICRA & 0b11111110) | 0b00000010;
	EIMSK = EIMSK | 0b00000001;
	sei();
    while (1) 
    {
		PORTB = PORTB ^ 0b00100000;
		_delay_ms(2000);
    }
	
	return 0;
}

ISR (INT0_vect)
{
	PORTB = PORTB ^ 0b00000001;
}

