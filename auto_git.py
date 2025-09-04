import customtkinter,os,subprocess
from PIL import Image
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.title("AutoGit")
app.geometry("720x480")


def commit_files():
    #msg_1.configure(text=f"{path_to_file.get()}\n{repo_url.get()}")
    os.chdir(path_to_file.get())
    try:
        res1 = subprocess.run(['git','init'])
        msg_1.configure(text=f"{res1.stdout}\n")

        res2 = subprocess.run(['git','add','.'])
        msg_1.configure(text=f"{res2.stdout}\n")

        res3 = subprocess.run(['git','commit','-m','By AutoGit'])
        msg_1.configure(text=f"{res3.stdout}\n")

        res4 = subprocess.run(['git','branch','-M','main'])
        msg_1.configure(text=f"{res4.stdout}\n")

        res5 = subprocess.run(['git','remote','add','origin',repo_url.get()])
        msg_1.configure(text=f"{res5.stdout}\n")

        res6 = subprocess.run(['git','push','-u','origin','main'])
        msg_1.configure(text=f"{res6.stdout}\n")

    except subprocess.CalledProcessError as e:
        msg_1.configure(text=f"{e}\n")
    except FileNotFoundError as e:
        msg_1.configure(text=f"{e}\n")
    except Exception as e:
        msg_1.configure(text=f"{e}\n")

def clone_repo():
    #msg_2.configure(text=f"{path_to_save_file.get()}\n{clone_repo_url.get()}")
    try:
        os.chdir(path_to_save_file.get())
        res7 = subprocess.run(['git','clone',clone_repo_url.get()], capture_output=True,text=True,check=True)
        for l1 in res7.stdout:
            msg_2.configure(text=f"{l1}")

        for l2 in res7.stderr:
            msg_2.configure(text=f"{l2}")

    except subprocess.CalledProcessError as e:
        msg_2.configure(text=f"{e}\n")
    except Exception as e:
        msg_2.configure(text=f"{e}\n")
    


def commit_new_branch():
    msg_3.configure(text=f"{path_to_project.get()}\n{branch_name.get()}\n{commit_message.get()}")

    os.chdir(path_to_project.get())    
    res8 = subprocess.run(['git','branch',branch_name.get()])
    msg_3.configure(text=f"{res8.stdout}")
    #print(res8.stdout)

    res9 = subprocess.run(['git','checkout',branch_name.get()])
    msg_3.configure(text=f"{res9.stdout}")
    print(res9.stdout)

    res10 = subprocess.run(['git','add','.'])
    msg_3.configure(text=f"{res10.stdout}")
    #print(res10.stdout)

    res11 = subprocess.run(['git','commit','-m',commit_message.get()])
    msg_3.configure(text=f"{res11.stdout}")
    #print(res11.stdout)

    res12 = subprocess.run(['git','push','-u', 'origin',branch_name.get()])
    msg_3.configure(text=f"{res12.stdout}")
    #print(res12.stdout)




tabs = customtkinter.CTkTabview(app,width=680,height=440,corner_radius=10)
tabs.pack(pady=20,padx=20)


home = tabs.add("Home")
commit = tabs.add("Commit Files")
clone = tabs.add("Clone Repository")
new_branch = tabs.add("Commit New Branch")

#################---Home---##########

app_name = customtkinter.CTkLabel(home,text="AutoGit",font=('arial',24))
app_name.pack()
  
logo = customtkinter.CTkImage(light_image=Image.open('images/logo.png'),
                              dark_image=Image.open('images/logo.png'),
                              size=(280,280))
logo_holder = customtkinter.CTkLabel(home,text="",image=logo)
logo_holder.pack()

welcome_message = customtkinter.CTkLabel(home,text="Automate your github commits",font=('arial',24))
welcome_message.pack()

#################---Commit files Tab---##########
path_to_file = customtkinter.CTkEntry(commit,placeholder_text="Enter path to file e.g c:\\users\\user\\folder",width=300,height=40)
path_to_file.pack(pady=10)

repo_url = customtkinter.CTkEntry(commit,placeholder_text="Enter repo url",width=300,height=40)
repo_url.pack(pady=10)

commit_btn = customtkinter.CTkButton(commit,text="Commit",command=commit_files)
commit_btn.pack()

frame_1 = customtkinter.CTkScrollableFrame(commit,width=400,height=200,label_text="Output",label_fg_color='green',label_text_color='white')
frame_1.pack()

msg_1 = customtkinter.CTkLabel(frame_1,text="",font=('arial',24),text_color="green")
msg_1.pack()



#################---Clone repository tab---##########
path_to_save_file = customtkinter.CTkEntry(clone,placeholder_text="Enter path where to save files e.g c:\\users\\user\\folder",width=400,height=40)
path_to_save_file.pack(pady=10)

clone_repo_url = customtkinter.CTkEntry(clone,placeholder_text="Enter repo url to clone",width=400,height=40)
clone_repo_url.pack(pady=10)

clone_btn = customtkinter.CTkButton(clone,text="Clone",command=clone_repo)
clone_btn.pack()

frame_2 = customtkinter.CTkScrollableFrame(clone,width=400,height=200,label_text="Output",label_fg_color='green',label_text_color='white')
frame_2.pack()

msg_2 = customtkinter.CTkLabel(frame_2,text="",font=('arial',24),text_color="green")
msg_2.pack(pady=20)

####################---New branch tab---###############
path_to_project = customtkinter.CTkEntry(new_branch,placeholder_text="Enter path to existing project e.g c:\\users\\user\\folder",width=400,height=40)
path_to_project.pack(pady=10)

branch_name = customtkinter.CTkEntry(new_branch,placeholder_text="Enter new branch name",width=400,height=40)
branch_name.pack(pady=10)

commit_message = customtkinter.CTkEntry(new_branch,placeholder_text="Enter commit message",width=400,height=40)
commit_message.pack(pady=10)

new_branch_btn = customtkinter.CTkButton(new_branch,text="Create & Commit",command=commit_new_branch)
new_branch_btn.pack()


frame_3 = customtkinter.CTkScrollableFrame(new_branch,width=400,height=200,label_text="Output",label_fg_color='green',label_text_color='white')
frame_3.pack()

msg_3 = customtkinter.CTkLabel(frame_3,text="",font=('arial',24),text_color="green")
msg_3.pack(pady=20)


##End
app.mainloop()