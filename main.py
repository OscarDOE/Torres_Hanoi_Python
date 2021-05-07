from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter 
from tkinter import ttk
from tkinter import messagebox
import time

class Aplicacion:

    def __init__(self):
        self.pila1 = []
        self.pila2 = []
        self.pila3 = []
        self.p1 = {}
        self.raiz = tkinter.Tk()
        self.raiz.geometry('725x500')
        self.raiz.resizable(width=True,height=True)
        self.raiz.title('Torres de Hanoi')
        #nb = ttk.Notebook(raiz,width=625)
        #nb.pack(fill=BOTH, expand=TRUE)
        #tinfo = Entry(self.raiz, width=50,font=("Calibri 20"))

        #p1 = ttk.Frame(nb)
        #nb.add(p1,text='Cargar Archivos')
        self.F1 = tkinter.Canvas(self.raiz,bg='light blue')
        self.F1.place(height=520,width=745)

        #F2 = tkinter.Canvas(raiz,bg='red')
        #F2.place(x=0,y=70,height=400,width=210)

        #F3 = tkinter.Canvas(raiz,bg='yellow')
        #F3.place(x=210,y=70,height=400,width=210)

        #F4 = tkinter.Canvas(raiz,bg='violet')
        #F4.place(x=420,y=70,height=400,width=210)

        #F1.place(x=50,y=0)
        #F1.place(x=0, y = 0)
        #Button(F1,text = "Cargaddr",  bg = 'green', padx=20).place(x=300)
        self.c1 = ttk.Combobox(self.F1,state= "readonly")
        self.c1.place(x=15,y=40 )
        self.c1["values"] = ["3","4","5","6"]
        self.c1.current(0)
        self.b1F1 = tkinter.Label(self.F1, text= "Seleccionar Número de Discos", bg= "light green", width=25)
        self.b1F1.place(x=5,y=10)
        self.b2F1 = tkinter.Button(self.F1, text= "Jugar", bg= "light green",width=20,command=self.escogistediscos)
        self.b2F1.place(x=200,y=10)
        self.b3F1 = tkinter.Button(self.F1, text= "Reiniciar", bg= "light green",width=20,command=self.Cancelar)
        self.b3F1.place(x=500,y=10)

        self.texto = " SOLUCIÓN \n"
        self.pasosautomatico = []
        #self.pasosautomatico.append(["10","15"])
        self.contadormovs = 0
        self.place1 = [10, 420, 200, 450]
        self.place2 = [25, 390, 185, 420]
        self.place3 = [40, 360, 170, 390]
        self.place4 = [55, 330, 155, 360]
        self.place5 = [70, 300, 140, 330]
        self.place6 = [85, 270, 125, 300]
        self.disco_seleccionado = 0
        self.xantes = 0
        self.yantes = 0
        self.banderamovil = False
        

        self.raiz.mainloop()

    def solucion(self):
        #botonsolucion = tkinter.Button(self.F1, text= "SOLUCION", bg= "light blue",width=20,command=self.hanoi(self.disco_seleccionado,"1","3","2"))
        self.botonsolucion = tkinter.Button(self.F1, text= "SOLUCION", bg= "light blue",width=20,command=self.solutipo2)
        self.botonsolucion.place(x=200,y=50)
        print("SOLUCIONES               SOLUCION")
    # DEF REALIZARSOLU YA NO SE UTILIZÖ 
    #
    #
    #
    #
    def realizarsolu(self):
        texto1 = ""

        self.hanoi(self.disco_seleccionado,"1","3","2")
        print("SE IMPRIMIRA TODA ESTA MADRE")
        print(self.texto)
        ventana = tkinter.Tk()
        ventana.title('Solucion de '+str(self.disco_seleccionado)+' discos')
        #ventana.geometry('400x250')
        #ventana.resizable(width=True,height=True)
        scrollbar = tkinter.Scrollbar(ventana)
        c = tkinter.Canvas(ventana,background='pink',yscrollcommand=scrollbar.set)
        #ventanaF1.place(height=520,width=745)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        elframe = tkinter.Frame(c)
        c.pack(side="left",fill="both",expand=True)
        c.create_window(0,0,window=elframe,anchor='nw')


        texto = tkinter.Label(elframe, wraplength=250,text= self.texto, bg= "light green")
        #ventanalabel.place(x=5,y=10)
        texto.pack()
        ventana.update()
        c.config(scrollregion=c.bbox("all"))
        #ventana.mainloop()
        self.texto = ""

    def solutipo2(self):

        print("SOLCUOION TIPO 2")
        self.hanoi(self.disco_seleccionado, "1", "3", "2")
        print("IMPRIMIENDO PASSOS AUTOMATICO")
        self.despueshanoi()



    def hanoi(self,n, pivote1,pivote3,pivote2):
        if n == 1:
            #print(pivote1+" -> "+pivote3)
            self.texto += pivote1+" -> "+pivote3+"\n"
            self.pasosautomatico.append([pivote1,pivote3])
        else:
            self.contadormovs += 1
            self.hanoi(n-1, pivote1, pivote2, pivote3)
            #print(pivote1 +" -> "+pivote3)
            #self.texto +=  pivote1 +" -> "+pivote3+"\n"
            self.pasosautomatico.append([pivote1,pivote3])
            self.hanoi(n-1, pivote2, pivote3, pivote1)
    
    def despueshanoi(self):
        #texto = int(self.labelmovimientos['text'])
        #texto += 1
        #self.labelmovimientos['text'] = texto
        self.botonsolucion.destroy()
        self.recorrer(0)
        #self.F1.after(800,self.despuesdespueshanoi)
        
    
    def despuesdespueshanoi(self):
        for i in self.pasosautomatico:
            self.Cancelar2()
            print(i)
            if i[0] == "1":
                self.Cancelar2()
                tam = len(self.pila1)
                aux = self.pila1[tam-1]
                if i[1] == "2":
                    self.Cancelar2()
                    tam2 = len(self.pila2)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila2[tam2-1]
                    if aux2 is None:
                        self.pila1.pop()
                        self.pila2.append(aux)
                    else:
                        self.pila1.pop()
                        self.pila2.append(aux)
                elif i[1] == "3":
                    self.Cancelar2()
                    tam2 = len(self.pila3)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila3[tam2-1]
                    if aux2 is None:
                        self.pila1.pop()
                        self.pila3.append(aux)
                    else:
                        self.pila1.pop()
                        self.pila3.append(aux)
                self.Cancelar2()
                    
            elif i[0] == "2":
                self.Cancelar2()
                tam = len(self.pila2)
                aux = self.pila2[tam-1]
                if i[1] == "1":
                    self.Cancelar2()
                    tam2 = len(self.pila1)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila1[tam2-1]
                    if aux2 is None:
                        self.pila2.pop()
                        self.pila1.append(aux)
                    else:
                        self.pila2.pop()
                        self.pila1.append(aux)
                elif i[1] == "3":
                    self.Cancelar2()
                    tam2 = len(self.pila3)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila3[tam2-1]
                    if aux2 is None:
                        self.pila2.pop()
                        self.pila3.append(aux)
                    else:
                        self.pila2.pop()
                        self.pila3.append(aux)
                self.Cancelar2()
                
            elif i[0] == "3":
                self.Cancelar2()
                tam = len(self.pila3)
                aux = self.pila3[tam-1]
                if i[1] == "1":
                    tam2 = len(self.pila1)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila1[tam2-1]
                    if aux2 is None:
                        self.pila3.pop()
                        self.pila1.append(aux)
                    else:
                        self.pila3.pop()
                        self.pila1.append(aux)
                elif i[1] == "2":
                    self.Cancelar2()
                    tam2 = len(self.pila2)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila2[tam2-1]
                    if aux2 is None:
                        self.pila3.pop()
                        self.pila2.append(aux)
                    else:
                        self.pila3.pop()
                        self.pila2.append(aux)
            
            print("PILA 1: ",self.pila1)
            print("PILA 2: ",self.pila2)
            print("PILA 3: ",self.pila3)
            #texto = int(self.labelmovimientos['text'])
            #texto += 1
            #self.labelmovimientos['text'] = texto
            #time.sleep(1)
        self.pasosautomatico = []
        self.F1.after(800,self.despuesdespueshanoi)
    
    def recorrer(self,cont):
        if cont == 0:
            
            pass
        elif cont-1 < len(self.pasosautomatico):
            if self.pasosautomatico[cont-1][0] == "1" and self.pasosautomatico[cont-1][1] == "2":
                tam = len(self.pila1)
                aux = self.pila1[tam-1]
                self.pila1.pop()
                self.pila2.append(aux)
            elif self.pasosautomatico[cont-1][0] == "1" and self.pasosautomatico[cont-1][1] == "3":
                tam = len(self.pila1)
                aux = self.pila1[tam-1]
                self.pila1.pop()
                self.pila3.append(aux)
            elif self.pasosautomatico[cont-1][0] == "2" and self.pasosautomatico[cont-1][1] == "1":
                tam = len(self.pila2)
                aux = self.pila2[tam-1]
                self.pila2.pop()
                self.pila1.append(aux)
            elif self.pasosautomatico[cont-1][0] == "2" and self.pasosautomatico[cont-1][1] == "3":
                tam = len(self.pila2)
                aux = self.pila2[tam-1]
                self.pila2.pop()
                self.pila3.append(aux)
            elif self.pasosautomatico[cont-1][0] == "3" and self.pasosautomatico[cont-1][1] == "1":
                tam = len(self.pila3)
                aux = self.pila3[tam-1]
                self.pila3.pop()
                self.pila1.append(aux) 
            elif self.pasosautomatico[cont-1][0] == "3" and self.pasosautomatico[cont-1][1] == "2":
                tam = len(self.pila3)
                aux = self.pila3[tam-1]
                self.pila3.pop()
                self.pila2.append(aux)
            texto = int(self.labelmovimientos['text'])
            texto += 1
            #print("SE AUMENTO EN 1 EL MOVIMIENTO")
            self.labelmovimientos['text'] = texto
                
        print("LLEGO A ESTE PUNTO?????")
        cont += 1
        #self.F1.after(800,self.Cancelar2)
        if len(self.pila3) == self.disco_seleccionado:
            self.pasosautomatico = []
            self.texto = ""
        else:
            self.F1.after(800,self.recorrer,cont)
            
        self.Cancelar2()
        


    
    def hanoi3(self,n, pivote1,pivote3,pivote2):
        if n >= 1:
            self.hanoi(n-1, pivote1, pivote2, pivote3)
            #print(pivote1 +" -> "+pivote3)
            self.pasosautomatico.append([pivote1,pivote3])
            #self.texto +=  pivote1 +" -> "+pivote3+"\n"
            self.hanoi(n-1, pivote2, pivote3, pivote1)

    
    
    def hanoi2(self,n, pivote1,pivote3,pivote2):
        if n == 1:
            print(pivote1+" -> "+pivote3)
            if pivote1 == "1":
                tam = len(self.pila1)
                aux = self.pila1[tam-1]
                if pivote3 == "2":
                    tam2 = len(self.pila2)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila2[tam2-1]
                    if aux2 is None:
                        self.pila1.pop()
                        self.pila2.append(aux)
                    else:
                        self.pila1.pop()
                        self.pila2.append(aux)
                elif pivote3 == "3":
                    tam2 = len(self.pila3)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila3[tam2-1]
                    if aux2 is None:
                        self.pila1.pop()
                        self.pila3.append(aux)
                    else:
                        self.pila1.pop()
                        self.pila3.append(aux)
                self.Cancelar2()
                    
            elif pivote1 == "2":
                tam = len(self.pila2)
                aux = self.pila2[tam-1]
                if pivote3 == "1":
                    tam2 = len(self.pila1)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila1[tam2-1]
                    if aux2 is None:
                        self.pila2.pop()
                        self.pila1.append(aux)
                    else:
                        self.pila2.pop()
                        self.pila1.append(aux)
                elif pivote3 == "3":
                    tam2 = len(self.pila3)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila3[tam2-1]
                    if aux2 is None:
                        self.pila2.pop()
                        self.pila3.append(aux)
                    else:
                        self.pila2.pop()
                        self.pila3.append(aux)
                self.Cancelar2()
                
            elif pivote1 == "3":
                tam = len(self.pila3)
                aux = self.pila3[tam-1]
                if pivote3 == "1":
                    tam2 = len(self.pila1)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila1[tam2-1]
                    if aux2 is None:
                        self.pila3.pop()
                        self.pila1.append(aux)
                    else:
                        self.pila3.pop()
                        self.pila1.append(aux)
                elif pivote3 == "2":
                    tam2 = len(self.pila2)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila2[tam2-1]
                    if aux2 is None:
                        self.pila3.pop()
                        self.pila2.append(aux)
                    else:
                        self.pila3.pop()
                        self.pila2.append(aux)
                self.Cancelar2()
            #time.sleep(1)
            texto = int(self.labelmovimientos['text'])
            texto += 1
            self.labelmovimientos['text'] = texto

    
    def Cancelar(self):
        self.F1 = tkinter.Canvas(self.raiz,bg='light blue')
        self.F1.place(height=520,width=745)
        self.c1 = ttk.Combobox(self.F1,state= "readonly")
        self.c1.place(x=15,y=40)
        self.c1["values"] = ["3","4","5","6"]
        self.c1.current(0)
        self.b1F1 = tkinter.Label(self.F1, text= "Seleccionar Número de Discos", bg= "light green", width=25)
        self.b1F1.place(x=5,y=10)
        self.b2F1 = tkinter.Button(self.F1, text= "Jugar", bg= "light green",width=20,command=self.escogistediscos)
        self.b2F1.place(x=200,y=10)
        self.b3F1 = tkinter.Button(self.F1, text= "Reiniciar", bg= "light green",width=20,command=self.Cancelar)
        self.pila1 = []
        self.pila2 = []
        self.pila3 = []
        self.b3F1.place(x=500,y=10)
    
    def Cancelar2(self):
        #print("CANCELAR 2")
        #print("******************************************************************")
        
        self.F1 = tkinter.Canvas(self.raiz,bg='light blue')
        self.F1.place(height=520,width=745)
        self.c1 = ttk.Combobox(self.F1,state= "readonly")
        self.c1.place(x=15,y=40)
        self.c1["values"] = ["3","4","5","6"]
        self.c1.current(0)
        self.b1F1 = tkinter.Label(self.F1, text= "Seleccionar Número de Discos", bg= "light green", width=25)
        self.b1F1.place(x=5,y=10)
        self.b2F1 = tkinter.Button(self.F1, text= "Jugar", bg= "light green",width=20,command=self.escogistediscos)
        self.b2F1.place(x=200,y=10)
        self.b3F1 = tkinter.Button(self.F1, text= "Reiniciar", bg= "light green",width=20,command=self.Cancelar)
        self.b3F1.place(x=500,y=10)
        self.F1.create_line(105,150,105,450,width="25", fill="blue")
        self.F1.create_line(350,150,350,450,width="25", fill="blue")
        self.F1.create_line(595,150,595,450,width="25", fill="blue")
        self.labelsinimportancia = tkinter.Label(self.F1,text= "Movimientos Realizados",bg="light blue")
        self.labelsinimportancia.place(x=35,y=480)
        self.labelsinimportancia = tkinter.Label(self.F1,text= "Movimientos Mínimos",bg="light blue")
        self.labelsinimportancia.place(x=400,y=480)
        self.labelmovimientosmin = tkinter.Label(self.F1,text= ((2**self.disco_seleccionado)-1),bg="light blue")
        self.labelmovimientosmin.place(x=580,y=480)
        self.labelmovimientos = tkinter.Label(self.F1,text= self.labelmovimientos['text'],bg="light blue")
        self.labelmovimientos.place(x=210,y=480)
        t1 = len(self.pila1)
        t2 = len(self.pila2)
        t3 = len(self.pila3)
        #print(t1,t2,t3)
        x = 0
        x1 = 10
        y1 = 420
        x2 = 200
        y2 = 450
        while x < t1:
            xdisco = self.pila1[x][1] - self.pila1[x][3]
            ydisco = self.pila1[x][2] - self.pila1[x][4]
            if x == (t1-1):

            
                r = self.F1.create_rectangle(105-(xdisco/2),y1-(x*30),105+(xdisco/2),y2-(x*30),fill="orange",tags="movil")
            else:
                    r = self.F1.create_rectangle(105-(xdisco/2),y1-(x*30),105+(xdisco/2),y2-(x*30),fill="orange",tags="inmovil")
            #r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),xdisco,y2-(x*30),fill="orange",tags="movil")
            #r = self.F1.create_rectangle(self.pila1[x][1],y1-(x*30),self.pila1[x][3],y2-(x*30),fill="orange",tags="movil")
            #r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="movil")
            x += 1
        #for i in self.pila1:

            #print("I :",i)
            #print("I :",i[0])
            #print("I :",i[1])
            #print("I :",i[2])
            #print("I :",i[3])
            #print("I :",i[4])
         #   r = self.F1.create_rectangle(i[1],i[2],i[3],i[4],fill="orange",tags="movil")

            
            #print(i)
        
        x = 0
        x1 = 210
        y1 = 420
        x2 = 400
        y2 = 450
        while x < t2:
            xdisco = self.pila2[x][1] - self.pila2[x][3]
            ydisco = self.pila2[x][2] - self.pila2[x][4]
            if x == (t2-1):

            
                r = self.F1.create_rectangle(350-(xdisco/2),y1-(x*30),350+(xdisco/2),y2-(x*30),fill="orange",tags="movil")
            else:
                r = self.F1.create_rectangle(350-(xdisco/2),y1-(x*30),350+(xdisco/2),y2-(x*30),fill="orange",tags="inmovil")
            #r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),xdisco,y2-(x*30),fill="orange",tags="movil")
            #r = self.F1.create_rectangle(self.pila2[x][1],y1-(x*30),self.pila2[x][3],y2-(x*30),fill="orange",tags="movil")
            #r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="movil")
            x += 1
        #for i in self.pila2:
          #  r = self.F1.create_rectangle(i[1],i[2],i[3],i[4],fill="orange",tags="movil")
            #print(i)

        
        x = 0
        x1 = 500
        y1 = 420
        x2 = 690
        y2 = 450
        while x < t3:
            xdisco = self.pila3[x][1] - self.pila3[x][3]
            ydisco = self.pila3[x][2] - self.pila3[x][4]

            if x == (t3-1):
                r = self.F1.create_rectangle(595-(xdisco/2),y1-(x*30),595+(xdisco/2),y2-(x*30),fill="orange",tags="movil")
            else:
                r = self.F1.create_rectangle(595-(xdisco/2),y1-(x*30),595+(xdisco/2),y2-(x*30),fill="orange",tags="inmovil")
            #r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),xdisco,y2-(x*30),fill="orange",tags="movil")
            #r = self.F1.create_rectangle(self.pila3[x][1],y1-(x*30),self.pila3[x][3],y2-(x*30),fill="orange",tags="movil")
            #r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="movil")
            x += 1
        #for i in self.pila3:
         #   r = self.F1.create_rectangle(i[1],i[2],i[3],i[4],fill="orange",tags="movil")
            #print(i)
        self.F1.tag_bind("movil", "<ButtonPress-1>",self.presion_boton)
        self.F1.tag_bind("movil", "<Button1-Motion>",self.mover)
        self.F1.tag_bind("movil", "<ButtonRelease-1>",self.boton_soltar)

        #self.F1.tag_bind("inmovil", "<ButtonPress-1>",self.presion_boton)
        #self.F1.tag_bind("movil", "<Button1-Motion>",self.mover)
        #self.F1.tag_bind("inmovil", "<ButtonRelease-1>",self.boton_soltar)
        if len(self.pila3) == self.disco_seleccionado and self.labelmovimientos['text'] == ((2**self.disco_seleccionado)-1):
            print("************************************************************************")
            print("************************************************************************")
            print("************************************************************************")
            print("         FELICIDADES HAS GANADO EN LOS MOVIMIENTOS MÍNIMOS              ")
            print("************************************************************************")
            print("************************************************************************")
            print("************************************************************************")
            messagebox.showinfo("FELICIDADES","HA COMPLETADO EL JUEGO CON EL MENOR NÚMERO DE MOVIMIENTOS")
            self.Cancelar()
        elif len(self.pila3) == self.disco_seleccionado:
            print("************************************************************************")
            print("************************************************************************")
            print("************************************************************************")
            print("                         FELICIDADES HAS GANADO                         ")
            print("************************************************************************")
            print("************************************************************************")
            print("************************************************************************")
            messagebox.showinfo("FELICIDADES","HA COMPLETADO EL JUEGO \nAún puede lograrlo en el menor número de movimientos. \n   SUERTE")
        #self.hanoi(self.disco_seleccionado, "1", "3", "2")


    def escogistediscos(self):
        global F1
        numdisc = int(self.c1.get())
        self.F1 = tkinter.Canvas(self.raiz,bg='light blue')
        self.F1.place(height=520,width=745)
        self.c1 = ttk.Combobox(self.F1,state= "readonly")
        self.c1.place(x=15,y=40)
        self.c1["values"] = ["3","4","5","6"]
        self.c1.current(numdisc-3)
        self.b1F1 = tkinter.Label(self.F1, text= "Seleccionar Número de Discos", bg= "light green", width=25)
        self.b1F1.place(x=5,y=10)
        self.b2F1 = tkinter.Button(self.F1, text= "Jugar", bg= "light green",width=20,command=self.escogistediscos)
        self.b2F1.place(x=200,y=10)
        self.b3F1 = tkinter.Button(self.F1, text= "Reiniciar", bg= "light green",width=20,command=self.Cancelar)
        self.pila1 = []
        self.pila2 = []
        self.pila3 = []
        self.b3F1.place(x=500,y=10)
        #self.hanoi()
        
        #print("CONCONCONOCNONCON:",self.contadormovs)

        #global c1,F1,F2,F3,F4
        #print((2**numdisc)-1)
        #self.F2 = tkinter.Canvas(self.raiz,bg='red')
        #elf.F2.place(x=0,y=70,height=400,width=210)

        #self.F3 = tkinter.Canvas(self.raiz,bg='yellow')
        #self.F3.place(x=210,y=70,height=400,width=210)

        #self.F4 = tkinter.Canvas(self.raiz,bg='violet')
        #self.F4.place(x=420,y=70,height=400,width=210)

        self.F1.create_line(105,150,105,450,width="25", fill="blue")
        self.F1.create_line(350,150,350,450,width="25", fill="blue")
        self.F1.create_line(595,150,595,450,width="25", fill="blue")

        self.labelsinimportancia = tkinter.Label(self.F1,text= "Movimientos Realizados",bg="light blue")
        self.labelsinimportancia.place(x=35,y=480)
        self.labelsinimportancia = tkinter.Label(self.F1,text= "Movimientos Mínimos",bg="light blue")
        self.labelsinimportancia.place(x=400,y=480)
        self.labelmovimientosmin = tkinter.Label(self.F1,text= ((2**numdisc)-1),bg="light blue")
        self.labelmovimientosmin.place(x=580,y=480)
        self.labelmovimientos = tkinter.Label(self.F1,text= "0",bg="light blue")
        self.labelmovimientos.place(x=210,y=480)
        self.solucion()
        #self.F2.create_line(105,150,105,450,width="25", fill="blue")
        #self.F3.create_line(105,150,105,450,width="25", fill="blue")
        #self.F4.create_line(105,150,105,450,width="25", fill="blue")
        x = 0
        lista1 = []
        lista2 = []
        #print(x)
        lista3 = []
        x1 = 10
        y1 = 420
        x2 = 200
        y2 = 450
        #r =F2.create_rectangle(10,370,200,400,fill="orange",tags="movil")
        if numdisc == 3:
            #print("JKJFKJDLKSJDKFL")

            while x < numdisc:
                #r = F2.create_rectangle(10,370,200,400,fill="orange",tags="movil")
                if x == (numdisc-1):
                    r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="movil")
                    self.pila1.append([x,x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30)])
                    #print("TAGRAISE: ",self.F1.tag_raise("inmovil"))
                else:
                    r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="inmovil")
                    self.pila1.append([x,x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30)])
                    #print("TAGRAISE INMOVILES: ",self.F1.tag_raise("inmovil"))
                    #print(self.F1.type("inmovil"))
                    #print(self.F1.type("inmovil"))
                #self.pila1.append([r,"Numero "+str(x)])
                x += 1
                #print(x)
        elif numdisc == 4:
            while x < numdisc:
                if x == (numdisc-1):
                    r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="movil")
                    self.pila1.append([x,x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30)])
                    #print("TAGRAISE: ",self.F1.tag_raise("inmovil"))
                else:
                    r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="inmovil")
                    self.pila1.append([x,x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30)])
                    #print("TAGRAISE INMOVILES: ",self.F1.tag_raise("inmovil"))
                    #print(self.F1.type("inmovil"))
                    #print(self.F1.type("inmovil"))
                #self.pila1.append([r,"Numero "+str(x)])
                x += 1
                #print(x)
        elif numdisc == 5:
            while x < numdisc:
                if x == (numdisc-1):
                    r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="movil")
                    self.pila1.append([x,x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30)])
                    #print("TAGRAISE: ",self.F1.tag_raise("inmovil"))
                else:
                    r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="inmovil")
                    self.pila1.append([x,x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30)])
                    #print("TAGRAISE INMOVILES: ",self.F1.tag_raise("inmovil"))
                    #print(self.F1.type("inmovil"))
                    #print(self.F1.type("inmovil"))
                #self.pila1.append([r,"Numero "+str(x)])
                x += 1
                #print(x)
        elif numdisc == 6:
            while x < numdisc:
                if x == (numdisc-1):
                    r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="movil")
                    self.pila1.append([x,x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30)])
                    #print("TAGRAISE: ",self.F1.tag_raise("inmovil"))
                else:
                    r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="inmovil")
                    self.pila1.append([x,x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30)])
                    #print("TAGRAISE INMOVILES: ",self.F1.tag_raise("inmovil"))
                    #print(self.F1.type("inmovil"))
                    #print(self.F1.type("inmovil"))
                #self.pila1.append([r,"Numero "+str(x)])
                x += 1
                #print(x)
            '''while x < numdisc:
                if x == (numdisc-1):
                    r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="movil")
                    self.pila1.append([x,x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30)])
                    #print("TAGRAISE: ",self.F1.tag_raise("inmovil"))
                else:
                    r = self.F1.create_rectangle(x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30),fill="orange",tags="inmovil")
                    self.pila1.append([x,x1+(x*15),y1-(x*30),x2-(x*15),y2-(x*30)])
                    #print("TAGRAISE INMOVILES: ",self.F1.tag_raise("inmovil"))
                    #print(self.F1.type("inmovil"))
                    print(self.F1.type("inmovil"))
                #self.pila1.append([r,"Numero "+str(x)])
                x += 1
                print(x)'''
        else:
            l1 = tkinter.Label(self.F1,text= "Son demasiados discos, hay un máximo de 6, y un mínimo de 3")
            l1.pack()
            pass
        self.disco_seleccionado = numdisc
        print("PRIMERO : ",self.pila1)
        #self.pila1.reverse()
        #print("PRIMERO REVERSE : ",self.pila1)
        print("SEGUNDO : ",self.pila2)
        print("TERCERO : ",self.pila3)
        self.F1.tag_bind("movil", "<ButtonPress-1>",self.presion_boton)
        self.F1.tag_bind("movil", "<Button1-Motion>",self.mover)
        self.F1.tag_bind("movil", "<ButtonRelease-1>",self.boton_soltar)

        #self.F1.tag_bind("inmovil", "<ButtonPress-1>",self.presion_boton)
        #self.F1.tag_bind("movil", "<Button1-Motion>",self.mover)
        #self.F1.tag_bind("inmovil", "<ButtonRelease-1>",self.boton_soltar)

        
    def presion_boton(self,evento):
        cuadrado = self.F1.find_withtag(tkinter.CURRENT)
        #self.F1.gettags("movil")
        #print("INTENTADO IMPRIMIR EL TAG",self.F1.gettags("movil"))
        self.cuadrado_seleccionado = (cuadrado,evento.x,evento.y)
        self.xantes = evento.x
        self.yantes = evento.y
        print("XANTES:",self.xantes)
        print("YANTES:",self.yantes)
        #self.F1.addtag("movil")
        #print("Posicion X: ",evento.x)
        #print("Posicion Y: ",evento.y)
        #print("CUADRADO SELECCIONADO: ",self.cuadrado_seleccionado)
        #print("CUADRADO : ",cuadrado)
        #print("PRIMEROXXXX : ",self.pila1[0])
        print("\n\n\n\nPila1:",self.pila1)
        print("\n\n\n\nPila2:",self.pila2)
        print("\n\n\n\nPila3:",self.pila3)
        print("\n\n\n\n")

    def mover(self,evento):
        x,y = evento.x,evento.y
        cuadrado,x1,y1 = self.cuadrado_seleccionado
        self.F1.move(cuadrado,x-x1,y-y1)
        #print("XXXX:",self.F1.move(cuadrado,x-x1,y-y1))
        self.cuadrado_seleccionado = (cuadrado,x,y)

    def boton_soltar(self,evento):
        cuadrado = self.F1.find_withtag(tkinter.CURRENT)
        self.cuadrado_seleccionado = (cuadrado,evento.x,evento.y)
        #print("CUADRADO SELECCIONADO: ",self.cuadrado_seleccionado)
        #print("CUADRADO : ",cuadrado)
        #print("PRUEBA",self.F1)
        #aux = self.pila1[0]
        #self.pila1.pop(0)
        #print("PILA 1 OTRA VEZ", self.pila1)
        x,y = evento.x,evento.y
        print("POSICION X:",evento.x)
        print("POSICION Y:",evento.y)
        z = 280+ 470
        cuadrado,x1,y1 = self.cuadrado_seleccionado
        if evento.x >= 10 and evento.x <= 280 and evento.y >= 170 and evento.y <= 500:
            print("ESTA EN EL RANGO DE 1")
        elif evento.x >= 280 and evento.x <= 470 and evento.y >= 170 and evento.y <= 500:
            print("ESTA EN EL RANGO DE 2")
        elif evento.x >= 470 and evento.x <= 730 and evento.y >= 170 and evento.y <= 500:
            print("ESTA EN EL RANGO DE 3")
        else:
            #self.F1.move(cuadrado, self.xantes,self.yantes)
            print("NO ESTA ENTRE EL RANGO")
        self.cuadrado_seleccionado = (cuadrado,x,y)
        #self.labelmovimientos = tkinter.Label(self.F1,text="carta1") 
        texto = int(self.labelmovimientos['text'])
        antesx = self.xantes
        antesy = self.yantes
        torrecita = 0
        if antesx >= 10 and antesx <= 280 and antesy >= 170 and antesy <= 500:
            #print("ESTA EN EL RANGO DE 1")
            torrecita = 1
        elif antesx >= 280 and antesx <= 470 and antesy >= 170 and antesy <= 500:
            #print("ESTA EN EL RANGO DE 2")
            torrecita = 2
        elif antesx >= 470 and antesx <= 730 and antesy >= 170 and antesy <= 500:
            #print("ESTA EN EL RANGO DE 3")
            torrecita = 3
        else:
            #self.F1.move(cuadrado, self.xantes,self.yantes)
            print("NO ESTA ENTRE EL RANGO")

        if torrecita == 1:
            if evento.x >= 10 and evento.x <= 280:
                pass
            else:
                if evento.x >= 280 and evento.x <= 470:
                    tam = len(self.pila1)
                    aux = self.pila1[tam-1]
                    tam2 = len(self.pila2)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila2[tam2-1]
                    if aux2 is None:
                        self.pila1.pop()
                        self.pila2.append(aux)
                        
                    else:

                        if aux2[1] > aux[1]:
                            print("---------------------------------- ES MENOR ---------------------------------------")
                            texto -= 1
                        else:
                            self.pila1.pop()
                            self.pila2.append(aux)
                elif evento.x >= 470 and evento.x <= 730:
                    tam = len(self.pila1)
                    aux = self.pila1[tam-1]
                    tam2 = len(self.pila3)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila3[tam2-1]
                    if aux2 is None:
                        self.pila1.pop()
                        self.pila3.append(aux)
                        
                    else:

                        if aux2[1] > aux[1]:
                            print("---------------------------------- ES MENOR ---------------------------------------")
                            texto -= 1
                        else:
                            self.pila1.pop()
                            self.pila3.append(aux)
                texto += 1
                
            
        elif torrecita == 2:
            if evento.x >= 280 and evento.x <= 470:
                pass
            else:
                if evento.x >= 10 and evento.x <= 280:
                    tam = len(self.pila2)
                    aux = self.pila2[tam-1]
                    tam2 = len(self.pila1)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila1[tam2-1]
                    if aux2 is None:
                        self.pila2.pop()
                        self.pila1.append(aux)
                        
                    else:

                        if aux2[1] > aux[1]:
                            texto -= 1
                            print("---------------------------------- ES MENOR ---------------------------------------")
                        else:
                            self.pila2.pop()
                            self.pila1.append(aux)
                elif evento.x >= 470 and evento.x <= 730:
                    tam = len(self.pila2)
                    aux = self.pila2[tam-1]
                    tam2 = len(self.pila3)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila3[tam2-1]
                    if aux2 is None:
                        self.pila2.pop()
                        self.pila3.append(aux)
                        
                    else:

                        if aux2[1] > aux[1]:
                            texto -= 1
                            print("---------------------------------- ES MENOR ---------------------------------------")
                        else:
                            self.pila2.pop()
                            self.pila3.append(aux)
                texto += 1
        elif torrecita == 3:
            if evento.x >= 470 and evento.x <= 730:
                pass
            else:
                if evento.x >= 280 and evento.x <= 470:
                    tam = len(self.pila3)
                    aux = self.pila3[tam-1]
                    tam2 = len(self.pila2)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila2[tam2-1]
                    if aux2 is None:
                        self.pila3.pop()
                        self.pila2.append(aux)
                        
                    else:

                        if aux2[1] > aux[1]:
                            texto -= 1
                            print("---------------------------------- ES MENOR ---------------------------------------")
                        else:
                            self.pila3.pop()
                            self.pila2.append(aux)
                elif evento.x >= 100 and evento.x <= 280:
                    tam = len(self.pila3)
                    aux = self.pila3[tam-1]
                    tam2 = len(self.pila1)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila1[tam2-1]
                    if aux2 is None:
                        self.pila3.pop()
                        self.pila1.append(aux)
                        
                    else:

                        if aux2[1] > aux[1]:
                            texto -= 1
                            print("---------------------------------- ES MENOR ---------------------------------------")
                        else:
                            self.pila3.pop()
                            self.pila1.append(aux)
                texto += 1
        else:
            pass
        #print("ESTE ES EL TECTO :",texto)
        self.labelmovimientos['text'] = texto
        self.Cancelar2()
        
        #self.labelmovimientos.place(x=150,y=180)
        

        
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXX: ",evento.x)
        print("YYYYYYYYYYYYYYYYYYYYYYYYYYY: ",evento.y)
        #self.luegoprimermov()
    

    def luegoprimermov(self):
        cantidad1 = len(self.pila1)
        cantidad2 = len(self.pila2)
        cantidad3 = len(self.pila3)
        print(cantidad1)
        print(cantidad2)
        print(cantidad3)
        print(self.pila1)
        print(self.pila2)
        print(self.pila3)

        


