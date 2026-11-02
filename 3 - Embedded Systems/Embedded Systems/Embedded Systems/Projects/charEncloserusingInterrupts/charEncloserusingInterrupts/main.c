/*
 * charEncloserusingInterrupts.c
 *
 * Created: 11/22/2024 2:15:35 PM
 * Author : asus
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
char ch[] = {'[',' ',']'};
volatile int i = 0;
int main(void)
{
    UBRR0  = 103;
	UCSR0B = UCSR0B & 0b11111011;
	UCSR0C = UCSR0C | 0b00000110;
	UCSR0B = UCSR0B | 0b00011000;
	UCSR0B = UCSR0B | 0b10000000;
	sei();
    while (1)
    {
    }
	
	return 0;
}

ISR(USART_RX_vect){
	ch[1] = UDR0;
	UCSR0B = UCSR0B & 0b01111111;
	UCSR0B = UCSR0B | 0b00100000;
		
}

ISR(USART_UDRE_vect)
{
	UDR0 = ch[i++];
	if (i == 3)
	{
		i = 0;
		UCSR0B = UCSR0B & 0b11011111;
		UCSR0B = UCSR0B | 0b10000000;
	}
}