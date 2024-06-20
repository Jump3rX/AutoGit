import pyfiglet, subprocess,os
intro = pyfiglet.figlet_format("AutoGit")
print(intro)
print("Automate your github commits")

active = True
while active:
    choice = int(input("\nSelect action:\n1:Commit files\n2:Exit\n>>"))
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

            res = subprocess.run(['git','push','-u','origin','main'])
            print(res.stdout)

        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
        except FileNotFoundError as e:
            print(f"Directory not found: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        continue
    elif choice == 2:
        print("Goodbye!")
        break