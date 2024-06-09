class RemoteTv():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
        self.volume = 0  # Menambah atribut volume dengan nilai awal 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    def volumeUp(self):  # Method untuk menambahkan volume
        if self.volume < 10:
            self.volume += 1

    def volumeDown(self):  # Method untuk menurunkan volume
        if self.volume > 0:
            self.volume -= 1

    # Method tambahan 
    def show(self):
        print('Switch is on ?', self.switchIsOn)
        print('Brightness is:', self.brightness)
        print('Volume is:', self.volume)

# Main code
remoteSatu = RemoteTv()

# Nyalakan saklar, dan naikkan level sebanyak 5 kali
remoteSatu.turnOn()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.show()

# Turunkan level 2 kali, lalu matikan
remoteSatu.lowerLevel()
remoteSatu.lowerLevel()
remoteSatu.turnOff()
remoteSatu.show()

# tingkatkan level volume sebanyak 3
remoteSatu.turnOn()
remoteSatu.volumeUp()
remoteSatu.volumeUp()
remoteSatu.volumeUp()
remoteSatu.show()

# Kurangi level volume sebanyak 2
remoteSatu.volumeDown()
remoteSatu.volumeDown()
remoteSatu.show()
