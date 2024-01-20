#define L_PWM 5
#define L_DIR 4
#define R_PWM 6
#define R_DIR 9
#define PWM_MAX 165
#define LED_1_PIN 10
#define LED_2_PIN 11

void setup() {
  // Configure H-bridge motor control pins
  pinMode(L_DIR, OUTPUT);
  pinMode(R_DIR, OUTPUT);
  pinMode(L_PWM, OUTPUT);
  pinMode(R_PWM, OUTPUT);

  // Configure LED pins
  pinMode(LED_1_PIN, OUTPUT);
  pinMode(LED_2_PIN, OUTPUT);

  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    byte command = Serial.read(); // Read a single byte

    if (command & 0x01) { // Check if bit 0 is set (W key)
      // Forward logic
      if (command & 0x02) { // Check if bit 1 is set (A key)
        // Forward-left logic
        leftMotor(50);
        rightMotor(25);
        Serial.println("Moving Forward-Left");
      } else if (command & 0x08) { // Check if bit 3 is set (D key)
        // Forward-right logic
        leftMotor(25);
        rightMotor(50);
        Serial.println("Moving Forward-Right");
      } else {
        leftMotor(50); // Move forward
        rightMotor(50);
        Serial.println("Moving Forward");
      }
    } else if (command & 0x04) { // Check if bit 2 is set (S key)
      // Backward logic
      if (command & 0x02) { // Check if bit 1 is set (A key)
        // Backward-left logic
        leftMotor(-50);
        rightMotor(-25);
        Serial.println("Moving Backward-Left");
      } else if (command & 0x08) { // Check if bit 3 is set (D key)
        // Backward-right logic
        leftMotor(-25);
        rightMotor(-50);
        Serial.println("Moving Backward-Right");
      } else {
        leftMotor(-50); // Move backward
        rightMotor(-50);
        Serial.println("Moving Backward");
      }
    } else if (command & 0x02) { // Check if bit 1 is set (A key)
      leftMotor(-50); // Turn left
      rightMotor(50);
      Serial.println("Turning Left");
    } else if (command & 0x08) { // Check if bit 3 is set (D key)
      leftMotor(50); // Turn right
      rightMotor(-50);
      Serial.println("Turning Right");
    } else {
      stopMotors(); // Stop motors
      Serial.println("Stopping");
    }
  }
}

void leftMotor(int V) {
  if (V > 0) {
    V = map(V, 0, 100, 0, PWM_MAX);
    digitalWrite(L_DIR, 0);
    analogWrite(L_PWM, V); 
  } else {
    V = abs(V);
    V = map(V, 0, 100, 0, PWM_MAX);
    digitalWrite(L_DIR, 1);
    analogWrite(L_PWM, V);   
  }
}

void rightMotor(int V) {
  if (V > 0) {
    V = map(V, 0, 100, 0, PWM_MAX);
    digitalWrite(R_DIR, 0);
    analogWrite(R_PWM, V); 
  } else {
    V = abs(V);
    V = map(V, 0, 100, 0, PWM_MAX);
    digitalWrite(R_DIR, 1);
    analogWrite(R_PWM, V);    
  }
}

void stopMotors() {
  analogWrite(L_PWM, 0);
  analogWrite(R_PWM, 0);
}
