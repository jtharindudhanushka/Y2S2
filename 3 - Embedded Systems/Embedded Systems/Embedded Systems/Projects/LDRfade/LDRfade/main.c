/*
 * LDRfade.c
 *
 * Created: 12/16/2024 12:51:41 AM
 * Author : asus
 */ 

#include <avr/io.h>


int main(void)
{
    DDRD = DDRD | 0b00001000;
	DDRC = DDRC & 0b11111110;
	
	ADMUX = (ADMUX & 0b01111111) | 0b01000000;
	ADMUX = ADMUX & 0b11111000;
	ADCSRA = ADCSRA | 0b10000000;
	ADCSRA = ADCSRA | 0b00000111;
	
	TCCR2B = TCCR2B & 0b11110111;
	TCCR2A = TCCR2A | 0b00000011;
	TCCR2A = (TCCR2A & 0b11101111) | 0b00100000;
	TCCR2B = (TCCR2B & 0b11111011) | 0b00000011;
	
    while (1) 
    {
		ADCSRA = ADCSRA | 0b01000000;
		while(ADCSRA & 0b01000000);
		OCR2B = ADCW;
    }
	
	return 0;
}

