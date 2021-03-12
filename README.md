# idf_to_hyetograph

Módulo criado para a geração de hietogramas de intensidade de chuva a partir dos parâmetros regionais de curva IDF utilizando o Método dos Blocos Alternados.

## Modo de uso

Os dados de entrada são:
- Parâmetros da curva IDF regional (K, a, b e c);
- Período de retorno da chuva (T) em anos;
- Tempo de duração total da chuva (td) em minutos;
- Passo de tempo da chuva (dt) em minutos.

Com este módulo é possível obter:
- Um arquivo no formato txt com as intensidades da chuva em mm/h para cada passo de tempo;
- Um gráfico no formato png com a distribuição da chuva.

Se preferir utilizar Jupyter Notebook, basta abrir o arquivo "example_notebook.ipynb" e alterar os parâmetros de entrada.
