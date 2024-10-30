#include<DHT.h>

#define LDR A0
#define RED 13
#define YELLOW 12
#define GREEN 8
#define BUZZER 7
#define DHTPIN 4
#define DHTTYPE DHT22

int ldrValue = 0;
int buzzerTimer = 0;
int intervalTimer = 0;
bool alerta = false;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  pinMode(LDR, INPUT);
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  ldrValue = analogRead(LDR);
  int temp = dht.readTemperature();
  int umi = dht.readHumidity();
  delay(100);

  Serial.println(temp);
  Serial.println(umi);

  bool luzRuim = ldrValue < 333 || ldrValue > 970;
  bool luzMaisOuMenos = !luzRuim && (ldrValue < 777 || ldrValue > 900);
  bool temperaturaRuim = temp < 10 || temp > 16;
  bool temperaturaMaisOuMenos = !temperaturaRuim && temp != 13;
  bool umidadeRuim = umi < 60 || umi > 80;
  bool umidadeMaisOuMenos = !umidadeRuim && (umi < 65 || umi > 75);

  if (luzRuim || temperaturaRuim || umidadeRuim) {
    digitalWrite(RED, HIGH);
    digitalWrite(YELLOW, LOW);
    digitalWrite(GREEN, LOW);
    alerta = true;
  } else if (luzMaisOuMenos || temperaturaMaisOuMenos || umidadeMaisOuMenos) {
    digitalWrite(RED, LOW);
    digitalWrite(YELLOW, HIGH);
    digitalWrite(GREEN, LOW);
    alerta = true;
  } else {
    digitalWrite(RED, LOW);
    digitalWrite(YELLOW, LOW);
    digitalWrite(GREEN, HIGH);
    alerta = false;
  }

  if (alerta && buzzerTimer == 0 && intervalTimer == 0) {
    tone(BUZZER, 1500);
    buzzerTimer += 100;
  } else if (alerta && buzzerTimer <= 3000 && intervalTimer == 0) {
    buzzerTimer += 100;
  } else if (alerta && intervalTimer <= 1000) {
    buzzerTimer = 0;
    noTone(BUZZER);
    intervalTimer += 100;
  } else if (alerta) {
    intervalTimer = 0;
  } else {
    noTone(BUZZER);
    intervalTimer = 0;
    buzzerTimer = 0;
  }
}
