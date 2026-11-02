/*
 * counterBasedTriggerusingInterrupt.c
 *
 * Created: 10/25/2024 2:08:30 PM
 * Author : asus
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>


int main(void)
{
	DDRB = DDRB | 0b00100000;
	DDRD = DDRD & 0b11101111;
	
	
	while (1)
	{
	}
}

