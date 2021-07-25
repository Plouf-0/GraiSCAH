import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox 
from tkinter.constants import BOTTOM, FLAT, LEFT, YES, BOTH, RIGHT, Y, X, VERTICAL, NO, CENTER, TOP

from DBmanagement import *
from cstecouleur import *

from tkcalendar import DateEntry

######################################################



class Interface(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.minsize(1024, 810)
        self.maxsize(2048, 500000)
        self.title("Grainotheque SCAH   Section Jardinage")
        self.iconbitmap("LOGO_SCAH_OFFICIEL_2014-1_avec_titre.ico")
        self.config(bg = vert_claire)
        self.Menubar()
        self.frame_menu()

    def INIT(self):
        
        try: 
            self.frame_acceuil_inactif()
        except:
            pass
        try:     
            self.frame_membrehist_inactif()
        except:
            pass
        try:     
            self.frame_graineshist_inactif()
        except:
            pass
        try:     
            self.frame_transhist_inactif()
        except:
            pass
        try:     
            self.frame_add_graine_inactif()
        except:
            pass
        try:     
            self.frame_modif_graine_inactif()
        except:
            pass
        try: 
            self.frame_add_mem_inactif()
        except:
            pass
        try:
            self.frame_modif_mem_inactif()
        except:
            pass
        try:
            self.frame_add_trans_inactif()
        except:
            pass
        try:
            self.frame_fiche_graine_inactif()
        except:
            pass
        try:
            self.frame_fiche_membre_inactif()            
        except:
            pass  


    #frame du menu
    def frame_menu(self):
        
        self.INIT()

        self.framenu = tk.Frame(self, bg = vert_claire)
        self.framenu.grid()

        self.framenubout = tk.Frame(self.framenu, bg = vert_claire)
        self.framenubout.grid(row = 1, padx = 0, sticky = "w")

        self.framenupic = tk.Frame(self.framenu, bg = vert_claire)
        self.framenupic.grid(row = 2)
        
        self.label = tk.Label(self.framenubout, text = "Bienvenue sur la Grainotheque des Jardiniers", bg = vert_claire, fg = vert_foncé, font = ("Oswald", 30))
        self.label.pack()
        
        self.bouton_acceuil = tk.Button(self.framenubout, text = "Acceuil",font = ("Montserrat", 14), bg = orange, fg = vert_claire, relief = FLAT, command = lambda: self.frame_acceuil_actif())
        self.bouton_acceuil.pack(side = LEFT, anchor = "n", pady=20)
        
        self.bouton_graines = tk.Button(self.framenubout, text = "Graines",font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: [self.framenu.grid_forget(), self.frame_graineshist_actif()])
        self.bouton_graines.pack(side = LEFT, anchor = "n", pady=20)
        
        self.bouton_membres = tk.Button(self.framenubout, text = "Membres",font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: [self.framenu.grid_forget(), self.frame_membrehist_actif()])
        self.bouton_membres.pack(side = LEFT, anchor = "n", pady=20)
        
        self.bouton_transaction = tk.Button(self.framenubout, text = "Transactions",font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: [self.framenu.grid_forget(), self.frame_transhist_actif()])
        self.bouton_transaction.pack(side = LEFT, anchor = "n", pady=20)

        can1 = tk.Canvas(self.framenupic, width = 800, height = 500, bg = vert_claire, highlightthickness = 0)
        imagescah = PhotoImage(file = "LOGO_SCAH_OFFICIEL_2014-1_avec_titre.gif")
        can1.create_image(520, 250, image = imagescah)
        can1.image = imagescah
        can1.pack(expand = YES, fill = BOTH)

    def frame_acceuil_actif(self):
        self.frame_menu()
    def frame_acceuil_inactif(self):
        self.framenu.grid_forget()


    #historique graines
    def frame_hist_graine(self):        
        
        self.INIT()

        self.frame_his_grain_fond = tk.Frame(self, bg = vert_claire)
        self.frame_his_grain_fond.grid()

        self.frame_his_grain_heading = tk.Frame(self.frame_his_grain_fond, bg = vert_claire)
        self.frame_his_grain_heading.grid(row = 1, sticky = "nw")

        self.frame_his_grain_table = tk.Frame(self.frame_his_grain_fond, bg = orange, borderwidth = 2)
        self.frame_his_grain_table.grid(row = 2, pady = 20, padx = 35)
        
        self.frame_his_grain_buttons = tk.Frame(self.frame_his_grain_fond, bg = vert_claire)
        self.frame_his_grain_buttons.grid(row = 3, sticky = "we")

        self.label = tk.Label(self.frame_his_grain_heading, text = "Inventaire de toutes les graines disponibles", bg = vert_claire, fg = vert_foncé, font = ("Oswald", 30))
        self.label.pack()
        
        table_seeds = ttk.Treeview(self.frame_his_grain_table, columns = (1, 2, 3, 4, 5, 6, 7, 8, 9), show = 'headings', height = 30)
        table_seeds.pack(side = LEFT)

        table_seeds.heading(1, text = "Id")
        table_seeds.heading(2, text = "Nom")
        table_seeds.heading(3, text = "Couleur")
        table_seeds.heading(4, text = "Quantité")
        table_seeds.heading(5, text = "Catégorie")
        table_seeds.heading(6, text = "Descendance")
        table_seeds.heading(7, text = "Année de récolte")
        table_seeds.heading(8, text = "Mois de plantation")
        table_seeds.heading(9, text = "Observation")

        table_seeds.column(1, anchor = CENTER, minwidth = 25, width = 25, stretch = YES) #Id
        table_seeds.column(2, minwidth = 75, width = 75, stretch = YES) #Nom
        table_seeds.column(3, minwidth = 100, width = 100, stretch = YES) #Couleur
        table_seeds.column(4, anchor = CENTER, minwidth = 70, width = 70, stretch = YES) #Quantité
        table_seeds.column(5, minwidth = 80, width = 80, stretch = YES) #Catégorie
        table_seeds.column(6, anchor = CENTER, minwidth = 110, width = 110, stretch = YES) #Descendance
        table_seeds.column(7, anchor = CENTER, minwidth = 135, width = 135, stretch = YES) #Année de récolte
        table_seeds.column(8, anchor = CENTER, minwidth = 140, width = 140, stretch = YES) #mois de plantation        
        table_seeds.column(9, minwidth = 200, width = 200, stretch = NO) #Observation

        sb = tk.Scrollbar(self.frame_his_grain_table, orient = VERTICAL)
        sb.pack(side = RIGHT, fill = Y)

        table_seeds.config(yscrollcommand = sb.set)
        sb.config(command = table_seeds.yview)
        
        for i in range(len(get_seeds_values())):
            table_seeds.insert(parent = '', index = i, iid = i, values = (get_seeds_values()[i]))

        self.bouton_fiche_graine = tk.Button(self.frame_his_grain_buttons, text = "Aller\nà la fiche\nde la graine", font = ("Montserrat", 14), bg = orange, fg = vert_claire, relief = FLAT, command = lambda: select_graine())
        self.bouton_fiche_graine.pack(side = LEFT)

        self.bouton_ajouter_graine = tk.Button(self.frame_his_grain_buttons, text = "Ajouter\nla graine\n", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: self.frame_add_graine_actif())
        self.bouton_ajouter_graine.pack(side = LEFT)

        self.bouton_modif_graine = tk.Button(self.frame_his_grain_buttons, text = "Modifier\nla graine\n", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: get_item())
        self.bouton_modif_graine.pack(side = LEFT)

        self.bouton_supr_graine = tk.Button(self.frame_his_grain_buttons, text = "Suprimer\nla graine\n", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: suppr_graine())
        self.bouton_supr_graine.pack(side = LEFT)

        self.bouton_undo_graine = tk.Button(self.frame_his_grain_buttons, text = "Annuler\naction\n(wip)", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: annuler_action())
        self.bouton_undo_graine.pack(side = LEFT)

        self.bouton_acceuil = tk.Button(self.frame_his_grain_buttons, text = "Revenir\nau\nmenu", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: self.frame_acceuil_actif())
        self.bouton_acceuil.pack(side = LEFT)

        def select_graine():
            selected = table_seeds.focus()
            if not selected:
                messagebox.showerror("Erreur", "Il faut sélectionner une graine")
            else: 
                seed = table_seeds.item(selected, 'values')
                self.frame_fiche_graine_actif(seed)

        def get_item():
            selected = table_seeds.focus()
            if not selected:
                messagebox.showerror("Erreur", "Il faut sélectionner une graine")
            else: 
                seed = table_seeds.item(selected, 'values')
                self.frame_modif_graine_actif(seed)

        def suppr_graine():
            selected = table_seeds.focus()
            if not selected:
                messagebox.showerror("Erreur", "Il faut sélectionner une graine")
            else: 
                if messagebox.askokcancel("Confirmation", "Attention, la graine va etre suprimé"):
                    seed = table_seeds.item(selected, 'values')
                    del_seed(seed[0])
                    messagebox.showinfo("Information", "La graine "+seed[1]+" a était suprimée")
                    self.frame_graineshist_actif()
                
        def annuler_action():
            selected = table_seeds.focus()
            if not selected:
                messagebox.showerror("Erreur", "Il faut sélectionner une graine")
            else: 
                seed = table_seeds.item(selected, 'values')
                print(seed)

    def frame_graineshist_actif(self):
        self.frame_hist_graine()
    def frame_graineshist_inactif(self):
        self.frame_his_grain_fond.grid_forget()


    #ajout graine
    def frame_graine_add(self):

        self.INIT()

        self.frame_princ_graine_add = tk.Frame(self, bg = vert_claire)
        self.frame_princ_graine_add.grid(sticky = "we")

        self.frame_graine_add_labelbuton = tk.Frame(self.frame_princ_graine_add, bg = vert_claire)
        self.frame_graine_add_labelbuton.grid(rows = 1, sticky = "we")

        self.frame_graine_add_entries = tk.Frame(self.frame_princ_graine_add, bg = vert_claire)
        self.frame_graine_add_entries.grid(rows = 2, sticky = "we")

        self.frame_graine_add_obs = tk.Frame(self.frame_princ_graine_add, bg = vert_claire)
        self.frame_graine_add_obs.grid(rows = 3, sticky = "we")

        self.label_add = tk.Label(self.frame_graine_add_labelbuton, text = "Ajouter une graine", bg = vert_claire, fg = vert_foncé, font = ("Oswald", 30))
        self.label_add.pack(side = LEFT, anchor = "w")
        
        self.bouton_graine_add_retour = tk.Button(self.frame_graine_add_labelbuton, text = "Retour", font = ("Montserrat", 14), bg = orange_claire, fg = noir, relief = FLAT, command = lambda: retour())
        self.bouton_graine_add_retour.pack(side = RIGHT, anchor = "e")
        
        def retour():
            obs = self.obs_entry.get("1.0", tk.END)
            obs = obs[:-1]
            if self.name_entry.get() or self.color_entry.get() or self.qte_entry.get() or self.desc_entry.get() or self.ann_entry.get() or self.mois_entry.get() or obs:
                rep = messagebox.askokcancel("Attention", "Si les valeurs\nn'ont pas étaient sauvegardées elles seront perdues\nvoulez vous vraiment revenir aux graines ?")
                if rep == True:
                    self.frame_graineshist_actif()
            else:
                self.frame_graineshist_actif()
                
        tk.Label(self.frame_graine_add_entries, text = "Nom", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 1, column = 2)
        tk.Label(self.frame_graine_add_entries, text = "Couleur", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 1, column = 4)
        tk.Label(self.frame_graine_add_entries, text = "Quantité", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 1, column = 6)
        tk.Label(self.frame_graine_add_entries, text = "Catégorie", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 3, column = 1)
        tk.Label(self.frame_graine_add_entries, text = "Descendance", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 3, column = 3)
        tk.Label(self.frame_graine_add_entries, text = "Année de récolte", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 3, column = 5)
        tk.Label(self.frame_graine_add_entries, text = "Mois de plantation", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 3, column = 7)
        tk.Label(self.frame_graine_add_entries, text = "Observation", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 5, column = 4)

        self.name_entry = tk.Entry(self.frame_graine_add_entries)
        self.name_entry.grid(row = 2, column = 2)
        self.color_entry = tk.Entry(self.frame_graine_add_entries)
        self.color_entry.grid(row = 2, column = 4)
        self.qte_entry = tk.Entry(self.frame_graine_add_entries, width = 5)  #entrée mais avec chiffres uniquement
        self.qte_entry.grid(row = 2, column = 6)        
        self.desc_entry = tk.Entry(self.frame_graine_add_entries, width = 3)  #menu déroulant chiffre
        self.desc_entry.grid(row = 4, column = 3)
        self.ann_entry = tk.Entry(self.frame_graine_add_entries) #menu déroulant 
        self.ann_entry.grid(row = 4, column = 5)
        self.mois_entry = tk.Entry(self.frame_graine_add_entries)
        self.mois_entry.grid(row = 4, column = 7) 
        self.obs_entry = tk.Text(self.frame_graine_add_obs, width = 100, height = 10)
        self.obs_entry.pack()
        
        self.cate_box = ttk.Combobox(self.frame_graine_add_entries, values = get_category(), state = 'readonly')
        self.cate_box.set("Choisir catégorie")
        self.cate_box.grid(row = 4, column = 1)

        self.bouton_graine_add_save = tk.Button(self.frame_graine_add_obs, text = "Sauvegarder la\nnouvelle graine", font = ("Montserrat", 14), bg = orange, fg = noir, relief = FLAT, command = lambda: message_sauvegarde()) 
        self.bouton_graine_add_save.pack()       

        def message_sauvegarde():            
            qte = self.qte_entry.get()
            desc = self.desc_entry.get()
            cate = self.cate_box.get()[0]
            if qte.isdigit() == True:
                if desc.isdigit() == True:
                    if cate != "C":
                        rep = messagebox.askquestion("Sauvegarde", "Confirmer la sauvegarde ?")
                        if rep == 'yes':
                            main_add_graines(None, self.name_entry.get(), self.cate_box.get()[0], self.color_entry.get(), self.qte_entry.get(), self.desc_entry.get(), self.ann_entry.get(), self.mois_entry.get(), self.obs_entry.get("1.0", tk.END))
                            self.name_entry.delete(0, tk.END)
                            self.color_entry.delete(0, tk.END)
                            self.qte_entry.delete(0, tk.END)
                            self.cate_box.set('')
                            self.desc_entry.delete(0, tk.END)
                            self.ann_entry.delete(0, tk.END)
                            self.mois_entry.delete(0, tk.END)
                            self.obs_entry.delete(0, tk.END)
                    else:messagebox.showerror("Erreur", "Il faut choisir une catégorie")        
                else:messagebox.showerror("Erreur", "La descendance doit être un nombre entier")
            else:messagebox.showerror("Erreur", "La quantité doit être un nombre entier")

    def frame_add_graine_actif(self):
        self.frame_graine_add()
    def frame_add_graine_inactif(self):
        self.frame_princ_graine_add.grid_forget()


    #modif graine
    def frame_graine_modif(self, seed):
        
        self.INIT()

        self.frame_princ_graine_modif = tk.Frame(self, bg = vert_claire)
        self.frame_princ_graine_modif.grid()

        self.frame_graine_modif_labelbuton = tk.Frame(self.frame_princ_graine_modif, bg = vert_claire)
        self.frame_graine_modif_labelbuton.grid(rows = 1, sticky = "we")

        self.frame_graine_modif_entries = tk.Frame(self.frame_princ_graine_modif, bg = vert_claire)
        self.frame_graine_modif_entries.grid(rows = 2, sticky = "we")

        self.frame_graine_modif_obs = tk.Frame(self.frame_princ_graine_modif, bg = vert_claire)
        self.frame_graine_modif_obs.grid(rows = 3, sticky = "we")

        tk.Label(self.frame_graine_modif_labelbuton, text = ("Modifier la graine : "+ seed[1]), bg = vert_claire, fg = vert_foncé, font = ("Oswald", 30)).pack(side = LEFT, anchor = "w")
        
        self.bouton_graine_modif_retour = tk.Button(self.frame_graine_modif_labelbuton, text = "Retour", font = ("Montserrat", 14), bg = orange_claire, fg = noir, relief = FLAT, command = lambda: retour())
        self.bouton_graine_modif_retour.pack(side = RIGHT, ipadx = 20)
        
        def retour():
            obs = self.obs_entry.get("1.0", tk.END)
            obs = obs[:-1]
            if self.name_entry.get() != seed[1] or self.color_entry.get() != seed[2] or self.qte_entry.get() != seed[3] or self.desc_entry.get() != seed[5] or self.ann_entry.get() != seed[6] or self.mois_entry.get() != seed[7] or obs != seed[8]:
                rep = messagebox.askokcancel("Attention", "Si les valeurs\nn'ont pas étaient sauvegardées elles seront perdues\nvoulez vous vraiment revenir aux graines ?")
                if rep == True:
                    self.frame_graineshist_actif()
            else:
                self.frame_graineshist_actif()
        def findi(l, a):
                    for i in range(len(l)):
                        if l[i][1] == a:
                            return i

        tk.Label(self.frame_graine_modif_entries, text = "Nom", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 1, column = 2)
        tk.Label(self.frame_graine_modif_entries, text = "Couleur", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 1, column = 4)
        tk.Label(self.frame_graine_modif_entries, text = "Quantité", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 1, column = 6)
        tk.Label(self.frame_graine_modif_entries, text = "Catégorie", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 3, column = 1)
        tk.Label(self.frame_graine_modif_entries, text = "Descendance", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 3, column = 3)
        tk.Label(self.frame_graine_modif_entries, text = "Année de récolte", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 3, column = 5)
        tk.Label(self.frame_graine_modif_entries, text = "Mois de plantation", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 3, column = 7)
        tk.Label(self.frame_graine_modif_entries, text = "Observation", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 40).grid(row = 5, column = 4)

        self.name_entry = tk.Entry(self.frame_graine_modif_entries)
        self.name_entry.grid(row = 2, column = 2)
        self.name_entry.insert(0, str(seed[1]))
        self.color_entry = tk.Entry(self.frame_graine_modif_entries)
        self.color_entry.grid(row = 2, column = 4)
        self.color_entry.insert(0, str(seed[2]))
        self.qte_entry = tk.Entry(self.frame_graine_modif_entries, width = 5)  #entrée mais avec chiffres uniquement
        self.qte_entry.grid(row = 2, column = 6)
        self.qte_entry.insert(0, str(seed[3]))
        self.desc_entry = tk.Entry(self.frame_graine_modif_entries, width = 3)  #menu déroulant chiffre
        self.desc_entry.grid(row = 4, column = 3)
        self.desc_entry.insert(0, str(seed[5]))
        self.ann_entry = tk.Entry(self.frame_graine_modif_entries) #menu déroulant 
        self.ann_entry.grid(row = 4, column = 5)
        self.ann_entry.insert(0, str(seed[6]))
        self.mois_entry = tk.Entry(self.frame_graine_modif_entries)
        self.mois_entry.grid(row = 4, column = 7) 
        self.mois_entry.insert(0, str(seed[7]))
        
        self.obs_entry = tk.Text(self.frame_graine_modif_obs, width = 100, height = 10)
        self.obs_entry.insert(tk.END, seed[8])
        self.obs_entry.pack()

        self.cate_box = ttk.Combobox(self.frame_graine_modif_entries, state='readonly', values = get_category())
        self.cate_box.grid(row = 4, column = 1)
        self.cate_box.current(findi(get_category(), seed[4]))

        self.bouton_graine_modif_save = tk.Button(self.frame_graine_modif_obs, text = "Sauvegarder la\nnouvelle graine", font = ("Montserrat", 14), bg = orange, fg = noir, relief = FLAT, command = lambda: message_sauvegarde()) 
        self.bouton_graine_modif_save.pack()        

        def message_sauvegarde():
            qte = self.qte_entry.get()
            desc = self.desc_entry.get()
            if qte.isdigit() == True:
                if desc.isdigit() == True:
                        rep = messagebox.askquestion("Sauvegarde", "Confirmer la sauvegarde ?")
                        if rep == 'yes':
                            selection = self.cate_box.get()
                            cate_id = [int(s) for s in selection.split() if s.isdigit()]
                            main_modif_graines(seed[0], self.name_entry.get(), cate_id[0], self.color_entry.get(), self.qte_entry.get(), self.desc_entry.get(), self.ann_entry.get(), self.mois_entry.get(), self.obs_entry.get("1.0", tk.END))
                            self.frame_graineshist_actif()
                else:messagebox.showerror("Erreur", "La descendance doit être un nombre entier")
            else:messagebox.showerror("Erreur", "La quantité doit être un nombre entier")

    def frame_modif_graine_actif(self, mem):
        self.frame_graine_modif(mem)
    def frame_modif_graine_inactif(self):
        self.frame_princ_graine_modif.grid_forget()   


    #fiche graine
    def frame_fiche_graine(self, seed): 

        print(seed)

        self.INIT()

        self.frame_fiche_graine_fond = tk.Frame(self, bg = vert_claire)    
        self.frame_fiche_graine_fond.grid()

        self.frame_fiche_graine_fond_1 = tk.Frame(self.frame_fiche_graine_fond, bg = vert_claire)    
        self.frame_fiche_graine_fond_1.grid(row = 1, sticky = "we")

        self.frame_fiche_graine_photo = tk.Frame(self.frame_fiche_graine_fond_1, bg = vert_claire)
        self.frame_fiche_graine_photo.grid(row = 1, column = 1)

        self.frame_fiche_graine_nc = tk.Frame(self.frame_fiche_graine_fond_1, bg = vert_claire)
        self.frame_fiche_graine_nc.grid(row = 1, column = 2)

        self.frame_fiche_graine_vals_g = tk.Frame(self.frame_fiche_graine_fond_1, bg = vert_claire)
        self.frame_fiche_graine_vals_g.grid(row = 2, column = 1)

        self.frame_fiche_graine_vals_d = tk.Frame(self.frame_fiche_graine_fond_1, bg = vert_claire)
        self.frame_fiche_graine_vals_d.grid(row = 2, column = 2)
        
        self.frame_fiche_graine_fond_obs = tk.Frame(self.frame_fiche_graine_fond, bg = vert_claire)    
        self.frame_fiche_graine_fond_obs.grid(row = 2, sticky = "we")

        tk.Label(self.frame_fiche_graine_fond, text = "Fiche de graine", bg = vert_claire, fg = vert_foncé, font = (None, 30)).grid(row = 0)
        
        self.bouton_graine_fiche_retour = tk.Button(self.frame_fiche_graine_fond, text = "Retour", font = ("Montserrat", 14), bg = orange_claire, fg = noir, relief = FLAT, command = lambda: self.frame_graineshist_actif())
        self.bouton_graine_fiche_retour.grid(row = 0, column = 1, sticky = "e")
 
        can_photo = tk.Canvas(self.frame_fiche_graine_photo, width = 500, height = 320, bg = vert_claire, highlightthickness = 0)
        imagegraine = PhotoImage(file = "default_pic.gif")
        can_photo.create_image(250, 150, image = imagegraine)
        can_photo.image = imagegraine
        can_photo.pack(expand = YES, fill = BOTH)

        tk.Label(self.frame_fiche_graine_nc, text = "Nom:", bg = vert_claire, fg = noir, font = (None, 30)).grid(row = 1, sticky = "w")
        tk.Label(self.frame_fiche_graine_nc, text = seed[1], bg = vert_claire, fg = vert_foncé, font = (None, 28), ).grid(row = 2, sticky = "w", ipady = 10)
        tk.Label(self.frame_fiche_graine_nc, text = "Couleur:", bg = vert_claire, fg = noir, font = (None, 30)).grid(row = 3, sticky = "w")
        tk.Label(self.frame_fiche_graine_nc, text = seed[2], bg = vert_claire, fg = vert_foncé, font = (None, 28)).grid(row = 4, sticky = "w")

        tk.Label(self.frame_fiche_graine_vals_d, text = "Quantité:", bg = vert_claire, fg = noir, font = (None, 22)).grid(row = 1, sticky = "w")
        tk.Label(self.frame_fiche_graine_vals_d, text = seed[3], bg = vert_claire, fg = vert_foncé, font = (None, 20)).grid(row = 2, sticky = "w", ipady = 10)
        tk.Label(self.frame_fiche_graine_vals_d, text = "Année de récolte:", bg = vert_claire, fg = noir, font = (None, 22)).grid(row = 3, sticky = "w")
        tk.Label(self.frame_fiche_graine_vals_d, text = seed[6], bg = vert_claire, fg = vert_foncé, font = (None, 20)).grid(row = 4, sticky = "w", ipady = 10)
        tk.Label(self.frame_fiche_graine_vals_d, text = "Descendance:", bg = vert_claire, fg = noir, font = (None, 22)).grid(row = 5, sticky = "w")
        tk.Label(self.frame_fiche_graine_vals_d, text = seed[5], bg = vert_claire, fg = vert_foncé, font = (None, 20)).grid(row = 6, sticky = "w")

        tk.Label(self.frame_fiche_graine_vals_g, text = "Catégorie:", bg = vert_claire, fg = noir, font = (None, 22)).grid(row = 1, sticky = "w")
        tk.Label(self.frame_fiche_graine_vals_g, text = seed[4], bg = vert_claire, fg = vert_foncé, font = (None, 20)).grid(row = 2, sticky = "w", ipady = 10)
        tk.Label(self.frame_fiche_graine_vals_g, text = "Mois de plantation:", bg = vert_claire, fg = noir, font = (None, 22)).grid(row = 3, sticky = "w")
        tk.Label(self.frame_fiche_graine_vals_g, text = seed[7], bg = vert_claire, fg = vert_foncé, font = (None, 20)).grid(row = 4, sticky = "w")

        tk.Label(self.frame_fiche_graine_fond_obs, text = "Observation:", bg = vert_claire, fg = noir, font = (None, 22)).pack(side = TOP, ipady = 15)
        self.obs_display = tk.Text(self.frame_fiche_graine_fond_obs, width = 100, height = 10)
        self.obs_display.insert(tk.END, seed[8])
        self.obs_display.pack(side = BOTTOM)

    def frame_fiche_graine_actif(self, seed):
        self.frame_fiche_graine(seed)
    def frame_fiche_graine_inactif(self):
        self.frame_fiche_graine_fond.grid_forget()  

    
    #historique membre
    def frame_hist_membres(self):
        
        self.INIT()

        self.frame_his_mem_fond = tk.Frame(self, bg = vert_claire)
        self.frame_his_mem_fond.grid(sticky = "nw")

        self.frame_his_mem_heading = tk.Frame(self.frame_his_mem_fond, bg = vert_claire)
        self.frame_his_mem_heading.grid(row = 1, sticky = "nw")

        self.frame_his_mem_table = tk.Frame(self.frame_his_mem_fond, bg = orange, borderwidth = 2)
        self.frame_his_mem_table.grid(row = 2, pady = 20, padx = 35)
        
        self.frame_his_mem_buttons = tk.Frame(self.frame_his_mem_fond, bg = vert_claire)
        self.frame_his_mem_buttons.grid(row = 3, sticky = "we")
        
        self.label = tk.Label(self.frame_his_mem_heading, text = "Liste de tous les membres", bg = vert_claire, fg = vert_foncé, font = ("Oswald", 30))
        self.label.pack()
        
        table_mem = ttk.Treeview(self.frame_his_mem_table, columns = (1, 2, 3, 4, 5, 6, 7, 8), show = 'headings', height = 30)
        table_mem.pack(side = LEFT, fill = X)

        table_mem.heading(1, text = "Id")
        table_mem.heading(2, text = "Nom")
        table_mem.heading(3, text = "Prénom")
        table_mem.heading(4, text = "Telephone")
        table_mem.heading(5, text = "Email")
        table_mem.heading(6, text = "Ville")
        table_mem.heading(7, text = "Donation")
        table_mem.heading(8, text = "Reception")

        table_mem.column(1, anchor = CENTER, minwidth = 25, width = 25, stretch = YES) #Id
        table_mem.column(2, minwidth = 75, width = 75, stretch = YES) #Nom
        table_mem.column(3, minwidth = 100, width = 100, stretch = YES) #Prénom
        table_mem.column(4, anchor = CENTER, minwidth = 70, width = 70, stretch = YES) #Telephone
        table_mem.column(5, minwidth = 80, width = 80, stretch = YES) #Email
        table_mem.column(6, minwidth = 110, width = 110, stretch = YES) #Ville
        table_mem.column(7, anchor = CENTER, minwidth = 70, width = 70, stretch = YES) #Donation
        table_mem.column(8, anchor = CENTER, minwidth = 70, width = 70, stretch = YES) #Reception        

        sb = tk.Scrollbar(self.frame_his_mem_table, orient = VERTICAL)
        sb.pack(side = RIGHT, fill = Y)

        table_mem.config(yscrollcommand = sb.set)
        sb.config(command = table_mem.yview)
        
        for i in range(len(get_member())):
            table_mem.insert(parent = '', index = i, iid = i, values = (get_member()[i]))

        self.bouton_fiche_mem = tk.Button(self.frame_his_mem_buttons, text = "Aller\nà la fiche\ndu membre", font = ("Montserrat", 14), bg = orange, fg = vert_claire, relief = FLAT, command = lambda: select_membre())
        self.bouton_fiche_mem.pack(side = LEFT)

        self.bouton_ajouter_mem = tk.Button(self.frame_his_mem_buttons, text = "Ajouter\nle membre\n", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: self.frame_add_mem_actif())
        self.bouton_ajouter_mem.pack(side = LEFT)

        self.bouton_modif_mem = tk.Button(self.frame_his_mem_buttons, text = "Modifier\nle membre\n", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: get_item())
        self.bouton_modif_mem.pack(side = LEFT)

        self.bouton_supr_mem = tk.Button(self.frame_his_mem_buttons, text = "Suprimer\nle membre\n", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: suppr_mem())
        self.bouton_supr_mem.pack(side = LEFT)

        self.bouton_undo_mem = tk.Button(self.frame_his_mem_buttons, text = "Annuler\naction\n(wip)", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: annuler_action())
        self.bouton_undo_mem.pack(side = LEFT)

        self.bouton_acceuil = tk.Button(self.frame_his_mem_buttons, text = "Revenir\nau\nmenu", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: self.frame_acceuil_actif())
        self.bouton_acceuil.pack(side = LEFT)
        
        def select_membre():
            selected = table_mem.focus()
            if not selected:
                messagebox.showerror("Erreur", "Il faut sélectionner un membre")
            else: 
                mem = table_mem.item(selected, 'values')
                self.frame_fiche_membre_actif(mem)
        
        def get_item():
            selected = table_mem.focus()
            if not selected:
                messagebox.showerror("Erreur", "Il faut sélectionner un membre")
            else: 
                mem = table_mem.item(selected, 'values')
                self.frame_modif_mem_actif(mem)

        def suppr_mem():
            selected = table_mem.focus()
            if not selected:
                messagebox.showerror("Erreur", "Il faut sélectionner un membre")
            else: 
                if messagebox.askokcancel("Confirmation", "Attention, le membre va etre suprimé"):
                    mem = table_mem.item(selected, 'values')
                    del_mem(mem[0])
                    messagebox.showinfo("Information", "Le membre "+mem[1]+" a était suprimée")
                    self.frame_membrehist_actif()
                
        def annuler_action():
            selected = table_mem.focus()
            if not selected:
                messagebox.showerror("Erreur", "Il faut sélectionner une graine")
            else: 
                seed = table_mem.item(selected, 'values')
                print(seed)
    
    def frame_membrehist_actif(self):
        self.frame_hist_membres()
    def frame_membrehist_inactif(self):
        self.frame_his_mem_fond.grid_forget()
    

    #ajoute membre
    def frame_mem_add(self):

        self.INIT()

        self.frame_princ_mem_add = tk.Frame(self, bg = vert_claire)
        self.frame_princ_mem_add.grid(sticky = "we")

        self.frame_mem_add_labelbuton = tk.Frame(self.frame_princ_mem_add, bg = vert_claire)
        self.frame_mem_add_labelbuton.grid(rows = 1, sticky = "we")

        self.frame_mem_add_entries = tk.Frame(self.frame_princ_mem_add, bg = vert_claire)
        self.frame_mem_add_entries.grid(rows = 2, sticky = "we")

        self.label_add = tk.Label(self.frame_mem_add_labelbuton, text = "Ajouter un membre", bg = vert_claire, fg = vert_foncé, font = ("Oswald", 30))
        self.label_add.pack(side = LEFT, anchor = "w")
        
        self.bouton_mem_add_retour = tk.Button(self.frame_mem_add_labelbuton, text = "Retour", font = ("Montserrat", 14), bg = orange_claire, fg = noir, relief = FLAT, command = lambda: retour())
        self.bouton_mem_add_retour.pack(side = RIGHT, anchor = "e")
        
        def retour():
            if self.name_entry.get() or self.fname_entry.get() or self.tel_entry.get() or self.mail_entry.get() or self.city_entry.get() or self.don_entry.get() or self.rec_entry.get():
                rep = messagebox.askokcancel("Attention", "Si les valeurs\nn'ont pas étaient sauvegardées elles seront perdues\nvoulez vous vraiment revenir aux membres ?")
                if rep == True:
                    self.frame_membrehist_actif()
            else:
                self.frame_membrehist_actif()
                
        tk.Label(self.frame_mem_add_entries, text = "Nom", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 1, column = 2)
        tk.Label(self.frame_mem_add_entries, text = "Prénom", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 1, column = 4)
        tk.Label(self.frame_mem_add_entries, text = "Telephone", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 3, column = 1)
        tk.Label(self.frame_mem_add_entries, text = "Email", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 3, column = 3)
        tk.Label(self.frame_mem_add_entries, text = "Ville", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 3, column = 5)
        tk.Label(self.frame_mem_add_entries, text = "Donation", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 5, column = 2)
        tk.Label(self.frame_mem_add_entries, text = "Reception", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 5, column = 4)

        self.name_entry = tk.Entry(self.frame_mem_add_entries)
        self.name_entry.grid(row = 2, column = 2)
        self.fname_entry = tk.Entry(self.frame_mem_add_entries)
        self.fname_entry.grid(row = 2, column = 4)
        self.tel_entry = tk.Entry(self.frame_mem_add_entries, width = 11)
        self.tel_entry.grid(row = 4, column = 1)        
        self.mail_entry = tk.Entry(self.frame_mem_add_entries, width = 30)
        self.mail_entry.grid(row = 4, column = 3)
        self.city_entry = tk.Entry(self.frame_mem_add_entries)
        self.city_entry.grid(row = 4, column = 5)
        self.don_entry = tk.Entry(self.frame_mem_add_entries)
        self.don_entry.grid(row = 6, column = 2) 
        self.rec_entry = tk.Entry(self.frame_mem_add_entries)
        self.rec_entry.grid(row = 6, column = 4)

        self.bouton_mem_add_save = tk.Button(self.frame_mem_add_entries, text = "Sauvegarder le\nnouveau membre", font = ("Montserrat", 14), bg = orange, fg = noir, relief = FLAT, command = lambda: message_sauvegarde()) 
        self.bouton_mem_add_save.grid(row = 7, column = 3, pady = 10)       

        def message_sauvegarde():            
            tel = self.tel_entry.get()
            don = self.don_entry.get()
            rec = self.rec_entry.get()
            if tel:
                print()
            else:
                tel = "0"
            if don:
                print()
            else:
                don = "0"
            if rec:
                print()
            else:
                rec = "0"
            if tel.isdigit() == True:
                if don.isdigit() == True:
                    if rec.isdigit() == True:
                        rep = messagebox.askquestion("Sauvegarde", "Confirmer la sauvegarde ?")
                        if rep == 'yes':
                            main_add_member(None, self.name_entry.get(), self.fname_entry.get(), self.tel_entry.get(), self.mail_entry.get(), self.city_entry.get(), self.don_entry.get(), self.rec_entry.get())
                            self.name_entry.delete(0,tk.END)
                            self.fname_entry.delete(0,tk.END)
                            self.tel_entry.delete(0,tk.END)
                            self.mail_entry.delete(0,tk.END)
                            self.city_entry.delete(0,tk.END)
                            self.don_entry.delete(0,tk.END)
                            self.rec_entry.delete(0, tk.END)
                    else:messagebox.showerror("Erreur", "La reception doit être un nombre entier")        
                else:messagebox.showerror("Erreur", "La donation doit être un nombre entier")
            else:messagebox.showerror("Erreur", "Le telephone doit être un nombre entier")

    def frame_add_mem_actif(self):
        self.frame_mem_add()
    def frame_add_mem_inactif(self):
        self.frame_princ_mem_add.grid_forget()


    #modif mem
    def frame_mem_modif(self, mem):
        
        self.INIT()

        self.frame_princ_mem_modif = tk.Frame(self, bg = vert_claire)
        self.frame_princ_mem_modif.grid()

        self.frame_mem_modif_labelbuton = tk.Frame(self.frame_princ_mem_modif, bg = vert_claire)
        self.frame_mem_modif_labelbuton.grid(rows = 1, sticky = "we")

        self.frame_mem_modif_entries = tk.Frame(self.frame_princ_mem_modif, bg = vert_claire)
        self.frame_mem_modif_entries.grid(rows = 2, sticky = "we")

        tk.Label(self.frame_mem_modif_labelbuton, text = ("Modifier le membre : "+ mem[1]), bg = vert_claire, fg = vert_foncé, font = ("Oswald", 30)).pack(side = LEFT, anchor = "w")
        
        self.bouton_mem_modif_retour = tk.Button(self.frame_mem_modif_labelbuton, text = "Retour", font = ("Montserrat", 14), bg = orange_claire, fg = noir, relief = FLAT, command = lambda: retour())
        self.bouton_mem_modif_retour.pack(side = RIGHT, ipadx = 20)
        
        def retour():
            if self.name_entry.get() != mem[1] or self.fname_entry.get() != mem[2] or self.tel_entry.get() != mem[3] or self.mail_entry.get() != mem[4] or self.city_entry.get() != mem[5] or self.don_entry.get() != mem[6] or self.rec_entry.get() != mem[7]:
                rep = messagebox.askokcancel("Attention", "Si les valeurs\nn'ont pas étaient sauvegardées elles seront perdues\nvoulez vous vraiment revenir aux membres ?")
                if rep == True:
                    self.frame_membrehist_actif()
            else:
                self.frame_membrehist_actif()

        tk.Label(self.frame_mem_modif_entries, text = "Nom", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 1, column = 2)
        tk.Label(self.frame_mem_modif_entries, text = "Prénom", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 1, column = 4)
        tk.Label(self.frame_mem_modif_entries, text = "Telephone", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 3, column = 1)
        tk.Label(self.frame_mem_modif_entries, text = "Email", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 3, column = 3)
        tk.Label(self.frame_mem_modif_entries, text = "Ville", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 3, column = 5)
        tk.Label(self.frame_mem_modif_entries, text = "Donation", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 5, column = 2)
        tk.Label(self.frame_mem_modif_entries, text = "Reception", bg = vert_claire, fg = noir, font = (None, 14), padx = 10, pady = 20).grid(row = 5, column = 4)

        self.name_entry = tk.Entry(self.frame_mem_modif_entries)
        self.name_entry.grid(row = 2, column = 2)
        self.name_entry.insert(0, str(mem[1]))
        self.fname_entry = tk.Entry(self.frame_mem_modif_entries)
        self.fname_entry.grid(row = 2, column = 4)
        self.fname_entry.insert(0, str(mem[2]))
        self.tel_entry = tk.Entry(self.frame_mem_modif_entries, width = 11)
        self.tel_entry.grid(row = 4, column = 1)
        self.tel_entry.insert(0, str(mem[3]))
        self.mail_entry = tk.Entry(self.frame_mem_modif_entries, width = 30)
        self.mail_entry.grid(row = 4, column = 3)
        self.mail_entry.insert(0, str(mem[4]))
        self.city_entry = tk.Entry(self.frame_mem_modif_entries)
        self.city_entry.grid(row = 4, column = 5)
        self.city_entry.insert(0, str(mem[5]))
        self.don_entry = tk.Entry(self.frame_mem_modif_entries)
        self.don_entry.grid(row = 6, column = 2) 
        self.don_entry.insert(0, str(mem[6]))
        self.rec_entry = tk.Entry(self.frame_mem_modif_entries)
        self.rec_entry.grid(row = 6, column = 4) 
        self.rec_entry.insert(0, str(mem[7]))

        self.bouton_mem_modif_save = tk.Button(self.frame_mem_modif_entries, text = "Sauvegarder le\nnouveau membre", font = ("Montserrat", 14), bg = orange, fg = noir, relief = FLAT, command = lambda: message_sauvegarde()) 
        self.bouton_mem_modif_save.grid(row = 7, column = 3)        

        def message_sauvegarde():
            tel = self.tel_entry.get()
            don = self.don_entry.get()
            rec = self.rec_entry.get()
            if tel.isdigit() == True:
                if don.isdigit() == True:
                    if rec.isdigit() == True:
                        rep = messagebox.askquestion("Sauvegarde", "Confirmer la sauvegarde ?")
                        if rep == 'yes':
                            main_modif_member(mem[0], self.name_entry.get(), self.fname_entry.get(), self.tel_entry.get(), self.mail_entry.get(), self.city_entry.get(), self.don_entry.get(), self.rec_entry.get())
                            self.frame_membrehist_actif()
                    else:messagebox.showerror("Erreur", "La reception doit être un nombre entier")
                else:messagebox.showerror("Erreur", "La donation doit être un nombre entier")
            else:messagebox.showerror("Erreur", "Le téléphone doit être un nombre entier")

    def frame_modif_mem_actif(self, mem):
        self.frame_mem_modif(mem)
    def frame_modif_mem_inactif(self):
        self.frame_princ_mem_modif.grid_forget()
    

    #fiche membre
    def frame_fiche_membre(self, mem): 

        print(mem)

        self.INIT()

        self.frame_fiche_membre_fond = tk.Frame(self, bg = vert_claire)    
        self.frame_fiche_membre_fond.grid()

        self.frame_fiche_membre_fond_1 = tk.Frame(self.frame_fiche_membre_fond, bg = vert_claire)    
        self.frame_fiche_membre_fond_1.grid(row = 1, sticky = "we")

        self.frame_fiche_membre_photo = tk.Frame(self.frame_fiche_membre_fond_1, bg = vert_claire)
        self.frame_fiche_membre_photo.grid(row = 1, column = 1)

        self.frame_fiche_membre_np = tk.Frame(self.frame_fiche_membre_fond_1, bg = vert_claire)
        self.frame_fiche_membre_np.grid(row = 1, column = 2)

        self.frame_fiche_membre_vals_g = tk.Frame(self.frame_fiche_membre_fond_1, bg = vert_claire)
        self.frame_fiche_membre_vals_g.grid(row = 2, column = 1)

        self.frame_fiche_membre_vals_d = tk.Frame(self.frame_fiche_membre_fond_1, bg = vert_claire)
        self.frame_fiche_membre_vals_d.grid(row = 2, column = 2)
        
        tk.Label(self.frame_fiche_membre_fond, text = "Fiche de graine", bg = vert_claire, fg = vert_foncé, font = (None, 30)).grid(row = 0)
        
        self.bouton_membre_fiche_retour = tk.Button(self.frame_fiche_membre_fond, text = "Retour", font = ("Montserrat", 14), bg = orange_claire, fg = noir, relief = FLAT, command = lambda: self.frame_membrehist_actif())
        self.bouton_membre_fiche_retour.grid(row = 0, column = 1, sticky = "e")
 
        can_photo = tk.Canvas(self.frame_fiche_membre_photo, width = 500, height = 320, bg = vert_claire, highlightthickness = 0)
        imagemembre = PhotoImage(file = "default_pic.gif")
        can_photo.create_image(250, 150, image = imagemembre)
        can_photo.image = imagemembre
        can_photo.pack(expand = YES, fill = BOTH)

        tk.Label(self.frame_fiche_membre_np, text = "Nom:", bg = vert_claire, fg = noir, font = (None, 30)).grid(row = 1, sticky = "w")
        tk.Label(self.frame_fiche_membre_np, text = mem[1], bg = vert_claire, fg = vert_foncé, font = (None, 28), ).grid(row = 2, sticky = "w", ipady = 10)
        tk.Label(self.frame_fiche_membre_np, text = "Prénom:", bg = vert_claire, fg = noir, font = (None, 30)).grid(row = 3, sticky = "w")
        tk.Label(self.frame_fiche_membre_np, text = mem[2], bg = vert_claire, fg = vert_foncé, font = (None, 28)).grid(row = 4, sticky = "w")

        tk.Label(self.frame_fiche_membre_vals_d, text = "Téléphone:", bg = vert_claire, fg = noir, font = (None, 22)).grid(row = 1, sticky = "w")
        tk.Label(self.frame_fiche_membre_vals_d, text = mem[3], bg = vert_claire, fg = vert_foncé, font = (None, 20)).grid(row = 2, sticky = "w", ipady = 10)
        tk.Label(self.frame_fiche_membre_vals_d, text = "Ville:", bg = vert_claire, fg = noir, font = (None, 22)).grid(row = 3, sticky = "w")
        tk.Label(self.frame_fiche_membre_vals_d, text = mem[5], bg = vert_claire, fg = vert_foncé, font = (None, 20)).grid(row = 4, sticky = "w", ipady = 10)
        tk.Label(self.frame_fiche_membre_vals_d, text = "E_mail:", bg = vert_claire, fg = noir, font = (None, 22)).grid(row = 5, sticky = "w")
        tk.Label(self.frame_fiche_membre_vals_d, text = mem[4], bg = vert_claire, fg = vert_foncé, font = (None, 20)).grid(row = 6, sticky = "w")

        tk.Label(self.frame_fiche_membre_vals_g, text = "Dons:", bg = vert_claire, fg = noir, font = (None, 22)).grid(row = 1, sticky = "w")
        tk.Label(self.frame_fiche_membre_vals_g, text = mem[6], bg = vert_claire, fg = vert_foncé, font = (None, 20)).grid(row = 2, sticky = "w", ipady = 10)
        tk.Label(self.frame_fiche_membre_vals_g, text = "Réceptions:", bg = vert_claire, fg = noir, font = (None, 22)).grid(row = 3, sticky = "w")
        tk.Label(self.frame_fiche_membre_vals_g, text = mem[7], bg = vert_claire, fg = vert_foncé, font = (None, 20)).grid(row = 4, sticky = "w")

    def frame_fiche_membre_actif(self, mem):
        self.frame_fiche_membre(mem)
    def frame_fiche_membre_inactif(self):
        self.frame_fiche_membre_fond.grid_forget()  


    #historique transactions
    def frame_his_trans(self):
        
        self.INIT()

        self.frame_his_trans_fond = tk.Frame(self, bg = vert_claire)
        self.frame_his_trans_fond.grid()

        self.frame_his_trans_heading = tk.Frame(self.frame_his_trans_fond, bg = vert_claire)
        self.frame_his_trans_heading.grid(row = 1, sticky = "nw")   

        self.frame_his_trans_table = tk.Frame(self.frame_his_trans_fond, bg = orange, borderwidth = 2)
        self.frame_his_trans_table.grid(row = 2, pady = 20, padx = 35)
        
        self.frame_his_trans_buttons = tk.Frame(self.frame_his_trans_fond, bg = vert_claire)
        self.frame_his_trans_buttons.grid(row = 3, sticky = "we")
        
        self.label = tk.Label(self.frame_his_trans_heading, text = "Liste de toutes les transactions", bg = vert_claire, fg = vert_foncé, font = ("Oswald", 30))
        self.label.pack()
        
        table_trans = ttk.Treeview(self.frame_his_trans_table, columns = (1, 2, 3, 4, 5), show = 'headings', height = 30)
        table_trans.pack(side = LEFT, fill = X)

        table_trans.heading(1, text = "Id")
        table_trans.heading(2, text = "Nom membre")
        table_trans.heading(3, text = "Nom graine")
        table_trans.heading(4, text = "Quantité")
        table_trans.heading(5, text = "Date")

        table_trans.column(1, anchor = CENTER, minwidth = 25, width = 25, stretch = YES) #Id
        table_trans.column(2, minwidth = 100, width = 100, stretch = YES) #Nom membre
        table_trans.column(3, minwidth = 100, width = 100, stretch = YES) #Nom graine
        table_trans.column(4, anchor = CENTER, minwidth = 70, width = 70, stretch = YES) #Quantité
        table_trans.column(5, anchor = CENTER,minwidth = 80, width = 80, stretch = YES) #Date

        sb = tk.Scrollbar(self.frame_his_trans_table, orient = VERTICAL)
        sb.pack(side = RIGHT, fill = Y)

        table_trans.config(yscrollcommand = sb.set)
        sb.config(command = table_trans.yview)
        
        for i in range(len(get_transaction())):
            table_trans.insert(parent = '', index = i, iid = i, values = (get_transaction()[i]))

        self.bouton_ajouter_trans = tk.Button(self.frame_his_trans_buttons, text = "Ajouter\nune transaction\n", font = ("Montserrat", 14), bg = orange, fg = noir, relief = FLAT, command = lambda: self.frame_add_trans_actif())
        self.bouton_ajouter_trans.pack(side = LEFT)

        self.bouton_supr_trans = tk.Button(self.frame_his_trans_buttons, text = "Suprimer\nla transaction\n", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: suppr_trans())
        self.bouton_supr_trans.pack(side = LEFT)

        self.bouton_acceuil = tk.Button(self.frame_his_trans_buttons, text = "Revenir\nau\nmenu", font = ("Montserrat", 14), bg = vert_claire, fg = noir, relief = FLAT, command = lambda: self.frame_acceuil_actif())
        self.bouton_acceuil.pack(side = LEFT)

        def suppr_trans():
            selected = table_trans.focus()
            if not selected:
                messagebox.showerror("Erreur", "Il faut sélectionner une transaction")
            else:
                if messagebox.askokcancel("Confirmation", "Attention, la transaction va etre suprimée"):
                    trans = table_trans.item(selected, 'values')
                    print(trans)
                    del_trans(trans)
                    messagebox.showinfo("Information", "La transaction "+trans[1]+" a était suprimée")
                    self.frame_transhist_actif()

    def frame_transhist_actif(self):
        self.frame_his_trans()
    def frame_transhist_inactif(self):
        self.frame_his_trans_fond.grid_forget()


    #ajoute transaction
    def frame_trans_add(self):

        self.INIT()

        self.frame_princ_trans_add = tk.Frame(self, bg = vert_claire)
        self.frame_princ_trans_add.grid()

        self.frame_trans_add_labelbuton = tk.Frame(self.frame_princ_trans_add, bg = vert_claire)
        self.frame_trans_add_labelbuton.grid(rows = 1, sticky = "we")

        self.frame_trans_add_tabl = tk.Frame(self.frame_princ_trans_add, bg = vert_claire)
        self.frame_trans_add_tabl.grid(rows = 2, sticky = "we")
        
        self.frame_trans_add_tabl_seed = tk.Frame(self.frame_trans_add_tabl, bg = vert_claire)
        self.frame_trans_add_tabl_seed.pack(side = LEFT)

        self.frame_trans_add_tabl_mem = tk.Frame(self.frame_trans_add_tabl, bg = vert_claire)
        self.frame_trans_add_tabl_mem.pack(side = RIGHT)

        self.frame_trans_add_choix = tk.Frame(self.frame_princ_trans_add, bg = vert_claire)
        self.frame_trans_add_choix.grid(rows = 3, sticky = "we")

        self.frame_trans_add_choix_dr = tk.Frame(self.frame_trans_add_choix, bg = vert_claire)
        self.frame_trans_add_choix_dr.grid(rows = 1, column = 0, sticky = "w")

        self.frame_trans_add_choix_date = tk.Frame(self.frame_trans_add_choix_dr, bg = vert_claire)
        self.frame_trans_add_choix_date.grid(rows = 2,column = 4, sticky = "e")

        self.frame_trans_add_butons = tk.Frame(self.frame_princ_trans_add, bg = vert_claire)
        self.frame_trans_add_butons.grid(rows = 4, sticky = "we")

        self.label_add = tk.Label(self.frame_trans_add_labelbuton, text = "Ajouter une transaction", bg = vert_claire, fg = vert_foncé, font = ("Oswald", 30))
        self.label_add.pack(side = LEFT, anchor = "w")
        
        self.bouton_trans_add_retour = tk.Button(self.frame_trans_add_labelbuton, text = "Retour", font = ("Montserrat", 14), bg = orange_claire, fg = noir, relief = FLAT, command = lambda: retour())
        self.bouton_trans_add_retour.pack(side = RIGHT, anchor = "e")
        
        def retour():
            self.frame_transhist_actif()
                
        table_seeds = ttk.Treeview(self.frame_trans_add_tabl_seed, columns = (1, 2, 3, 4, 5, 6, 7, 8, 9), show = 'headings', height = 15)
        table_seeds.pack(side = LEFT)

        table_seeds.heading(1, text = "Id")
        table_seeds.heading(2, text = "Nom")
        table_seeds.heading(3, text = "Couleur")
        table_seeds.heading(4, text = "Qté")
        table_seeds.heading(5, text = "Catégorie")
        table_seeds.heading(6, text = "Descendance")
        table_seeds.heading(7, text = "Année de récolte")
        table_seeds.heading(8, text = "Mois de plantation")
        table_seeds.heading(9, text = "Observation")

        table_seeds.column(1, anchor = CENTER, minwidth = 25, width = 25, stretch = YES) #Id
        table_seeds.column(2, minwidth = 75, width = 75, stretch = YES) #Nom
        table_seeds.column(3, minwidth = 75, width = 75, stretch = YES) #Couleur
        table_seeds.column(4, anchor = CENTER, minwidth = 30, width = 30, stretch = YES) #Quantité
        table_seeds.column(5, minwidth = 60, width = 60, stretch = YES) #Catégorie
        table_seeds.column(6, anchor = CENTER, minwidth = 40, width = 40, stretch = YES) #Descendance
        table_seeds.column(7, anchor = CENTER, minwidth = 50, width = 50, stretch = YES) #Année de récolte
        table_seeds.column(8, anchor = CENTER, minwidth = 50, width = 50, stretch = YES) #mois de plantation        
        table_seeds.column(9, minwidth = 80, width = 80, stretch = NO) #Observation

        sb = tk.Scrollbar(self.frame_trans_add_tabl_seed, orient = VERTICAL)
        sb.pack(side = RIGHT, fill = Y)

        table_seeds.config(yscrollcommand = sb.set)
        sb.config(command = table_seeds.yview)
        
        for i in range(len(get_seeds_values())):
            table_seeds.insert(parent = '', index = i, iid = i, values = (get_seeds_values()[i]))

        table_mem = ttk.Treeview(self.frame_trans_add_tabl_mem, columns = (1, 2, 3, 4, 5, 6, 7, 8), show = 'headings', height = 15)
        table_mem.pack(side = LEFT, fill = X)

        table_mem.heading(1, text = "Id")
        table_mem.heading(2, text = "Nom")
        table_mem.heading(3, text = "Prénom")
        table_mem.heading(4, text = "Telephone")
        table_mem.heading(5, text = "Email")
        table_mem.heading(6, text = "Ville")
        table_mem.heading(7, text = "Don")
        table_mem.heading(8, text = "Rec")

        table_mem.column(1, anchor = CENTER, minwidth = 25, width = 25, stretch = YES) #Id
        table_mem.column(2, minwidth = 75, width = 75, stretch = YES) #Nom
        table_mem.column(3, minwidth = 70, width = 70, stretch = YES) #Prénom
        table_mem.column(4, anchor = CENTER, minwidth = 70, width = 70, stretch = YES) #Telephone
        table_mem.column(5, minwidth = 80, width = 80, stretch = YES) #Email
        table_mem.column(6, minwidth = 60, width = 60, stretch = YES) #Ville
        table_mem.column(7, anchor = CENTER, minwidth = 40, width = 70, stretch = YES) #Donation
        table_mem.column(8, anchor = CENTER, minwidth = 40, width = 40, stretch = YES) #Reception        

        sb = tk.Scrollbar(self.frame_trans_add_tabl_mem, orient = VERTICAL)
        sb.pack(side = RIGHT, fill = Y)

        table_mem.config(yscrollcommand = sb.set)
        sb.config(command = table_mem.yview)
        
        for i in range(len(get_member())):
            table_mem.insert(parent = '', index = i, iid = i, values = (get_member()[i]))
        
        self.bouton_trans_add_don = tk.Button(self.frame_trans_add_choix_dr, text = "Donation", font = ("Montserrat", 18), bg = orange_claire, fg = noir, command = lambda: donclick())
        self.bouton_trans_add_don.grid(row = 0, column = 0, pady = 10, padx = 20, sticky = "w")

        self.bouton_trans_add_rec = tk.Button(self.frame_trans_add_choix_dr, text = "Réception", font = ("Montserrat", 18), bg = orange, fg = noir, command = lambda: recclick())
        self.bouton_trans_add_rec.grid(row = 2, column = 0)

        def donplusun():
            val = self.bouton_trans_add_don_entry.get()
            #print(val)
            self.bouton_trans_add_don_entry.delete(0, tk.END)
            self.bouton_trans_add_don_entry.insert(0, int(val) + 1)
            if int(val) < 0:
                self.bouton_trans_add_don_entry.delete(0, tk.END)
                self.bouton_trans_add_don_entry.insert(0, 0)
        def donmoinsun():
            val = self.bouton_trans_add_don_entry.get()
            #print(val)
            if int(val) > 0:
                self.bouton_trans_add_don_entry.delete(0, tk.END)
                self.bouton_trans_add_don_entry.insert(0, int(val) - 1)
            elif int(val) < 0:
                self.bouton_trans_add_don_entry.delete(0, tk.END)
                self.bouton_trans_add_don_entry.insert(0, 0)

        def donclick():
            self.bouton_trans_add_don.config(bg = orange_claire)
            self.bouton_trans_add_rec.config(bg = orange)
            #print("don")
            self.bouton_trans_add_don_g.grid(row = 1, column = 1)
            self.bouton_trans_add_don_entry.grid(row = 1, column = 2)
            self.bouton_trans_add_don_d.grid(row = 1, column = 3)
            self.bouton_trans_add_rec_g.grid_forget()
            self.bouton_trans_add_rec_entry.grid_forget()
            self.bouton_trans_add_rec_d.grid_forget()
            self.bouton_trans_add_don_entry.delete(0, tk.END)
            self.bouton_trans_add_don_entry.insert(0, 0)
        
        self.bouton_trans_add_don_g = tk.Button(self.frame_trans_add_choix_dr, text = "⇦", font = ("Montserrat", 30), bg = vert_claire, fg = noir, relief = FLAT, width = 1, command = lambda: donmoinsun()) 
        self.bouton_trans_add_don_g.grid(row = 1, column = 1)

        self.bouton_trans_add_don_entry = tk.Entry(self.frame_trans_add_choix_dr, font = 30)
        self.bouton_trans_add_don_entry.grid(row = 1, column = 2)
        self.bouton_trans_add_don_entry.insert(0, 0) 

        self.bouton_trans_add_don_d = tk.Button(self.frame_trans_add_choix_dr, text = "⇨", font = ("Montserrat", 30), bg = vert_claire, fg = noir, width =1,  relief = FLAT, command = lambda: donplusun()) 
        self.bouton_trans_add_don_d.grid(row = 1, column = 3)
        
        def recplusun():
            val = self.bouton_trans_add_rec_entry.get()
            #print(val)
            self.bouton_trans_add_rec_entry.delete(0, tk.END)
            self.bouton_trans_add_rec_entry.insert(0, int(val) + 1)
            if int(val) < 0:
                self.bouton_trans_add_rec_entry.delete(0, tk.END)
                self.bouton_trans_add_rec_entry.insert(0, 0)
        def recmoinsun():
            val = self.bouton_trans_add_rec_entry.get()
            #print(val)
            if int(val) > 0:
                self.bouton_trans_add_rec_entry.delete(0, tk.END)
                self.bouton_trans_add_rec_entry.insert(0, int(val) - 1)
            elif int(val) < 0:
                self.bouton_trans_add_rec_entry.delete(0, tk.END)
                self.bouton_trans_add_rec_entry.insert(0, 0)

        def recclick():
            self.bouton_trans_add_don.config(bg = orange)
            self.bouton_trans_add_rec.config(bg = orange_claire)
            #print("rec")
            self.bouton_trans_add_rec_g.grid(row = 1, column = 1)
            self.bouton_trans_add_rec_entry.grid(row = 1, column = 2)
            self.bouton_trans_add_rec_d.grid(row = 1, column = 3)
            self.bouton_trans_add_don_g.grid_forget()
            self.bouton_trans_add_don_entry.grid_forget()
            self.bouton_trans_add_don_d.grid_forget()
            self.bouton_trans_add_rec_entry.delete(0, tk.END)
            self.bouton_trans_add_rec_entry.insert(0, 0)

        self.bouton_trans_add_rec_g = tk.Button(self.frame_trans_add_choix_dr, text = "⇦", font = ("Montserrat", 30), bg = vert_claire, fg = noir, relief = FLAT, width = 1, command = lambda: recmoinsun()) 
        self.bouton_trans_add_rec_g.grid(row = 1, column = 1)

        self.bouton_trans_add_rec_entry = tk.Entry(self.frame_trans_add_choix_dr, font = 30)
        self.bouton_trans_add_rec_entry.grid(row = 1, column = 2)
        self.bouton_trans_add_rec_entry.insert(0, 0) 

        self.bouton_trans_add_rec_d = tk.Button(self.frame_trans_add_choix_dr, text = "⇨", font = ("Montserrat", 30), bg = vert_claire, fg = noir, width =1,  relief = FLAT, command = lambda: recplusun()) 
        self.bouton_trans_add_rec_d.grid(row = 1, column = 3)

        self.bouton_trans_add_rec_g.grid_forget()
        self.bouton_trans_add_rec_entry.grid_forget()
        self.bouton_trans_add_rec_d.grid_forget()

        labdate = ttk.Label(self.frame_trans_add_choix_date, text = "Choix d'une date", background = vert_claire, font = ("Montserrat", 20))
        labdate.pack(padx = 40, pady = 10)
        cal = DateEntry(self.frame_trans_add_choix_date, width = 20, background = orange, font = ("Montserrat", 15), borderwidth = 2)
        cal.pack(padx = 40, pady = 10)
        
        self.bouton_trans_add_save = tk.Button(self.frame_trans_add_butons, text = "Sauvegarder la\nnouvelle transaction", font = ("Montserrat", 14), bg = orange, fg = noir, relief = FLAT, command = lambda: save_trans()) 
        self.bouton_trans_add_save.pack()       

        def save_trans():
            select_seed = table_seeds.focus()
            select_mem = table_mem.focus()
            don = int(self.bouton_trans_add_don_entry.get())
            rec = int(self.bouton_trans_add_rec_entry.get())
            #print(don, rec)
            qte = don
            
            if not select_seed:
                messagebox.showerror("Erreur", "Il faut sélectionner une graine")
            else: 
                seed = table_seeds.item(select_seed, 'values')
                #print(seed)
                if not select_mem:
                    messagebox.showerror("Erreur", "Il faut sélectionner un membre")
                else: 
                    mem = table_mem.item(select_mem, 'values')
                    #print(mem)
                    if don and rec == 0:
                        messagebox.showerror("Erreur", "Il faut une valeur de don ou de reception positive")
                    else:
                        if don == 0:
                            qte = -rec 
                        add_transaction( None, mem[0], seed[0], cal.get_date(), int(qte))
                        messagebox.showinfo("Transaction", "La transaction a était enregistrée.")
               
    def frame_add_trans_actif(self):
        self.frame_trans_add()
    def frame_add_trans_inactif(self):
        self.frame_princ_trans_add.grid_forget()


    #Menu déroulant
    def Menubar(self):
        
        menuBar = tk.Menu(self)
        
        menuFile = tk.Menu(menuBar, tearoff=0)
        menuFile.add_command(label = "Acceuil", command = lambda: self.frame_acceuil_actif())
        menuFile.add_command(label = "Graines", command = lambda: self.frame_graineshist_actif())
        menuFile.add_command(label = "Membres", command = lambda: self.frame_membrehist_actif())
        menuFile.add_command(label = "Transactions", command = lambda: self.frame_transhist_actif())
        menuFile.add_separator()
        menuFile.add_command(label = "Exit", command = self.quit)
        menuBar.add_cascade( label = "File", menu=menuFile)

        menuEdit = tk.Menu(menuBar, tearoff=0)
        menuEdit.add_command(label ="Undo", command = self.doSomething)
        menuEdit.add_separator()
        menuEdit.add_command(label = "Copy", command = self.doSomething)
        menuEdit.add_command(label = "Cut", command = self.doSomething)
        menuEdit.add_command(label = "Paste", command = self.doSomething)
        menuBar.add_cascade( label = "Edit", menu = menuEdit)

        menuHelp = tk.Menu(menuBar, tearoff = 0)
        menuHelp.add_command(label = "About", command = self.doSomething)
        menuBar.add_cascade( label = "Help", menu = menuHelp)
 
        self.config(menu = menuBar)        
        
    def doSomething(self):
        print("Menu clicked")


if __name__ == "__main__":
    app = Interface()
    app.mainloop()