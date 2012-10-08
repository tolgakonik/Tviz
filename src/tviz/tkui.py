import logging

from tkinter import *
from tviz.tvizdriver import TvizDriver


class MainUI:
    TVIZ_MODE_OFF = TvizDriver.TVIZ_MODE_OFF
    TVIZ_MODE_MESSAGE = TvizDriver.TVIZ_MODE_MESSAGE
    TVIZ_MODE_TANDA = TvizDriver.TVIZ_MODE_TANDA


    def __init__(self):
        self.top = top = Tk()
        self.tviz = TvizDriver(widget=self)

        # Mode        
        modef = Frame(top)
        self.tviz_mode = IntVar()
        modef.pack()
        
#        r = Radiobutton(modef, 
#                        text="message", 
#                        variable=self.tviz_mode, 
#                        value=self.tviz.TVIZ_MODE_MESSAGE,
#                        command = self.enter_message_mode)
#        
#        r.pack(anchor=W, side=RIGHT)
#        
#        r = Radiobutton(modef, 
#                        text="tanda", 
#                        variable=self.tviz_mode, 
#                        value=self.tviz.TVIZ_MODE_TANDA,
#                        command = self.enter_tanda_mode)
#        
#        r.pack(anchor=W, side=RIGHT)
#
#        r = Radiobutton(modef, 
#                        text="off", 
#                        variable=self.tviz_mode, 
#                        value=self.tviz.TVIZ_MODE_OFF,
#                        command = self.enter_off_mode)
#        
#        r.pack(anchor=W, side=RIGHT)

        # self.tviz_mode = Checkbutton(messagef, text="Message Mode Active", variable = self.is_message_mode, command = self.toggle_message_mode)

        row1 = Frame()
        row1.pack()
        
        self.showtanda = Button(row1, text="Show Tanda", command=self.run)
        self.showtanda.pack(side=LEFT)

        # message
        messagef = Frame()
        messagef.pack()

        self.message_send = Button(messagef, text="Display Message", command=self.send_message)
        self.message_send.pack(side=LEFT)

        # message text
        self.message_txt = Entry(messagef)
        self.message_txt.pack(side=LEFT)
        

#         x = Button(top, text="Show Playing Now", command=self.enter_tanda_mode)
#        x.pack(side=LEFT)

        
        # control buttons
        # control = Frame(self.top)
        # control.pack()



        # x = Button(self.top, text="Turn off Updates", command=self.enter_off_mode)
        # x.pack()
       

        adminf = Frame(self.top)
        adminf.pack()

        self.quitbutton = Button(adminf, text="Configure...", command=self.configure)
        self.quitbutton.pack(side=LEFT)

        self.quitbutton = Button(adminf, text="Quit", command=self.quit)
        self.quitbutton.pack(side=LEFT)
        
        self.top.mainloop()

    def run(self):
        self.set_mode(self.TVIZ_MODE_TANDA)
        self.run_loop()

    def run_loop(self):
        if self.tviz_mode == self.TVIZ_MODE_TANDA:
            logging.info("Starting Tviz from tkui") 
            self.tviz.run_one()
            self.top.after(3000, self.run)
        
        #TODO : add n sec repeat here.
        
        

    def quit(self):
        logging.info("Quiting Tviz from Tkui")
        quit()
  
    def send_message(self):
        self.enter_message_mode()
        message = self.message_txt.get()
        # print "xxx Received message: " + message
        self.tviz.setMessage(message)
        self.tviz.run_one()
        
    def toggle_message_mode(self):
    
        if self.is_message_mode.get() == 1:
          logging.info("Message mode is on")
        else:
          logging.info("Message mode is off")

    def configure(self):
        logging.info("Will Enter into Config mode")

    def enter_message_mode(self):
        self.set_mode(self.TVIZ_MODE_MESSAGE)      


    def enter_off_mode(self):
        self.set_mode(self.TVIZ_MODE_OFF)

        
    def set_mode(self, mode):
        logging.debug("Setting mode: " + str(mode))
        self.tviz.setMode(mode)
        self.tviz_mode = mode


if __name__ == '__main__':
    ui = MainUI()
