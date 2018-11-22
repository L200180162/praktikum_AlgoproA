def konversiSuhu(C="none", F="none") :
    suhu = 0
    if C == ("none") and (F == "none") :
        print("Suhu 0 Celsius setara dengan 32 Fahrenheit")
    elif C != ("none") and (F == "none") :
        suhu = (9.0/5 * C) + 32
        suhu = int(suhu)
        print("Suhu "+str(C)+" Celsius setara dengan "+str(suhu)+" Fahrenheit")
    elif C == ("none") and (F != "none") :
        suhu = 5.0/9 * (F-32)
        suhu = int(suhu)
        print("Suhu "+str(F)+" Fahrenheit setara dengan "+str(suhu)+"Celsius")
