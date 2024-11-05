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

  Serial.println("Distancia: " + String(dist));
  Serial.println("Temperatura: " + String(temp));
  Serial.println("Humidade: " + String(umi));
  Serial.println("Luminosidade: " + String(ldrValue));

  delay(2000);
}
