

class ServantData():
    def __init__(self):
        self.Init_UI()
        
    def Init_UI(self):
        self.servantNameEnglish = {}
        self.servantNameChinese = {}
        self.servantSkillData = {}
        
        self.servantInitiate()
        
    def appendDatas(self, indexStr, ChineseName, EnglishName, SkillData):
        self.servantNameChinese[indexStr] = ChineseName
        self.servantNameEnglish[indexStr] = EnglishName
        self.servantSkillData[indexStr] = SkillData
        
    def servantInitiate(self):
        self.appendDatas('1', '玛修·基列莱特', 'Mash Kyrielite', [[5, 22, 5], [5, 24, 10], [5, 29, 30], [5, 31, 40], [5, 25, 100], [5, 34, 125], [5, 33, 250], [5, 42, 300], [1, 0, 500]])
        self.appendDatas('2', '阿尔托莉雅·潘德拉贡', 'Altria Pendragon', [[5, 1, 20], [12, 1, 40], [5, 8, 120], [12, 8, 15, 22, 160], [5, 15, 29, 22, 400], [12, 15, 12, 24, 500], [24, 24, 4, 40, 1000], [11, 40, 10, 42, 1200], [1, 0, 2000]])
        self.appendDatas('3', '阿尔托莉雅·潘德拉贡(Alter)', 'Altria Pendragon(Alter)', [[4, 1, 10], [10, 1, 20], [4, 8, 60], [10, 8, 3, 40, 80], [4, 15, 5, 40, 200], [10, 15, 10, 24, 250], [20, 24, 10, 25, 500], [30, 25, 8, 41, 600], [1, 0, 1000]])
        self.appendDatas('4', '阿尔托莉雅·潘德拉贡(Lily)', 'Altria Pendragon(Lily)', [[4, 1, 10], [10, 1, 20], [4, 8, 60], [10, 8, 10, 24, 80], [4, 15, 20, 24, 200], [10, 15, 12, 22, 250], [24, 22, 3, 40, 500], [9, 40, 8, 42, 600], [1, 0, 1000]])
        self.appendDatas('5', '尼禄·克劳狄乌斯', 'Nero Claudius', [[4, 1, 10], [10, 1, 20], [4, 8, 60], [10, 8, 4, 33, 80], [4, 15, 7, 33, 200], [10, 15, 4, 31, 250], [8, 31, 12, 24, 500], [36, 24, 20, 34, 600], [1, 0, 1000]])
        self.appendDatas('6', '齐格弗里德', 'Siegfried', [[4, 1, 10], [10, 1, 20], [4, 8, 60], [10, 8, 5, 29, 80], [4, 15, 10, 29, 200], [10, 15, 10, 24, 250], [20, 24, 2, 41, 500], [6, 41, 8, 42, 600], [1, 0, 1000]])
        self.appendDatas('7', '盖乌斯·尤里乌斯·凯撒', 'Gaius Julius Caesar', [[4, 1, 5], [8, 1, 10], [4, 8, 30], [8, 8, 4, 34, 40], [4, 15, 7, 34, 100], [8, 15, 10, 22, 125], [20, 22, 4, 37, 250], [12, 37, 10, 40, 300], [1, 0, 500]])
        self.appendDatas('8', '阿提拉', 'Artila', [[5, 1, 20], [12, 1, 40], [5, 8, 120], [12, 8, 3, 40, 160], [5, 15, 6, 40, 400], [12, 15, 10, 25, 500], [20, 25, 18, 23, 1000], [54, 23, 10, 41, 1200], [1, 0, 2000]])
        self.appendDatas('9', '吉尔·德·雷', 'Gilles de Rais', [[4, 1, 5], [8, 1, 10], [4, 8, 30], [8, 8, 7, 25, 40], [4, 15, 13, 25, 100], [8, 15, 10, 22, 125], [20, 22, 4, 30, 250], [12, 30, 7, 41, 300], [1, 0, 500]])
        self.appendDatas('', '', '', [[], [], [], [], [], [], [], [], [1, 0]])
        self.appendDatas('', '', '', [[], [], [], [], [], [], [], [], [1, 0]])
