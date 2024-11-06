#include<DHT.h>
#include<Servo.h>
#include<ArduinoJson.h>

#define LDR A0
#define RED 13
#define YELLOW 12
#define GREEN 11
#define DHTPIN 2
#define DHTTYPE DHT22
#define TRIGGER 7
#define ECHO 8
#define SERVOPIN 9

int ldrValue;
int dist;

DHT dht(DHTPIN, DHTTYPE);
Servo myServo;

void setup() {
  myServo.attach(SERVOPIN);

  dht.begin();

  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);

  pinMode(TRIGGER, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(SERVOPIN, OUTPUT);
  pinMode(LDR, INPUT);

  Serial.begin(9600);
}

void loop() {
  digitalWrite(TRIGGER, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER, LOW);
  
  dist = pulseIn(ECHO, HIGH);
  dist = dist / 58;

  int temp = dht.readTemperature();
  int umi = dht.readHumidity();

  ldrValue = analogRead(LDR);

  if (ldrValue < 300) {
    digitalWrite(GREEN, HIGH);
    digitalWrite(YELLOW, LOW);
    digitalWrite(RED, LOW);
  } else if (ldrValue < 700) {
    digitalWrite(GREEN, LOW);
    digitalWrite(YELLOW, HIGH);
    digitalWrite(RED, LOW);
  } else {
    digitalWrite(GREEN, LOW);
    digitalWrite(YELLOW, LOW);
    digitalWrite(RED, HIGH);
  }

  char comando;
  if (Serial.available() > 0) {
    comando = Serial.read();
    if (temp >= 40 && comando == '1') {
      myServo.write(180);
    } else if (temp >= 40 && comando == '0') {
      myServo.write(0);
    } else if (temp < 40 && comando == '0') {
      myServo.write(0);
    } else if (temp < 40 && comando == '1') {
      myServo.write(180);
    }
  } else if (comando == NULL) {
    if (temp >= 40) {
      myServo.write(180);
    } else {
      myServo.write(0);
    }
  }

  StaticJsonDocument<100>json;
  json["Distancia"] = dist;
  json["Luminosidade"] = ldrValue;
  json["Temperatura"] = temp;
  json["Umidade"] = umi;

  serializeJson(json, Serial);
  Serial.println();

  Serial.println("Distancia: " + String(dist));
  Serial.println("Temperatura: " + String(temp));
  Serial.println("Humidade: " + String(umi));
  Serial.println("Luminosidade: " + String(ldrValue));

  delay(2000);
}
