
#**************************Multiple inheritance***********************

class Animal:
    def eat(self):
        print("Animal eats")
class Walker:
    def walks(self):
        print("walks")
class Dog(Animal,Walker):    #inherited 
    def bark(self):
        print("Bark")
# dog=Dog()
# dog.bark()
# dog.eat()
# dog.walks()

            #output

            # Bark
            # Animal eats
            # walks


#**********************************************************************************
class Cameea:
    def take_photo(self):
        print("capturing photos")
class Call:
    def make_call(self):
        print("calling friends")
class Smart_phone(Cameea,Call):
    def internet(self):
        print("Browsing internet")
# smart_phone=Smart_phone()
# smart_phone.take_photo()
# smart_phone.make_call()
# smart_phone.internet()


                                #output


                                # capturing photos
                                # calling friends
                                # Browsing internet



#********************************Task********************************

class MediaPlayer:
    def play_video(self):
        print("Playing video")
class InternetDevice:
    def connect_wifi(self):
        print("Connected to WiFi")
class SmartTV(MediaPlayer,InternetDevice):
    def change_channel(self):
        print("Changing TV channel")
# smarttv=SmartTV()
# smarttv.play_video()
# smarttv.connect_wifi()
# smarttv.change_channel()


                            #output


                            # Playing video
                            # Connected to WiFi
                            # Changing TV channel