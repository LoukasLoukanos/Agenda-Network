from os import replace
from tkinter import *
from tkinter import ttk
from tkinter.font import names

#WINDOW MAIN________________________________________________________
tk = Tk()
tk.title("NETWORKING? FLORENÇA")
tk.geometry('600x370+230+75')

tk.resizable(width=0, height=0)
tk.configure(background="#f0f0f0", padx=0, pady=0)

#MENU '☰' COMMANDS_____________________________________________
def adc():
    tk_adc = Tk()
    tk_adc.title("NETWORKING? FLORENÇA")
    tk_adc.geometry('400x300+230+75')

    tk_adc.resizable(width=0, height=0)
    tk_adc.configure(background='#1d1e3a', padx=0, pady=0)

    def fields():
        def attribut_and_value():
            archive = open(id_contact.get() + ".txt", 'w+')# 'w+' cria o arquivo
            archive.close

            def save():
                archive = open(id_contact.get() + ".txt", "a") # 'a' para poder editar o arquivo
                archive.write("%s" % (entry_name_list.get()))

                archive.write("\n %s" % (attribut_.get()+"   |"+value_.get()))
                archive.close

            f = Frame(tk_adc, borderwidth=0, relief="sunke", background="#1d1e3a")
            f.place(x=0, y=0, height=300, width=400)

            l_attribut = Label(tk_adc, text="Um atributo ao contato:", font="arial 9 bold", fg="#ffffff", bg="#1d1e3a")
            l_attribut.place(x=130, y=40)

            attribut_ = Entry(tk_adc, font="arial 8 bold", fg="#ffffff", bg="#1d1e3a", width=21)
            attribut_.place(x=134, y=60)

            l_value = Label(tk_adc, text="O valor desse atributo:", font="arial 9 bold", fg="#ffffff", bg="#1d1e3a")
            l_value.place(x=130, y=80)

            value_ = Entry(tk_adc, font="arial 8 bold", fg="#ffffff", bg="#1d1e3a", width=21)
            value_.place(x=134, y=100)

            but = Button(tk_adc, text='Adicionar', font="arial 8 bold", fg="#ffffff", bg="#1d1e3a", height=1, width=8, borderwidth=1, relief="ridge",command=save)
            but.place(x=168, y=135)


        f = Frame(tk_adc, borderwidth=0, relief="sunke", background="#1d1e3a")
        f.place(x=0, y=0, height=300, width=400)

        l = Label(tk_adc, text="Um nome para identificar o novo contato:", font="arial 10 bold", fg="#ffffff", bg="#1d1e3a")
        l.place(x=68, y=70)

        id_contact = Entry(tk_adc, font="arial 8 bold", fg="#ffffff", bg="#1d1e3a", width=21)
        id_contact.place(x=135, y=100)

        but = Button(tk_adc, text='Inserir', font="arial 8 bold", fg="#ffffff", bg="#1d1e3a", height=1, width=6, borderwidth=1, relief="ridge",command=attribut_and_value)
        but.place(x=175, y=120)

    l = Label(tk_adc, text="Inserir na lista:", font="arial 10 bold", fg="#ffffff", bg="#1d1e3a")
    l.place(x=150, y=70)

    lists = ["iveco SJP", "Fiat Ctba", "Jeep Ctba", "Lista Pessoal"]
    entry_name_list = ttk.Combobox(tk_adc, font="arial 8 bold", values=lists, width=9)
    entry_name_list.place(x=161, y=99)

    but_select = Button(tk_adc, text='Selecionar', font="arial 8 bold", fg="#ffffff", bg="#1d1e3a", height=1, width=8, borderwidth=1, relief="ridge",command=fields)
    but_select.place(x=168, y=121)

def edit():
    tk = Tk()
    tk.title("NETWORKING? FLORENÇA")
    tk.geometry('400x300+230+75')

    tk.resizable(width=0, height=0)
    tk.configure(background='#1d1e3a', padx=0, pady=0)

    def edit_saving():
        variavel_nome_arquivo = None
        variavel_para_conteúdo_que_sera_esquito_no_arquivo = None
        sav = open(variavel_nome_arquivo, "a")
        sav.write("%d" % (variavel_para_conteúdo_que_sera_esquito_no_arquivo))
        sav.close

def delete():
    tk = Tk()
    tk.title("NETWORKING? FLORENÇA")
    tk.geometry('400x300+230+75')

    tk.resizable(width=0, height=0)
    tk.configure(background='#1d1e3a', padx=0, pady=0)

    def deleting():
            variavel_nome_arquivo = None
            delet = open(variavel_nome_arquivo+".txt", "w")#"W" limpa o contreúdo do arquivo
            delet.close
            #isso apenas limpa o conteúdo, → criar code para deletar o arquivo

