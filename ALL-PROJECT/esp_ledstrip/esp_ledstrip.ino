#include "ESP8266WiFi.h"
#include <Adafruit_NeoPixel.h>

int change_strip(int red, int green, int blue);

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
#define LED_PIN     9
#define LED_COUNT  300 // 2 strips 
#define LED_COUNT2 450 // 3 strips 
#define BRIGHTNESS 150 // 0-255
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip2(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
String response;
int r, g, b;
int clicks = 0;
// end of led info 
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
  pinMode(BUTTON_PIN, INPUT_PULLUP);
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
  int return_val; 
  if (client.connect(server,httpPort) && client){ // tries to connect to server
    digitalWrite(LED_BUILTIN, LOW); // led on when connected to server 
    Serial.println("Client Connected to Server.");
    //client.print("What Color?");    // send message to server
    response = client.readString(); // store received msg in 'response'
    //Serial.println(response);
    const char* input = response.c_str(); // input needs to be const char* for sscanf
    // terminate signal
    //client.print("exit");
    digitalWrite(LED_BUILTIN, HIGH); // led off 
    // flood leds with new color
    Serial.println("input: ");Serial.println(input);
    if(sscanf(input, "%d %d %d", &r, &g, &b) == 3 ){
      Serial.print("starting led strip: ");
      Serial.println(input);
      for(int i=0;i<LED_COUNT;i++){
        strip.setPixelColor(i, strip.Color(r, g, b));
        strip.show();
        delay(10);
      }
    }
    else{
      Serial.println("did not read correctly");          
    }
  }
  else{ 
    // add button part 
    if(digitalRead(BUTTON_PIN) == LOW){
      clicks += 1;
      clicks = clicks % 4;
      Serial.print("button pressed! ");
      Serial.println(clicks);
      if(clicks == 0){
        return_val = change_strip(r,g,b);
      }
      if(clicks == 1){ // blue
        return_val = change_strip(0,0,200);
      }
      if(clicks == 2){ // blue
        return_val = change_strip(0,200,0);
      }      
      if(clicks == 3){ // blue
        return_val = change_strip(200,0,0);
      }
      delay(300);
    }
  }
  if(WiFi.status() != WL_CONNECTED){ // if not connected to wifi
    Serial.print('!');
  }
}
int change_strip(int red, int green, int blue){
  delay(300); // needed in case button is held down too long when function starts
  for(int i=0;i<LED_COUNT;i++){
    if(digitalRead(BUTTON_PIN) == LOW){
      Serial.println("button pressed");
      return 0;
    }
    strip.setPixelColor(i, strip.Color(red, green, blue));
    strip.show();
    delay(10);
  }    
  for(int i=(LED_COUNT2-1);i>-1;i--){
    if(digitalRead(BUTTON_PIN) == LOW){
      Serial.println("button pressed");
      return 0;
    }
    strip2.setPixelColor(i, strip2.Color(red, green, blue));
    strip2.show();
    delay(10);
  }      
  return 1;
}
