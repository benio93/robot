#define LED_1_PIN 10
#define LED_2_PIN 11

void setup() {
  pinMode(LED_1_PIN, OUTPUT);
  pinMode(LED_2_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(LED_1_PIN, HIGH);
  
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if (data.equals("W")) {
      Serial.print("W");
    
    } else if (data.equals("S")) {
      Serial.println("S");
      digitalWrite(LED_1_PIN, HIGH);
      digitalWrite(LED_2_PIN, LOW);
    } else {
      digitalWrite(LED_1_PIN, LOW);
      digitalWrite(LED_2_PIN, LOW);
    }
  }
}
