#define LED_PIN1 43
#define LED_PIN2 44
#define LED_PIN3 45
#define LED_PIN4 46

#define BUTTON_PIN1 38
#define BUTTON_PIN2 39
byte buttonState = LOW;
byte lastButtonState = LOW;
//byte ledState = LOW;
int currentMode = 1;
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN1, OUTPUT);
  pinMode(LED_PIN2, OUTPUT);
  pinMode(LED_PIN3, OUTPUT);
  pinMode(LED_PIN4, OUTPUT);

  pinMode(BUTTON_PIN1, INPUT);
  pinMode(BUTTON_PIN2, INPUT);
}

void loop() {
  buttonState = digitalRead(BUTTON_PIN2);
  if (buttonState == HIGH && lastButtonState == LOW) {
    currentMode++;
    if(currentMode > 3) {
      currentMode = 1;
    }
  }

  lastButtonState = buttonState; 

  if (currentMode == 1) {
    mode1();
  } else if (currentMode == 2) {
    mode3();
  } else if (currentMode == 3) {
    mode2();
  }
  
}
void mode1() {
   digitalWrite(LED_PIN1, HIGH);
   digitalWrite(LED_PIN2, HIGH);
   digitalWrite(LED_PIN3, HIGH);
   digitalWrite(LED_PIN4, HIGH);
   delay(1000);
   digitalWrite(LED_PIN1, LOW);
   digitalWrite(LED_PIN2, LOW);
   digitalWrite(LED_PIN3, LOW);
   digitalWrite(LED_PIN4, LOW);
   delay(1000);
    
}

void mode2() {
  digitalWrite(LED_PIN1, HIGH);
  delay(1000);
  digitalWrite(LED_PIN2, HIGH);
  delay(1000);
  digitalWrite(LED_PIN3, HIGH);
  delay(1000);
  digitalWrite(LED_PIN4, HIGH);
  delay(1000);

  digitalWrite(LED_PIN1, LOW);
  digitalWrite(LED_PIN2, LOW);
  digitalWrite(LED_PIN3, LOW);
  digitalWrite(LED_PIN4, LOW);
}

void mode3() {
  digitalWrite(LED_PIN4, HIGH);
  delay(1000);
  digitalWrite(LED_PIN3, HIGH);
  delay(1000);
  digitalWrite(LED_PIN2, HIGH);
  delay(1000);
  digitalWrite(LED_PIN1, HIGH);
  delay(1000);

  digitalWrite(LED_PIN1, LOW);
  digitalWrite(LED_PIN2, LOW);
  digitalWrite(LED_PIN3, LOW);
  digitalWrite(LED_PIN4, LOW);
}