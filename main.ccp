#include <Arduino.h>
#include <WiFi.h>

//define WIFI
#define WIFI_SSID "WLAN-1234"
#define WIFI_PASSWORD "1234567890"

//define pins
#define LDRPIN 34

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  // put your setup code here, to run once:
  Serial.begin(921600);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected!");
  int lightvalue = analogRead(LDRPIN);
  Serial.print("Lightvalue: ");
  Serial.println(lightvalue);

  //deep sleep 60s 
  esp_sleep_enable_timer_wakeup(60000000);
  esp_deep_sleep_start();
}

void loop() {
  //empty because of deep sleep
}

