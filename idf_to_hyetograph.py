"""
Created by Yuri Ishizawa
e-mail: yuriishizawa@gmail.com
2021
"""

import csv
import matplotlib.pyplot as plt

class idf_to_hyetograph:
    def __init__(self, K, a, b, c, T, td, dt):
        self.K, self.a, self.b, self.c, self.T, self.td, self.dt = K, a, b, c, T, td, dt
        if td%dt == 0 and td >= dt:
            print("Módulo iniciado")
        elif td%dt != 0 and td >= dt:
            print("ATENÇÃO: O passo de tempo (dt) deve ser um divisor do tempo de duração (td) da chuva")
        else:
            print("ATENÇÃO: O passo de tempo (dt) deve ser menor que o tempo de duração (td) da chuva")
    
    def idf(self,t):
        intensity = ((self.K*(self.T**self.a))/((t + self.b)**self.c))
        return intensity
    
    def calc_dP_t(self): 
        intensity = []
        P = []
        dP = []
        self.dP_t = []

        for i,j in enumerate(list(range(self.dt,self.td+1,self.dt))):
            intensity.append(self.idf(j))
            P.append(intensity[i]*j/60)
            if j == self.dt:
                dP.append(P[i])
            else:
                dP.append(P[i] - P[i-1])
            self.dP_t.append(dP[i]*60/self.dt)
        self.dP_t.sort()       
    
    def calc_h(self):
        self.calc_dP_t()
        self.h = []
        #Para quantidade par de blocos
        if len(self.dP_t)%2 == 0:
            #Lado esquerdo do hietograma
            for i in list(range(1,len(self.dP_t),2)):
                self.h.append(self.dP_t[i])

            #Lado direito do hietograma        
            for i in list(range(len(self.dP_t)-2,1,-2)):
                self.h.append(self.dP_t[i])
            self.h.append(self.dP_t[0])

        #Para quantidade ímpar de blocos
        else:
            #Lado esquerdo do hietograma
            for i in list(range(0,len(self.dP_t),2)):
                self.h.append(self.dP_t[i])

            #Lado direito do hietograma
            for i in list(range(len(self.dP_t)-2,0,-2)):
                self.h.append(self.dP_t[i])
        return self.h
    
    def save_txt(self):
        self.calc_h()
        #Gravando o hietograma em txt
        csvfile = str(self.td)+"min_"+str(self.T)+"anos.txt"
        with open(csvfile, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for i,val in enumerate(self.h):
                writer.writerow([(i+1)*self.dt,val])
        print("Arquivo txt salvo no mesmo diretório deste programa")
    
    def plot_graph(self):
        self.calc_h()
        y_axis = self.h
        x_axis = []

        for i in list(range(self.dt,self.td+1,self.dt)):
            x_axis.append(i)
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        #ax.set_aspect(aspect=1)
        plt.bar(x_axis, y_axis, align='center', color="blue", width=self.dt/2)
        plt.text((self.td/2)+self.dt, self.dP_t[-2] + self.dt,f'td = {self.td} min, T = {self.T} anos')
        plt.title("Distribuição da chuva")
        plt.ylabel("Intensidade (mm/h)")
        plt.xlabel('Tempo (min)')
        plt.xticks(x_axis, rotation = 35)
        plt.tick_params(axis = 'x', which = 'major', labelsize = 8)
        plt.savefig(str(self.td)+"min_"+str(self.T)+"anos")
        plt.show()
        print("Gráfico do hietograma salvo no mesmo diretório deste programa")