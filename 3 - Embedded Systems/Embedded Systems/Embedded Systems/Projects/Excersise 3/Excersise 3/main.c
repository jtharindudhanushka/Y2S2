/*
 * Exercise_3.c
 *
 * Created: 12/15/2024 11:48:16 PM
 * Author : Manditha Madushanka
 */

#include <avr/io.h>
#include <avr/interrupt.h>
#define F_CPU 16000000UL
#include <util/delay.h> // For delay (debouncing)

volatile int count = 0;
volatile uint8_t debounce_flag = 0; // Debounce flag to avoid multiple triggers

int main(void)
{
    DDRB = DDRB | 0b00111111;                        // PB0 to PB5 pins as output (LED 1 to 6)
    DDRD = DDRD | 0b11000000;                        // PD6 to PD7 pins as output (LED 7 to 8)
    DDRD = DDRD & 0b11110011;                        // PD2 and PD3 pins as input (pushbutton 1 and 2), also to use external interrupt
    PORTD = PORTD | 0b00001100;                      // Enable pull-up PD2 and PD3

    EICRA = (EICRA & 0b11111110) | 0b00000010;       // Interrupt on falling edge of INT0 pin
    EICRA = (EICRA & 0b11111011) | 0b00001000;       // Interrupt on falling edge of INT1 pin
    EIMSK = EIMSK | 0b00000011;                      // Enable interrupt of INT0 and INT1
    sei();                                           // Enable global interrupt
    
    while (1) 
    {
        // Main loop does nothing as all the logic is handled in the ISR
    }
    return 0;
}

ISR(INT0_vect)                                       // Interrupt for pushbutton 1 (INT0)
{
    if (!debounce_flag) {                            // Check debounce flag
        debounce_flag = 1;                           // Set debounce flag
        _delay_ms(100);                               // Debounce delay (100ms)
        count++;                                     // Increment the count
        debounce_flag = 0;                           // Clear debounce flag
    }
}

ISR(INT1_vect)                                       // Interrupt for pushbutton 2 (INT1)
{
    if (!debounce_flag) {                            // Check debounce flag
        debounce_flag = 1;                           // Set debounce flag
        _delay_ms(100);                               // Debounce delay (100ms)
        
        if (count > 0) {
            PORTB = PORTB | (count % 64);            // Respective first six LEDs (PB0 - PB5) on for count remainder
            PORTD = PORTD | ((count / 64) * 64);     // Respective last two LEDs (PD6 & PD7) on for count above 63
            count = 0;                               // Reset count
        } else if (count == 0) {
            PORTB = PORTB & 0b11000000;              // Turn off LEDs PB0 - PB5
            PORTD = PORTD & 0b00111111;              // Turn off LEDs PD6 & PD7
        }
        
        debounce_flag = 0;                           // Clear debounce flag
    }
}