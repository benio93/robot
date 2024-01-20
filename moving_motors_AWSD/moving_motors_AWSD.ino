#define L_PWM 5
#define L_DIR 4
#define R_PWM 6
#define R_DIR 9
#define PWM_MAX 165
#define LED_1_PIN 10
#define LED_2_PIN 11


// Define a timeout in milliseconds
//const unsigned long serialTimeout = 100; // Adjust this value as needed
//String data = "";
//unsigned long lastTime = 0;


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
    String data = Serial.readStringUntil('\n');
    Serial.println(data);

    if (data.indexOf('W') != -1) {
      // Forward logic
      if (data.indexOf('A') != -1) {
        // Forward-left logic
      } else if (data.indexOf('D') != -1) {
        // Forward-right logic
      } else {
        leftMotor(50); // Move forward
        rightMotor(50);
        Serial.println("Moving Forward");
      }
    } else if (data.indexOf('S') != -1) {
      // Backward logic
      if (data.indexOf('A') != -1) {
        // Backward-left logic
      } else if (data.indexOf('D') != -1) {
        // Backward-right logic
      } else {
        leftMotor(-50); // Move backward
        rightMotor(-50);
        Serial.println("Moving Backward");
      }
    } else if (data.indexOf('A') != -1) {
      leftMotor(-50); // Turn left
      rightMotor(50);
      Serial.println("Turning Left");
    } else if (data.indexOf('D') != -1) {
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
