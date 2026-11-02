/*
 * faderC.c
 *
 * Created: 11/1/2024 2:42:08 PM
 * Author : asus
 */ 

#include <avr/io.h>
#define F_CPU 16000000UL
#include <util/delay.h>


int main(void)
{
	DDRD = DDRD | 0b01000000;
	TCCR0B = TCCR0B & 0b11110111;
	TCCR0A = TCCR0A | 0b00000011;
	TCCR0A = (TCCR0A & 0b10111111) | 0b10000000;
	TCCR0B = (TCCR0B & 0b11111011) | 0b00000011;
    while (1) 
    {
		for (int pulsewidth = 255; pulsewidth >= 0; pulsewidth -= 5)
		{
			OCR0A = pulsewidth;
			_delay_ms(30);
		}
    }
	
	return 0;
}

