#include "ESP8266WiFi.h"
#include <Adafruit_NeoPixel.h>

// server address and port 
WiFiClient client;
const IPAddress server(10,0,0,194);
const int httpPort = 12345;
// wifi name and password
const char* ssid = "Panic In DC    <(O.O)>";
const char* password = "12345678";
// led info
#define BUTTON_PIN  5
#define LED_PIN     4
#define LED_COUNT  300
#define BRIGHTNESS 150 // 0-255
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
String response;
int r, g, b;
// end of led info 
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
  pinMode(BUTTON_PIN, INPUT);
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  WiFi.mode(WIFI_STA);
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");  
    delay(1000);
    yield();
  }
  Serial.println("Connected to Wifi.");
  strip.begin(); // mandatory 
  strip.clear(); // clear all leds
  strip.setBrightness(BRIGHTNESS);
  digitalWrite(LED_BUILTIN, HIGH); // led off 
}

void loop() { 
  // Send message
//  String response;
  if (client.connect(server,httpPort) && client){ // tries to connect to server
    digitalWrite(LED_BUILTIN, LOW); // led on when connected to server 
    Serial.println("Client Connected to Server.");
    client.print("What Color?");    // send message to server
    response = client.readString(); // store received msg in 'response'
    //Serial.println(response);
    const char* input = response.c_str(); // input needs to be const char* for sscanf
    // terminate signal
    client.print("exit");
    digitalWrite(LED_BUILTIN, HIGH); // led off 
    // flood leds with new color
    if(sscanf(input, "%d %d %d", &r, &g, &b) == 3 ){
      Serial.print("starting led strip: ");
      Serial.println(input);
      for(int i=0;i<LED_COUNT;i++){
        strip.setPixelColor(i, strip.Color(r, g, b));
        strip.show();
        delay(10);
      }          
    }
  }
  else{ 
    
    if(WiFi.status() != WL_CONNECTED){ // if not connected to wifi
      ESP.restart(); // restart 
    }
  }
}
void blue(){
  for(int i=0;i<LED_COUNT;i++){
    strip.setPixelColor(i, strip.Color(0, 0, 200));
    strip.show();
    delay(10);
  }    
}
