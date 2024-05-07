

#pyautogui.click  --> clicar com o louse
#pyautogui.write --> escrever um texto
#pyautogui.hotkey --> clicar um conjunto de teclas (crtl +c, crtl+v)

#todos os comandos da biblioteca podem ser localizados no Google Pyautogui

import pyautogui
import time

pyautogui.PAUSE = 0.9

pyautogui.press ("win")
pyautogui.write ("Chrome")
pyautogui.press ("enter")
pyautogui.write("inserir aqui o local onde vai ser salvo ou sistema")
pyautogui.press ("enter")

#ter cuidado e configurar um tempo para carregamento da página
# time sleep só usamos no local que desejamos aguardar um tempo diferenciado
time.sleep(5)

pyautogui.click(x=-1218, y=235)

pyautogui.write ("pedro.magalhaes.oliveira@hotmail.com")

pyautogui.press("tab") #passou para o próximo campo
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

import pandas #--> uso para importação de base de dados

# pandas.read_csv ("produtos.csv")--> foi criada uma variável para ler a tabela

tabela = pandas.read_csv ("produtos.csv")

print (tabela)

#cadastrar o produto:

for linha in tabela.index: #index vai representar as linhas da tabela 

    codigo = str(tabela.loc[linha,"codigo"])

    pyautogui.click(x=-1185, y=131)
    pyautogui.write(codigo) #vou copiar para os demais campos.
    pyautogui.press("tab")  #vou copiar para os demais campos.
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    obs= (str(tabela.loc[linha,"obs"]))
    if obs != "nan": 
        pyautogui.write(obs) 
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll (5000) #--> Esse comando a barra de rolagem vai retornar para o inicio do cadastro.




