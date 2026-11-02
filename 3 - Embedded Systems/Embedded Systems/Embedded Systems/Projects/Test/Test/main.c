/*
 * Test.c
 *
 * Created: 11/23/2024 9:41:26 PM
 * Author : asus
 */ 

#include <avr/io.h>
#define F_CPU 16000000UL
#include <avr/delay.h>

int main(void)
{
    DDRB = DDRB | 0b00011111;
	DDRD = DDRD | 0b01100000;
    while (1) 
    {
		PORTD =  0b00100000;
		while(!(PORTD & 0b10000000))
		{
			PORTB =  0b00000001;
			
			while(!(PORTB & 0b00100000))
			{
				_delay_ms (150);
				PORTB = PORTB * 2;
			}
			
			PORTD = PORTD * 2;
		}
		
		while(!(PORTD & 0b00010000))
		{
			PORTB =  0b00010000;
			
			while(!(PORTB & 0b00000001))
			{
				_delay_ms (150);
				PORTB = PORTB / 2;
			}
			
			PORTD = PORTD / 2;
		}		

    }
	
	return 0;
}

