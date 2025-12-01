class Auth:
    def __init__(self):
        self.filename="users.txt"
        file = open(self.filename,"a")
        file.close()

    def register(self,username,password):
        self.username=username
        self.password=password
        file = open(self.filename,"r")
        users = file.readlines()
        file.close()
        for user in users:
            user = user.split(",")
            if(user[0]==username):
                print("User is already exist")
                return
        file = open(self.filename,"a")
        file.write(f"{username},{password}\n")
        file.close()
        print("register successfull!")

    def login(self,username,password):
        file = open(self.filename,"r")
        users = file.readlines()
        file.close()
        user_found = False
        for user in users:
            user = user.strip().split(",")
            if user[0] == username: 
                user_found = True
                if user[1] == password:
                    print("Login successful!")
                    return True
                else:
                    print("Wrong password!")
                    return False

        if not user_found:
            print("User not found, please register first!")
            return False
        

class product:
    def __init__(self,id,name,price):
        self.id = id
        self.name= name
        self.price = price
class store():
    def __init__(self):
        self.products = [
            product(1,"Laptop",45000), 
            product(2,"Smartphone",15000), 
            product(3,"Headphones",2000), 
            product(4,"Keyboard",1200), 
            product(5,"Mouse",800), 
            product(6,"Charger",500), 
            product(7,"USB Cable",300), 
            product(8,"Backpack",2500)
            ]
        self.cart=[]
    def view_product(self):
        for i in self.products:
            print(f"id = {i.id} name = {i.name} price = {i.price}")
    def add_product(self):
        product_id = int(input("enter the product id: "))
        for product in self.products:
            if product.id == product_id:
                self.cart.append(product)
            
                print(f"{product.name}product added successfully")
                return
        print("Invalid input")
    def view_cart(self):
        if not self.cart:
            print("cart is empty")
        for product in self.cart:
            print(f"{product.name} | {product.id} | {product.price}")
    def remove_cart(self):
        product_id = int(input("Enter the id: "))
        for i in self.cart:
            if product_id == i.id:
                self.cart.remove(i)
                print(f"{i.name} item was remove")
                return
        print("Invalid product id ")
    def checkout(self):
        for i in self.cart:
            print(i.id)
    def user(self):  
        while True:
                print("1) view_product")
                print("2) add_product")
                print("3) view_cart")
                print("4) remove_cart")
                print("5) check out")
                print("6) log out")
                choose_id = int(input("Choose the id: "))
                if choose_id == 1:
                    print("***************view_producty******************")
                    self.view_product()
                elif choose_id == 2:
                    print("***************view_producty******************")
                    self.add_product()   
                elif choose_id == 3:
                    print("***************view_producty******************")
                    self.view_cart()
                elif choose_id == 4:
                    print("***************view_producty******************")
                    self.remove_cart()
                elif choose_id == 5:
                    print("***************view_producty******************")
                    self.checkout()
                elif choose_id == 6:
                    break  
                else:
                    print("Invalid number")

obj = store()
auth = Auth()

while True:
    print("1) register ")
    print("2) login")
    print("3) logout")
    chooes_option = int(input("choose the option: "))
    if chooes_option == 1:
        username = (input("enter the name: "))
        password = (input("Enter the password: "))
        auth.register(username,password)
    elif chooes_option == 2:
        username = input("enter the name: ")
        password = input("Enter the password: ")
        if auth.login(username,password):
            obj.user()
        else:
            print("Access denied please login")

    elif chooes_option == 3:
        break
    else :
        print(" please enter valid number")