#MENU 'LOCAIS' COMMANDS_____________________________________________
def listas_fiat():
    global photo_fiat_wallpaper, entry_name
    photo_fiat_wallpaper = PhotoImage(file='fiat_wallpaper.png')
    l1 = Label(tk, image=photo_fiat_wallpaper, compound='bottom')
    l1.place(x=-2, y=-2)
    
    reading_ids_fiat()
    entry_name = ttk.Combobox(tk, font="arial 8", values=ids_list, width=11)
    entry_name.place(x=254, y=140)
    but_pesq = Button(tk, text='Pesquisar', font="arial 8 bold", fg="#000000", bg="#ffffff", height=1, width=8, borderwidth=1, relief="ridge",command=click_pesq)
    but_pesq.place(x=267, y=163)

def listas_iveco():
    global photo_iveco_wallpaper, entry_name
    photo_iveco_wallpaper = PhotoImage(file='iveco_wallpaper.png')
    l1 = Label(tk, image=photo_iveco_wallpaper, compound='bottom')
    l1.place(x=-40, y=-2)
    
    reading_ids_iveco()
    entry_name = ttk.Combobox(tk, font="arial 8", values=ids_list, width=11)
    entry_name.place(x=254, y=140)
    but_pesq = Button(tk, text='Pesquisar', font="arial 8 bold", fg="#000000", bg="#ffffff", height=1, width=8, borderwidth=1, relief="ridge",command=click_pesq)
    but_pesq.place(x=267, y=163)

def listas_jeep():
    global photo_jeep_wallpaper, entry_name
    photo_jeep_wallpaper = PhotoImage(file='jeep_wallpaper.png')
    l1 = Label(tk, image=photo_jeep_wallpaper, compound='bottom')
    l1.place(x=-60, y=-2)
    
    reading_ids_jeep()
    entry_name = ttk.Combobox(tk, font="arial 8", values=ids_list, width=11)
    entry_name.place(x=254, y=140)
    but_pesq = Button(tk, text='Pesquisar', font="arial 8 bold", fg="#000000", bg="#ffffff", height=1, width=8, borderwidth=1, relief="ridge",command=click_pesq)
    but_pesq.place(x=267, y=163)

def listas_todas():
    global photo_network_wallpaper, entry_name
    photo_network_wallpaper = PhotoImage(file='network_wallpaper.png')
    l1 = Label(tk, image=photo_network_wallpaper, compound='bottom')
    l1.place(x=-2, y=-2)
    
    reading_ids_todas()
    entry_name = ttk.Combobox(tk, font="arial 8", values=ids_list, width=11)
    entry_name.place(x=254, y=140)
    but_pesq = Button(tk, text='Pesquisar', font="arial 8 bold", fg="#000000", bg="#ffffff", height=1, width=8, borderwidth=1, relief="ridge",command=click_pesq)
    but_pesq.place(x=267, y=163)

def lista_pessoal():
    global photo_network_wallpaper, entry_name
    photo_network_wallpaper = PhotoImage(file='network_wallpaper.png')
    l1 = Label(tk, image=photo_network_wallpaper, compound='bottom')
    l1.place(x=-2, y=-2)
    
    reading_ids_pessoal()
    entry_name = ttk.Combobox(tk, font="arial 8", values=ids_list, width=11)
    entry_name.place(x=254, y=140)
    but_pesq = Button(tk, text='Pesquisar', font="arial 8 bold", fg="#000000", bg="#ffffff", height=1, width=8, borderwidth=1, relief="ridge",command=click_pesq)
    but_pesq.place(x=267, y=163)

#MENU WIDGET_________________________________________________________
menu_bar = Menu(tk)
menu_main = Menu(menu_bar, tearoff=0)
menu_main.add_command(label="Novo", command=adc)
menu_main.add_command(label="Editar", command=edit)
menu_main.add_command(label="Deletar", command=delete)
menu_main.add_separator()
menu_main.add_command(label="Fechar", command=tk.quit)
menu_bar.add_cascade(label="☰", menu=menu_main)

menu_2 = Menu(menu_bar, tearoff=0)
menu_2.add_command(label="Fiat Ctba", command=listas_fiat)
menu_2.add_command(label="Iveco SJP", command=listas_iveco)
menu_2.add_command(label="Jeep Ctba", command=listas_jeep)
menu_2.add_separator()
menu_2.add_command(label="Minha Lista", command=lista_pessoal)
menu_2.add_separator()
menu_2.add_command(label="Todas", command=listas_todas)
menu_bar.add_cascade(label="Locais", menu=menu_2)