'''raiz = tkinter.Tk()
raiz.geometry('625x500')
raiz.resizable(width=True,height=True)
raiz.title('IPC 2 Proyecto 2')
#nb = ttk.Notebook(raiz,width=625)
#nb.pack(fill=BOTH, expand=TRUE)
#tinfo = Entry(self.raiz, width=50,font=("Calibri 20"))

#p1 = ttk.Frame(nb)
#nb.add(p1,text='Cargar Archivos')
F1 = tkinter.Canvas(raiz,bg='light blue')
F1.place(height=900,width=725)

#F2 = tkinter.Canvas(raiz,bg='red')
#F2.place(x=0,y=70,height=400,width=210)

#F3 = tkinter.Canvas(raiz,bg='yellow')
#F3.place(x=210,y=70,height=400,width=210)

#F4 = tkinter.Canvas(raiz,bg='violet')
#F4.place(x=420,y=70,height=400,width=210)

#F1.place(x=50,y=0)
#F1.place(x=0, y = 0)
#Button(F1,text = "Cargaddr",  bg = 'green', padx=20).place(x=300)
c1 = ttk.Combobox(F1,state= "readonly")
c1.place(x=15,y=40 )
c1["values"] = ["3","4","5","6","7"]
c1.current(0)
b1F1 = tkinter.Label(F1, text= "Seleccionar Número de Discos", bg= "light green", width=25)
b1F1.place(x=0,y=10)
b2F1 = tkinter.Button(F1, text= "Jugar", bg= "light green",width=20,command=escogistediscos)
b2F1.place(x=200,y=10)

#F2.create_line(110,150,110,450,width="25", fill="blue")
#F3.create_line(110,150,110,450,width="25", fill="blue")
#F4.create_line(110,150,110,450,width="25", fill="blue")

#r =F2.create_rectangle(10,370,200,400,fill="orange",tags="movil")
#r =F3.create_rectangle(10,370,200,400,fill="orange",tags="movil")
#r =F4.create_rectangle(10,370,200,400,fill="orange",tags="movil")

#line = canvas.create_line(, y0, x1, y1, ..., xn, yn, options)
#b3F1 = tkinter.Button(F1, text= "Operaciones Duales", bg= "light green", width=20)
#b3F1.place(x=245,y=10)
#b4F1 = tkinter.Button(F1, text= "Reportes", bg= "light green", width=14)
#b4F1.place(x=395,y=10)
#b5F1 = tkinter.Button(F1, text= "Ayuda", bg= "light green", width=13)
#b5F1.place(x=503,y=10)

#image2 = Image.open("b123asurero.png")
#photo = ImageTk.PhotoImage(image2)

#b6F1 = tkinter.Button(F1, image=photo, bg= "light green", command=inicio,width=14)
#b6F1.img = photo
#b6F1.place(x=605,y=10)

#label1 = ttk.Label(F1,text="Ruta")
#label1.place(x=2,y=50)
#label1 = ttk.Label(F1,text="No ha ingresado ninguna matriz")
#label1.place(x=50,y=50)

raiz.mainloop()'''
aplicacion = Aplicacion()
'''            

        else:
            self.contadormovs += 1
            self.hanoi2(n-1, pivote1, pivote2, pivote3)
            if pivote1 == "1":
                tam = len(self.pila1)
                aux = self.pila1[tam-1]
                if pivote3 == "2":
                    tam2 = len(self.pila2)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila2[tam2-1]
                    if aux2 is None:
                        self.pila1.pop()
                        self.pila2.append(aux)
                    else:
                        self.pila1.pop()
                        self.pila2.append(aux)
                        
                elif pivote3 == "3":
                    tam2 = len(self.pila3)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila3[tam2-1]
                    if aux2 is None:
                        self.pila1.pop()
                        self.pila3.append(aux)
                    else:
                        self.pila1.pop()
                        self.pila3.append(aux)
                self.Cancelar2()
                    
            elif pivote1 == "2":
                tam = len(self.pila2)
                aux = self.pila2[tam-1]
                if pivote3 == "1":
                    tam2 = len(self.pila1)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila1[tam2-1]
                    if aux2 is None:
                        self.pila2.pop()
                        self.pila1.append(aux)
                    else:
                        self.pila2.pop()
                        self.pila1.append(aux)
                elif pivote3 == "3":
                    tam2 = len(self.pila3)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila3[tam2-1]
                    if aux2 is None:
                        self.pila2.pop()
                        self.pila3.append(aux)
                    else:
                        self.pila2.pop()
                        self.pila3.append(aux)
                self.Cancelar2()
            elif pivote1 == "3":
                tam = len(self.pila3)
                aux = self.pila3[tam-1]
                if pivote3 == "1":
                    tam2 = len(self.pila1)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila1[tam2-1]
                    if aux2 is None:
                        self.pila3.pop()
                        self.pila1.append(aux)
                    else:
                        self.pila3.pop()
                        self.pila1.append(aux)
                elif pivote3 == "2":
                    tam2 = len(self.pila2)
                    aux2 = None
                    if tam2 == 0:
                        pass
                    else:
                        aux2 = self.pila2[tam2-1]
                    if aux2 is None:
                        self.pila3.pop()
                        self.pila2.append(aux)
                    else:
                        self.pila3.pop()
                        self.pila2.append(aux)
                self.Cancelar2()
            self.Cancelar2()
            self.Cancelar2()
            self.Cancelar2()
            self.Cancelar2()
            self.Cancelar2()
            print(pivote1 +" -> "+pivote3)
            texto = int(self.labelmovimientos['text'])
            texto += 1
            self.labelmovimientos['text'] = texto
            time.sleep(1)
            self.Cancelar2()
            self.hanoi2(n-1, pivote2, pivote3, pivote1)'''