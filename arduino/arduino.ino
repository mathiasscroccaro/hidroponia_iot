/*

Projeto 1 - Termostato
IE327Q - 2 Semestre 2017

Professor Dr. Fabiano Fruett

Alunos:  Euclides
         Mathias
         Talles

*/

#define TAXA_AMOSTRAGEM 1000/8

/* Pinos a serem utilizados no projeto */
#define pinoSensor 0
#define pinoAlarme 13
#define pinoAtuador 3

void setup() 
{ 
  /* Inicializa comunicacao serial a 9600 bps */  
  Serial.begin(9600);
  
  /* Configura pinos do alarme e atuador(aquecedor) como saida */
  pinMode(pinoAlarme, OUTPUT);
  pinMode(pinoAtuador, OUTPUT);
  
  /* Referncia do ADC em 2,5 V */
  analogReference(EXTERNAL);  
}

/* Rotina que realiza a leitura dos dados via serial */
String leSerial()
{
  /* Variavel que armazena recepçao da comunicaçao serial */
  String leitura = "";
  /* Variavel auxiliar para leitura serial */  
  char caracter; 
  
  /* Ha dados a serem recepcionados? */
  while(Serial.available() > 0) 
  {
    /* Armazena o valor caso seja diferente de '\n' */
    caracter = Serial.read(); 
    if (caracter != '\n')
      leitura.concat(caracter);
  }
  
  /* Retorna a string lida via serial */
  return leitura; 
}

void loop() {
  
  unsigned char i = 0;
    
  /* Inicializa variavel auxiliar de leitura serial */
  String leituraSerial = "";
  String leituraSensores = "";
  
  for (i=0;i<4;i++)
  {
    if (i!=3)
      leituraSensores += String(analogRead(i),DEC) + ';';
    else
      leituraSensores += String(analogRead(i),DEC);
  
	delay(TAXA_AMOSTRAGEM); 
  }
  
  /* Envia valor amostrado via serial */
  Serial.println(leituraSensores);   
  
  /* Ha dados a serem recepcionados? */
  if (Serial.available() > 0)
  {
    /* Realiza a leitura serial */
    leituraSerial = leSerial();
    
    /* Se o primeiro caracter do pacote recebido for 0, desliga o alarme. Caso contrario o liga */
    (leituraSerial.charAt(0)=='0') ? (digitalWrite(pinoAlarme, LOW)) : (digitalWrite(pinoAlarme, HIGH));
    /* Se o segundo caracter do pacote recebido for 0, desliga o atuador. Caso contrario o liga */
    (leituraSerial.charAt(1)=='0') ? (digitalWrite(pinoAtuador, LOW)) : (digitalWrite(pinoAtuador, HIGH));    
  }
  
  /* Espera intervado de 500ms */
}
