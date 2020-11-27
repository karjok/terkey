import os
from time import sleep
from threading import Thread as td


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

class Terkey:
  def __init__(self):
    pass
  
  # Banner
  def banner(self):
      os.system('clear')
      print(f'{c}Terkey {a}[{c}Termux Key{a}]'.center(68))
      print(f'{a}Karjok Pangesty'.center(53))
      print("".join([i for i in "\n"*3]))
      
  # Loading animation   
  def animate(self,params):
    self.banner()
    print(f"{c}Setting up your keys..")
    t = td(target=self.setup,args=(params,))
    t.start()
    while t.is_alive():
          for i in "-\|/-\|/":
              print(f'\r{c}Please wait {a}{i} ',end="",flush=True)
              sleep(0.1)
    print(f"\nDONE !\n\n{c}Please run again this tool and select {a}About{c} menu\nfor more informatons\nThanks !")
              
  # Of course, like it name, paginate !
  def paginate(self,data,n):
    n_data = round(len(data)/n) + 1
    new_data_part = []
    batas = 0
    for i in range(n_data):
      new_data = []
      for x in range(batas,n+batas):
        try:
          new_data.append(data[x])
        except:
          pass
        batas += 1
      if new_data: new_data_part.append(new_data)
    return new_data_part
    
  # setting up the selected keys
  def setup(self,keys):
      keys = f"extra-keys = {keys}"
      try:
          os.mkdir('/data/data/com.termux/files/home/.termux')
      except:
          pass
      open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(keys)
      os.system('termux-reload-settings')
      
  # If you choose default keys, this function will be executed.
  def standar(self):
    key = "[['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    return key
  
  def about(self):
    self.banner()
    print(f"""
    {a}W E L C O M E  !{c}
    
    This is Terkey, yeah, Termux Key !
    A program from {a}Karjok Pangesty{c} for you.
    This tool is only for Termux app and absolutely FREE !
    
    You can find all default keys in this program at
    {a}https://wiki.termux.com/wiki/Touch_Keyboard{c}
    
    Want to chat with me ?
    {a}https://t.me/om_karjok{c}
    My Web Site
    {a}https://www.karjokpangesty.com{c}
    And if you want to give me some money, you can visit
    {a}https://trakteer.id/karjok-pangesty{c}
    
    """
    )
  # And if you select custom keys,
  def custom(self):
    index = 1
    lastindex = 0
    keys = ["CTRL","ALT","FN","SPACE","ESC","TAB","HOME","END","PGUP","PGDN","INS","DEL","BKSP","UP","LEFT","RIGHT","DOWN","ENTER","BACKSLASH","QUOTE","APOSTROPHE","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","KEYBOARD","DRAWER"]
    print(f"{a} --+ {c}Default Key Lists {a}+--".center(62))
    print()
    for i in self.paginate([*enumerate(keys)],4):
      for x in i:
        en = " " * (15 - len(". ".join([str(x[0]+1),x[1]])))
        print(f"{a}{x[0]+1}.{c} {x[1]}",end=en)
      print()
    print(f"{c}\nInput your selected key number \nand sparate it by comma (,) {a}ex: 1,2,3,4{c}\nOr you can add your own custom key \nlike {a}1,2,3,(,),*,<,>{c} etc.")
    
    selected_keys = []
    user_select = input(f"\n{a}Input {c}: ")
    ranges = [str(i+1) for i in range(len(keys))]
    for i in user_select.split(","):
      if i.isdigit() and i in ranges:
        selected_keys.append(keys[int(i)-1])
      else:
        selected_keys.append(i)
    return selected_keys
    
  # Main
  def start(self):
    self.banner()
    print(f"    {a}[ {c}MENU {a}]")
    print(f"""
  {a}1.{c} Use Default Keys
  {a}2.{c} Custom Keys
  {a}3.{c} About
    """
    )
    menu = input(f"  {c}>{a} ")
    if menu == "1":
      self.banner()
      key = self.standar()
      self.animate(key)
    elif menu == "2":
      self.banner()
      key = self.custom()
      keys = self.paginate(key,7)
      print(f"{c}\nSelected keys: {a}{','.join(key)}{c}\nAre you sure ?")
      try:
        input(f"{c}Press enter to continue or CTRL + C to cancel ")
        self.animate(keys)
      #self.finish()
      except:
        exit(f"{b}Canceled!{c}")
    elif menu == "3":
      self.about()
    else:
      pass
    #print(c+'Silahkan hubungi '+a+'https://t.me/om_karjok'+c+' jika ada yang mau di bicarakan terkait tool ini, bisnis atau sekedar bertanya kabar. :v\nTerimakasih ^_^')
if __name__=='__main__':
  terkey = Terkey()
  terkey.start()
# ini cuma shortcut buat bantu para nub
# karjok pangesty
