import fileProcess as fp


class GarbageSorting(object):
    Bin_Recycle = []
    Bin_Harmful = []
    Bin_Wet = []
    Bin_Dry = []

    File_recycle = []
    File_harmful = []
    File_wet = []
    File_dry = []

    def __init__(self):
        self.Bin_Recycle = []
        self.Bin_Harmful = []
        self.Bin_Wet = []
        self.Bin_Dry = []
        self.loadFile()
        print([{
            'Recycle bin': self.Bin_Recycle,
            'Harmful bin': self.Bin_Harmful,
            'Wet bin': self.Bin_Wet,
            'Dry bin': self.Bin_Dry
        }])

    def loadFile(self):
        self.File_recycle = open('recycleGarbageList.txt', 'r', encoding='UTF-8').read()
        self.File_harmful = open('harmfulGarbageList.txt', 'r', encoding='UTF-8').read()
        self.File_wet = open('wetGarbageList.txt', 'r', encoding='UTF-8').read()
        self.File_dry = open('dryGarbageList.txt', 'r', encoding='UTF-8').read()

        self.File_recycle = fp.modifyFile(self.File_recycle)
        self.File_harmful = fp.modifyFile(self.File_harmful)
        self.File_wet = fp.modifyFile(self.File_wet)
        self.File_dry = fp.modifyFile(self.File_dry)


    def search(self, garbageThrow):
        if garbageThrow in self.File_recycle:
            self.Bin_Recycle.append(garbageThrow)
            return '丢进可回收垃圾桶!'
        elif garbageThrow in self.File_harmful:
            self.Bin_Harmful.append(garbageThrow)
            return '丢进有害垃圾桶!'
        elif garbageThrow in self.File_wet:
            self.Bin_Wet.append(garbageThrow)
            return '丢进湿垃圾桶!'
        elif garbageThrow in self.File_dry:
            self.Bin_Dry.append(garbageThrow)
            return '丢进干垃圾桶!'
        else:
            return '您丢的垃圾"%s"不属于生活垃圾或系统暂未识别!' % garbageThrow

    def showBin(self):
        print([{
            'Recycle bin': self.Bin_Recycle,
            'Harmful bin': self.Bin_Harmful,
            'Wet bin': self.Bin_Wet,
            'Dry bin': self.Bin_Dry
        }])
        self.showFile()
        return [{
            'Recycle bin': self.Bin_Recycle,
            'Harmful bin': self.Bin_Harmful,
            'Wet bin': self.Bin_Wet,
            'Dry bin': self.Bin_Dry
        }]

    def showFile(self):
        print([{
            'Recycle file': self.File_recycle,
            'Harmful file': self.File_harmful,
            'Wet file': self.File_wet,
            'Dry file': self.File_dry
        }])
        # return [{
        #     'Recycle bin': self.File_recycle,
        #     'Harmful bin': self.File_harmful,
        #     'Wet bin': self.File_wet,
        #     'Dry bin': self.File_dry
        # }]

    def clearBin(self):
        self.__init__()
