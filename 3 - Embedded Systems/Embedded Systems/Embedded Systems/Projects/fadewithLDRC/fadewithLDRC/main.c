/*
 * fadewithLDRC.c
 *
 * Created: 11/1/2024 3:34:47 PM
 * Author : asus
 */ 

#include <avr/io.h>
#define F_CPU 16000000UL

int main(void)
{
	DDRD = DDRD | 0b01000000;
	DDRC = DDRC & 0b11111110;
    ADMUX = (ADMUX & 0b011111111) | 0b010000000;
	ADMUX = ADMUX & 0b11111000;
	ADCSRA = ADCSRA | 0b00000111;
	ADCSRA = ADCSRA | 0b10000000;
	
    while (1)
    {
		ADCSRA = ADCSRA | 0b01000000;
		while(ADCSRA & 0b01000000);
		float vIn = ADCW * 5.0/1024;
    }
}

