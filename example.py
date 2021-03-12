import matplotlib.pyplot as plt
import seaborn as sns
from idf_to_hyetograph import idf_to_hyetograph

plt.style.use("seaborn")
sns.set(style="ticks")  # white, darkgrid, ticks
sns.set_context("notebook")  # paper, talk, poster
plt.rc('font', family='serif')

K = input("K: ")
a = input("a: ")
b = input("b: ")
c = input("c: ")
T = input("T (anos): ")
td = input("Tempo de duração (minutos): ")
dt = input("Passo de tempo (minutos): ")


if __name__ == "__main__":
    idf = idf_to_hyetograph(K=float(K), a=float(a), b=float(b), c=float(c), T=int(T), td=int(td), dt=int(dt))
    idf.save_txt()
    idf.plot_graph()