/*
 * pollingBasedTriggerC.c
 *
 * Created: 10/4/2024 1:22:28 PM
 * Author : asus
 */ 

#include <avr/io.h>
#define F_CPU 16000000UL
#include <util/delay.h>


int main(void)
{
    DDRB = DDRB | 0b00100001;
	DDRD = DDRD & 0b11111011;
	
	PORTD = PORTD | 0b00000100;
	
    while (1) 
    {
		PORTB = PORTB ^ 0b00100000;
		_delay_ms(2000);
		
		if((PIND & 0b00000100) ==0)
		{
			PORTB = PORTB ^ 0b00000001;
		}
    }
	
	return 0;
}

