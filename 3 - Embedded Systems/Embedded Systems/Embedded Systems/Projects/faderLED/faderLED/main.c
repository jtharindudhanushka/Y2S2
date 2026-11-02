/*
 * faderLED.c
 *
 * Created: 12/15/2024 10:44:43 PM
 * Author : asus
 */ 

#include <avr/io.h>
#define F_CPU 16000000UL
#include <util/delay.h>

int main(void)
{
    DDRD = DDRD | 0b00001000;
	TCCR2B = TCCR2B & 0b11110111;
	TCCR2A = TCCR2A | 0b00000011;
	TCCR2A = (TCCR2A & 0b11101111) | 0b00100000;
	TCCR2B = (TCCR2B & 0b11111011) | 0b00000011;
    while (1)
    {
		for (int pulsewidth = 255; pulsewidth >= 0; pulsewidth-= 5)
		{
			OCR2B = pulsewidth;
			_delay_ms(300);
		}
    }
	
	return 0;
}