menu_3 = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Sobre", menu=menu_3, command=None)

tk.config(menu=menu_bar)

#LEITURA DE IDS DE LISTAS________________________________________
#criar link para um diretório e ler e criar um array com todos os nomes dos arquivos desse diretório para serem usados em um for um por um como segue↓....
def reading_ids_fiat():
    #o link do repositório da fiat vai aqui.....
    global ids_list
    ids_list = []
    ids_file = open("01ids_fiat.txt")
    ids = ids_file.readlines()
    for line in ids:
        line = line.rstrip('\n')
        ids_list.append(line)
    ids_file.close()

def reading_ids_iveco():
    global ids_list
    ids_list = []
    ids_file = open("02ids_iveco.txt")
    ids = ids_file.readlines()
    for line in ids:
        line = line.rstrip('\n')
        ids_list.append(line)
    ids_file.close()

def reading_ids_jeep():
    global ids_list
    ids_list = []
    ids_file = open("03ids_jeep.txt")
    ids = ids_file.readlines()
    for line in ids:
        line = line.rstrip('\n')
        ids_list.append(line)
    ids_file.close()

def reading_ids_pessoal():
    global ids_list
    ids_list = []
    ids_file = open("04ids_pessoal.txt")
    ids = ids_file.readlines()
    for line in ids:
        line = line.rstrip('\n')
        ids_list.append(line)
    ids_file.close()

def reading_ids_todas():
    global ids_list
    ids_list = []
    ids_file = open("05ids_todas.txt")
    ids = ids_file.readlines()
    for line in ids:
        line = line.rstrip('\n')
        ids_list.append(line)
    ids_file.close()

#DEFINIÇÃO DE INICIALIZAÇÃO________________________________________
photo_iveco_wallaper = PhotoImage(file='iveco_wallpaper.png')
l1 = Label(tk, bg="#f0f0f0", image=photo_iveco_wallaper, compound='bottom')
l1.place(x=-40, y=-2)

reading_ids_iveco()
entry_name = ttk.Combobox(tk, font="arial 8", values=ids_list, width=11)
entry_name.place(x=254, y=140)

#TREEVIEW__________________________________________________________
def click_pesq():
    global entry_name, names_
    attributes = {}
    indic_attribute = 0
    indic_value = 1
    id_entry = entry_name.get()
    for line in ids_list:
        if id_entry == line:
            file = str(id_entry+".txt")       
            attributes_file = open(file)

            frame_contacts = Frame(tk, borderwidth=1, relief="sunke", background="#1d1e3a")
            frame_contacts.place(x=100, y=191, height=128, width=400)

            tree = ttk.Treeview(frame_contacts, selectmode="browse", column=("colum_n1", "colum_n2"), show='headings')
            
            tree.column("colum_n1", width=74, minwidth=30, stretch=NO)
            tree.heading("#1", text="Atributos")

            tree.column("colum_n2", width=310, minwidth=30, stretch=NO)
            tree.heading("#2", text='Valores')

            for line_attribute_and_value in attributes_file:
                (attribute_, value_) = line_attribute_and_value.split("|")
                attributes[indic_attribute] = attribute_
                attributes[indic_value] = value_
        
                attribute = StringVar()
                attribute_hash = attributes[indic_attribute]
                attribute.set(attribute_hash)
                attribute = attribute.get()

                value = StringVar()
                value_hash = attributes[indic_value]
                value.set(value_hash)
                value = value.get()
            
                line_tree = [attribute, value]

                tree.insert("", END, values=line_tree, tags='line')
                tree.tag_configure('line', foreground='white', background='#1d1e3a')  
        
                tree.grid(row=0, column=0)

                tree.place(relx=0, rely=0, relwidth=0.97, relheight=1)# 100% = 1.0, 50% = 0.5, 2% = 0.02
                

            barra = ttk.Scrollbar(frame_contacts, orient='vertical')
            barra.place(relx=0.97, rely=0, relwidth=0.03, relheight=1)# 100% = 1.0, 50% = 0.5, 2% = 0.02

            barra.configure(command=tree.yview)
            tree.configure(yscrollcommand=barra.set)
            
            attributes_file.close()

#BOTÃO DO TREEVIEW_______________________________________________________
but_pesq = Button(tk, text='Pesquisar', font="arial 8 bold", fg="#000000", bg="#f0f0f0", height=1, width=8, borderwidth=1, relief="ridge",command=click_pesq)
but_pesq.place(x=267, y=163)

mainloop()
