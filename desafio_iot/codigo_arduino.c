#include<DHT.h>
#include <LiquidCrystal_I2C.h> // Biblioteca utilizada para fazer a comunicação com o display 20x4 

#define LDR A0
#define RED 13
#define YELLOW 12
#define GREEN 8
#define BUZZER 7
#define DHTPIN 4
#define DHTTYPE DHT22
#define col 16 // Serve para definir o numero de colunas do display utilizado
#define lin 2 // Serve para definir o numero de linhas do display utilizado
#define ende 0x27 // Serve para definir o endereço do display.

int ldrValue = 0;
int buzzerTimer = 0;
int intervalTimer = 0;
int lcdDelay = 1000;
int lcdTimer = 0;
bool alerta = false;

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(ende,col,lin);

void setup() {
  Serial.begin(9600);
  pinMode(LDR, INPUT);
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  dht.begin();
  lcd.init(); // Serve para iniciar a comunicação com o display já conectado
  lcd.backlight(); // Serve para ligar a luz do display

  lcd.setCursor(2,0);
  lcd.print("BEM - VINDO:");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print("VINHERIA AGNELLO");
  delay(4000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(".");
  delay(500);
  lcd.setCursor(1,0);
  lcd.print(".");
  delay(500);
  lcd.setCursor(2,0);
  lcd.print(".");
  delay(500);
  lcd.setCursor(3,0);
  lcd.print(".");
  delay(500);
  lcd.setCursor(4,0);
  lcd.print(".");
  delay(500);
  lcd.setCursor(5,0);
  lcd.print(".");
  delay(500);
  lcd.clear();
}

void loop() {
  // put your main code here, to run repeatedly:
  ldrValue = analogRead(LDR);
  int temp = dht.readTemperature();
  int umi = dht.readHumidity();
  delay(100);

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

  lcdTimer += 100;

  if (lcdTimer == lcdDelay) {
    lcd.clear();

    lcd.setCursor(0, 1);
    lcd.print("Temp");
    lcd.setCursor(5, 1);
    lcd.print(temp);
    lcd.setCursor(8, 1);
    lcd.print("Umi");
    lcd.setCursor(12, 1);
    lcd.print(umi);

    if (alerta) {
      lcd.setCursor(0, 0);
      lcd.print("Alerta!");
    } else {
      lcd.setCursor(0, 0);
      lcd.print("OK");
    }

    lcdTimer = 0;
  }
}
