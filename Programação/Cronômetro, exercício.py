import time

def iniciar_cronometro():
    tempo_inicial = time.time()
    
    while True:
        tempo_atual = time.time()
        tempo_passado = tempo_atual - tempo_inicial
        
        minutos = int(tempo_passado / 60)
        segundos = int(tempo_passado % 60)
        
        print(f"Tempo: {minutos}:{segundos}")
        
        time.sleep(1)
        
        if segundos >= 10:
        #if segundos == 10: essa parte do código garante que o cronômetro vai parar quando atingir 10 segundos, mas os dois = não faz isso acontecer, por isso o < diz pro programa para quando atingir ou passar 10 segundos.
            break
        
iniciar_cronometro()
