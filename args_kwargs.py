def exibir_poema(data_extenso, *args, **kwargs):
    texto  = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(f"a data por extenso é: {data_extenso}")
    print(mensagem)

exibir_poema("Miércoles de cenizas, quedamos juntos a bailar", "Zen of Python", "Beautiful is better than ugly...", autor="Tim Peters", ano=2004)

### ESTUDAR UM POUCO MAIS  ESSE ASSUNTO DE *args e **kwargs