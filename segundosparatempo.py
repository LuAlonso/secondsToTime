segundos_str = input("Digite o número de segundos que deseja converter")
total_segs = int(segundos_str)

dias = total_segs // 86400
segs_inicial = total_segs % 86400
horas = segs_inicial // 3600
segs_restante = segs_inicial % 3600
minutos = segs_restante // 60 
segs_restante_final = segs_restante % 60

print("o tempo é de",dias,"dias,",horas, "horas,", minutos, "minutos e", segs_restante_final, "segundos.")