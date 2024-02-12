import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
FONT = ("Microsoft YaHei",30,"bold")

app=customtkinter.CTk()
app.title('BMI')
app.geometry('500x500')
app.maxsize(width=500,
            height=500)
app.overrideredirect(1)


frame=customtkinter.CTkFrame(master=app,
                             width=490,
                             height=490
                             )

frame.place(relx=0.5,
            rely=0.5,
            anchor=customtkinter.CENTER
            )

bmılabel=customtkinter.CTkLabel(master=frame,
                                text_color="grey",
                                text="BMI",
                                font=FONT,
                                )
bmılabel.place(relx=0.5,
                 rely=0.2,
                 anchor=customtkinter.CENTER
               )

def quit():
    app.quit()

quitbutton=customtkinter.CTkButton(master=frame,
                                   width=30,
                                   height=20,
                                   text="----",
                                   corner_radius=4,
                                   text_color="black",
                                   fg_color="grey",
                                   hover_color="#dbdbdb",
                                   command=quit
                                   )

quitbutton.place(relx=0.94,
                 rely=0.06,
                 anchor=customtkinter.CENTER
                 )

def change_bmi():
    try:
        kilo=int(kilo_entry.get())
        boy=int(boy_entry.get())
        boy = boy/100
        result = kilo/(boy**2)
        result=(int(result))
        if result<18.5:
            MyStringVar.set(value=str(f"Beden Kitle İndeksiniz: {str(result)}"))
            bmi_StringVar.set(value="ZAYIFSINIZ")
        elif result>=18.5 and result<24.9:
            MyStringVar.set(value=str(f"Beden Kitle İndeksiniz: {str(result)}"))
            bmi_StringVar.set(value="NORMALSİNİZ")
        elif result>=25 and result<29.9:
            MyStringVar.set(value=str(f"Beden Kitle İndeksiniz: {str(result)}"))
            bmi_StringVar.set(value="KİLOLUSUNUZ")
        elif result>=30 and result<34.9:
            MyStringVar.set(value=str(f"Beden Kitle İndeksiniz: {str(result)}"))
            bmi_StringVar.set(value="OBEZSİNİZ")
        else:
            MyStringVar.set(value=str(f"Beden Kitle İndeksiniz: {str(result)}"))
            bmi_StringVar.set(value="MORBİD OBEZSİNİZ")

    except:
        MyStringVar.set(value="Lütfen kilo ve/veya boyunuz için sayısal değğer giriniz...")


kilo_label=customtkinter.CTkLabel(master=frame,
                                  text_color="white",
                                  text="_"*(45))
kilo_label.place(relx=0.5,
                 rely=0.43,
                 anchor=customtkinter.CENTER
                 )

kilo_entry=customtkinter.CTkEntry(master=frame,
                                  placeholder_text="Kilonuzu giriniz.",
                                  placeholder_text_color="grey",
                                  border_width=0,
                                  fg_color="#2b2b2b",
                                  width=250
                                  )

kilo_entry.place(relx=0.5,
                 rely=0.40,
                 anchor=customtkinter.CENTER
                 )

boy_label=customtkinter.CTkLabel(master=frame,
                                  text_color="white",
                                  text="_"*(45)
                                 )
boy_label.place(relx=0.5,
                 rely=0.58,
                 anchor=customtkinter.CENTER
                )

boy_entry=customtkinter.CTkEntry(master=frame,
                                  placeholder_text="Boyunuzu giriniz.",
                                  placeholder_text_color="grey",
                                  border_width=0,
                                  fg_color="#2b2b2b",
                                  width=250
                                 )

boy_entry.place(relx=0.5,
                 rely=0.55,
                 anchor=customtkinter.CENTER
                )


controlbutton=customtkinter.CTkButton(master=frame,
                                   width=100,
                                   height=30,
                                   text="Kontrol Et",
                                   corner_radius=4,
                                   text_color="black",
                                   fg_color="grey",
                                   hover_color="#dbdbdb",
                                   command=change_bmi
                                   )

controlbutton.place(relx=0.5,
                    rely=0.7,
                    anchor=customtkinter.CENTER
                    )

MyStringVar=tkinter.StringVar(value="Lütfen istenen değişkenleri giriniz.")

final_label=customtkinter.CTkLabel(master=frame,
                                   textvariable=MyStringVar,
                                   text_color="grey",
                                   fg_color="#2b2b2b",
                                   font=("Microsoft YaHei",15,"normal")
                                   )

final_label.place(relx=0.5,
                  rely=0.84,
                  anchor=customtkinter.CENTER
                  )

bmi_StringVar=tkinter.StringVar(value=" ")

bmi_Result=customtkinter.CTkLabel(master=frame,
                                  textvariable=bmi_StringVar,
                                  text_color="grey",
                                  fg_color="#2b2b2b",
                                  font=("Microsoft YaHei",20,"bold")
                                  )

bmi_Result.place(relx=0.5,
                 rely=0.91,
                 anchor=customtkinter.CENTER
                 )

app.mainloop()
