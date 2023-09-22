def register():
    

    def record():
        x = input("Is Customer Record on file? ")
        if x == "no" or x == "NO" or x == "No":
            f=open("nameaddress_database.csv","a")
            fname = input("What is the first name? ")
            lname = input("What is the last name? ")
            address = input("What is the address? ")
            phone = input("What is the phone number? ")
            post = str(input("What is the post code? "))

            f.write("--------------------------------------")
            f.write("\n")
            f.write("First Name:")
            f.write("\n")
            f.write(fname)
            f.write("\n")
            f.write("\n")

            f.write("last Name:")
            f.write("\n")
            f.write(lname)
            f.write("\n")
            f.write("\n")

            f.write("Address:")
            f.write("\n")
            f.write(address)
            f.write("\n")
            f.write("\n")
                   
            f.write("Phone Number:")
            f.write("\n")
            f.write(phone)
            f.write("\n")
            f.write("\n")

            f.write("Postcode:")
            f.write("\n")
            f.write(post)
            f.write("\n")

            f.close
        if x == "yes" or x == "Yes" or x == "YES":
            g=open("phoneandpost_database.txt","a")

            g.write("--------------------------------------")
            g.write("\n")
            g.write("Phone Number:")
            g.write("\n")
            g.write(phone)
            g.write("\n")
            g.write("\n")

            g.write("Postcode:")
            g.write("\n")
            g.write(post)
            g.write("\n")

            g.close





        if x == "yes" or "Yes" or "YES":
            p = input("What is the phone number? ")
            pc = input("What is the post code? ")




    record()  
    

def create():

    total = 0

    f=open("Pizza_database.txt","a")
        
    piamount = int(input("How many pizza(s)? "))
    while piamount>5:
        print("You cannot order more than 5 pizzas or less than 1 pizza!")
        piamount = int(input("How many pizza(s)? "))
        

    else:
        c = input("What crust would you like, thin, deep pan or stuffed crust: ")
        if c == "thin" or c == "Thin":
            total = total+3

        elif c == "deep pan" or c == "Deep pan" or c == "Deep Pan":
            total = total+4

        elif c == "stuffed crust" or c == "Stufffed crust" or c == "Stuffed Crust":
            total = total+5            

        else:
            c = input("What crust would you like, thin, deep pan or stuffed crust: ")
        
        t = int(input("How many differrent types of toppings would you like? (max 10) "))
        while t>10:
            print("You can only have a max of 10 toppings!")
            t = int(input("How many differrent types of toppings would you like? (max 10) "))
                
        else:
            total = (total+t*1.49)*piamount

            print("Your Total is £"+str(total))
        
                   
                   
create()     
register()                   
    






