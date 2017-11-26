/*

Projeto 1 - Termostato
IE327Q - 2 Semestre 2017

Professor Dr. Fabiano Fruett

Alunos:  Euclides
         Mathias
         Stenio
         Talles
*/

#define TAXA_AMOSTRAGEM 1000/8

/* Pinos a serem utilizados no projeto */
#define pinoAtuador0 3
#define pinoAtuador1 5
#define pinoAtuador2 6
#define pinoAtuador3 9

void setup() 
{ 
  /* Inicializa comunicacao serial a 9600 bps */  
  Serial.begin(9600);
  
  /* Configura pinos dos atuadores como saida como saida */
  pinMode(pinoAtuador0, OUTPUT);
  pinMode(pinoAtuador1, OUTPUT);
  pinMode(pinoAtuador2, OUTPUT);
  pinMode(pinoAtuador3, OUTPUT);
  
  /* Referncia do ADC em 5,0 V */
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
    
    /* Se o primeiro caracter do pacote recebido for 0, desliga o atuador. Caso contrario o liga */
    (leituraSerial.charAt(0)=='0') ? (digitalWrite(pinoAtuador0, LOW)) : (digitalWrite(pinoAtuador0, HIGH));
    /* Se o segundo caracter do pacote recebido for 0, desliga o atuador. Caso contrario o liga */
    (leituraSerial.charAt(1)=='0') ? (digitalWrite(pinoAtuador1, LOW)) : (digitalWrite(pinoAtuador1, HIGH));
    /* Se o terceiro caracter do pacote recebido for 0, desliga o atuador. Caso contrario o liga */
    (leituraSerial.charAt(2)=='0') ? (digitalWrite(pinoAtuador2, LOW)) : (digitalWrite(pinoAtuador2, HIGH));        
    /* Se o quarto caracter do pacote recebido for 0, desliga o atuador. Caso contrario o liga */
    (leituraSerial.charAt(3)=='0') ? (digitalWrite(pinoAtuador3, LOW)) : (digitalWrite(pinoAtuador3, HIGH));    
  }
}
