/*
 * Test ADC.c
 *
 * Created: 12/12/2024 1:14:35 PM
 * Author : asus
 */ 

#include <avr/io.h>


int main(void)
{
    DDRB = DDRB | 0b00011111;
	DDRC = DDRC & 0b11111110;
	ADMUX = (ADMUX & 0b01111111) | 0b01000000;
	ADMUX = ADMUX & 0b11111000;
	ADCSRA = ADCSRA | 0b00000111;
	ADCSRA = ADCSRA | 0b10000000;
    while (1)
    {
		ADCSRA = ADCSRA | 0b01000000;
		while (ADCSRA & 0b01000000);
		float Vin = ADCW * 5.0 /1024;
		PORTB = PORTB & 0b11100000;
		if (Vin > 4)
		{
			PORTB = PORTB | 0b00011111;
		}
		
		else if (Vin > 3)
		{
			PORTB = PORTB | 0b00001111;
		}
		
		else if (Vin > 2)
		{
			PORTB = PORTB | 0b00000111;
		}
		
		else if (Vin > 1)
		{
			PORTB = PORTB | 0b00000011;
		}
		
		else if (Vin > 0)
		{
			PORTB = PORTB | 0b00000001;
		}					
    }
	
	return 0;
}

