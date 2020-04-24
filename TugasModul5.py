class userService:
  def checkEmail (self) :
    for x in self.data :
      if self.email == self.data[x]["email"] :
        return 1
    return 0

  def checkPassword (self) :
    for x in self.data :
      if self.password == self.data[x]["password"] :
        return 1
      return 0

  def login (self) :
    if self.checkEmail() == 1 and self.checkPassword() == 1 :
      print("\nWelcome " + self.data[self.email]["role"])
      print("Logged it as user email: " + self.email + "\n")
      self.showHistory()
    else : print("Invalid Login")

  def showHistory(self) : 
    print(self.email + " Meminjam Buku:")
    for x in self.history[self.email]["pinjam_buku"] :
      print(x)
    print("\n" + self.history[self.email]["tgl_pinjam"] + "\n")

  def __init__ (self,email,password) :
    self.email = email
    self.password = password
    self.data = {
      "Adlikelompok13@gmail.com" : {
        "email" : "Adlikelompok13@gmail.com",
        "password" : "12345",
        "role" : "superadmin"
      },

      "Zorenskelompok13@gmail.com" : {
        "email" : "Zorenskelompok13@gmail.com",
        "password" : "12345",
        "role" : "user"
      },
    }
    self.history = {
      "Adlikelompok13@gmail.com" : {
        "pinjam_buku" : {"Fisika" , "Matematika"},
        "tgl_pinjam" : "24-04-2020"
      },
      
      "Zorenskelompok13@gmail.com" : {
        "pinjam_buku" : {"Kalkulus","Elektronika"},
        "tgl_pinjam" : "24-04-2020"
      },
    }

def main():
  isExit = 'y'
  while isExit == 'y' :
    email = input("E-mail: ")
    password = input("Password: ")

    user = userService(email,password)
    user.login()
    isExit = input("Kembali? (y/t) ")

main()
 