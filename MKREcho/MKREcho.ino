#include <WiFi101.h>

char ssid[16]; // SSID
char pwd[16];  // Password
int status = WL_IDLE_STATUS;     

// Especificamos la ubicación del servdidor ECHO
char host[] = "10.0.0.1";
byte port = 7;

WiFiClient client;

void setup() {
  // Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial);

  // Verificamos que la Ethernet está disponible.
  // En una MKR1000 nunca debería fallar.
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("WiFi shield not present");
    while (true);
  }

  readSSID(ssid,pwd);

  // Nos conectamos al AP (Raspberry)
  while ( status != WL_CONNECTED) {
    Serial.print(".");
    status = WiFi.begin(ssid, pwd);

    // Espero un poco antess de reintentar la conexión
    delay(5000);
  }
  Serial.println("\nConectado.");

  dumpWiFi();
}

void loop() {
  char data[128];

  readValue("\nMessage?",data);
  echo(data);
}

// Enviamos un mensaje al servidor ECHO y esperamos 
// a recibir la respuesta
// TODO: Añadir un timeout a la espera de la respuesta
void echo(char *message) {

  // Conectamos con el servidor ECHO
  if (client.connect(host,port)) {
    // Enviamos el mensaje
    Serial.print("Sending:");
    Serial.println(message);
    client.println(message);

    // Esperamos a que llegue la respuesta
    while (!client.available()) {
      delay(50);
      Serial.print(".");
    }
    Serial.println("");
    
    // Leemos cada uno de los caracteres de la conexión y 
    // los volcamos por pantalla
    Serial.print("Receiving:");
      while (client.available()) {
        char c = client.read();
        Serial.write(c);
      } 
    Serial.println("");

    // Cerramos la conexión
    client.stop();
  }
}

// Vuelco información básica de la conexión
void dumpWiFi() {

  // Imprimo la SSID de la conexión
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // Imprimo la configuración de red
  IPAddress ip = WiFi.localIP();
  Serial.print("IP address:  ");
  Serial.println(ip);

  Serial.print("Subnet mask: ");
  Serial.println((IPAddress)WiFi.subnetMask());

  Serial.print("Gateway IP:  ");
  Serial.println((IPAddress)WiFi.gatewayIP());

}

// Leo el SSD la contraseña
void readSSID(char *ssid, char *pwd) {
  readValue("SSID?",ssid);
  readValue("Password?",pwd);

  Serial.print("Conecting with SSID: ");
  Serial.println(ssid);
}

// Leo un parámetro de la consola
// TODO: Validar que no llegan más caracteres de los esperados
void readValue(char *msg, char *data) {

  // Mostramos el mensaje
  Serial.println(msg);
  // Esperamos a que lleguen caracteres
  while(!Serial.available()); 
  
  // Leemos los caracteres
  int n = Serial.available();
  for(int i=0; i<n; i++) {
    data[i] = Serial.read();
  }
  
  // Terminamos la cadena. 
  // Sé que tendría que ser data[n] pero así evito el CR final.
  data[n-1] = '\0'; 

}
