import pyfiglet, subprocess,os
intro = pyfiglet.figlet_format("AutoGit")
print(intro)
print("Automate your github commits")

active = True
while active:
    choice = int(input("\nSelect action:\n1:Commit files\n2.Clone Repository\n3.Commit to new branch\n0:Exit\n>>"))
    if choice == 1:
        repo_url = input("Enter repo url:\t")
        path_to_file =input("Enter path to file e.g c:\\users\\user\\folder:\t") 
        print("Your repository: ",repo_url)
        print("Your file path: ",path_to_file)
        commit_message ="By AutoGit"
        os.chdir(path_to_file)

        try:
            res1 = subprocess.run(['git','init'])
            print(res1.stdout)

            res2 = subprocess.run(['git','add','.'])
            print(res2.stdout)

            res3 = subprocess.run(['git','commit','-m',commit_message])
            print(res3.stdout)

            res4 = subprocess.run(['git','branch','-M','main'])
            print(res4.stdout)

            res5 = subprocess.run(['git','remote','add','origin',repo_url])
            print(res5.stdout)

            res6 = subprocess.run(['git','push','-u','origin','main'])
            print(res6.stdout)

        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
        except FileNotFoundError as e:
            print(f"Directory not found: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        continue
    elif choice == 2:
        save_path = input("Enter the path to save the files eg c:\\users\\user\\folder: ")
        clone_url = input("Enter the repo url to clone: ")
        os.chdir(save_path)
        res7 = subprocess.run(['git','clone',clone_url])
        print(res7.stdout)
        continue
    elif choice == 3:
        project_path = input("Enter the path to existing project eg c:\\users\\user\\folder: ")
        branch_name = input("Enter new branch name: ")
        os.chdir(project_path)

        new_message = "new branch, by AutoGit"
        
        res8 = subprocess.run(['git','branch',branch_name])
        print(res8.stdout)

        res9 = subprocess.run(['git','checkout',branch_name])
        print(res9.stdout)

        res10 = subprocess.run(['git','add','.'])
        print(res10.stdout)

        res11 = subprocess.run(['git','commit','-m',new_message])
        print(res11.stdout)

        res12 = subprocess.run(['git','push','-u', 'origin',branch_name])
        print(res12.stdout)

    elif choice == 0:
        print("Goodbye!")
        break