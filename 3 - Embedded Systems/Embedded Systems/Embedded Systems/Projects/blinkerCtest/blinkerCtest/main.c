/*
 * blinkerCtest.c
 *
 * Created: 11/19/2024 5:54:00 PM
 * Author : asus
 */ 

#include <avr/io.h>
#define F_CPU 16000000UL
#include <util/delay.h>


int main(void)
{
    DDRB = DDRB | 0b00000001;
	DDRB = DDRB & 0b11111101;
	PORTB = PORTB | 0b00000010;
	
    while (1) 
    {
		PORTB = PORTB ^ 0b00000001;
		
		if (PINB & 0b00000010)
		{
			_delay_ms(500);
		}else
		
		_delay_ms(200);
    }
	
	return 0;
}

