from random import randint
from tkinter import *
from tkinter import messagebox

#Esta função é para quando o jogadro escolhe PEDRA.
def pedra():
    jogadorp = 'PEDRA'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    randomizador = randint(0, 2)
    computador = (opcoes[randomizador])
    if jogadorp == ('PEDRA') and computador == ('PEDRA'):
        message = (f'EMPATE!!!\nO Computador também escolheu {computador}')
    elif jogadorp == ('PEDRA') and computador == ('PAPEL'):
        message=(f'COMUTADOR venceu!\nO COMPUTADOR escolheu {computador}')
    elif jogadorp == ('PEDRA') and computador == ('TESOURA'):
        message=(f'VOCÊ venceu!\nO computador escolheu {computador}')
    messagebox.showinfo(f'Resultado', message)

#Esta função é para quando o jogador escolhe PAPEL.
def papel():
    jogadorpa = 'PAPEL'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    randomizador = randint(0, 2)
    computador = (opcoes[randomizador])
    if jogadorpa == ('PAPEL') and computador == ('PAPEL'):
        message = (f'EMPATE!!!\nO computador escolheu {computador}')
    elif jogadorpa == ('PAPEL') and computador == ('PEDRA'):
        message =(f'VOCÊ venceu!\nComputador escolheu {computador}')
    elif jogadorpa == ('PAPEL') and computador == ('TESOURA'):
        message = (f'COMPUTADOR venceu!\nComputador escolheu {computador}')
    messagebox.showinfo(f'Resultado', message)


#Esta função é para quando o jogador escolhe TESOURA.
def tesoura():
    jogadort = 'TESOURA'
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    randomizador = randint(0, 2)
    computador = (opcoes[randomizador])
    print(f'O computador jogou {computador}')
    if jogadort == ('TESOURA') and computador == ('TESOURA'):
        message= (f'EMPATE!!!\nO Computador também escolheu {computador}')
    if jogadort == ('TESOURA') and computador == ('PEDRA'):
        message = (f'COMPUTADOR venceu!\nO computador escolheu {computador}')
    if jogadort == ('TESOURA') and computador == ('PAPEL'):
        message = (f'VOCÊ venceu!\nComputador escolheu {computador}')

    messagebox.showinfo('Resultado', message)


#interface

janela = Tk()
janela.title('JOKENPO')#titulo da janela
janela.geometry('250x350')#tamanho da janela

texto_orientacao = Label(janela, text='PEDRA, PAPEL OU TESOURA?')#Label precisa saber de onde ele é, e o que será escrito.
texto_orientacao.grid(column=0, row=0, padx=20, pady=20)

botaopedra = Button(janela, text='PEDRA',padx=22, command=pedra)
botaopedra.grid(column=0,padx=10, pady=10, row=1)

botaopapel = Button(janela, text='PAPEL', padx=22, command=papel)
botaopapel.grid(column=0, row=2,padx=10, pady=10)

botaotes = Button(janela, text='TESOURA', command=tesoura)
botaotes.grid(column=0, row=3, padx=10, pady=10)


janela.mainloop()