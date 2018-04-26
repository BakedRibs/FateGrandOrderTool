

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
        self.appendDatas('1', '玛修·基列莱特', 'Mash Kyrielite', [[5, 22], [5, 24], [5, 29], [5, 31], [5, 25], [5, 34], [5, 33], [5, 42], [1, 0]])
        self.appendDatas('2', '阿尔托莉雅·潘德拉贡', 'Altria Pendragon', [[5, 1], [12, 1], [5, 8], [12, 8, 15, 22], [5, 15, 29, 22], [12, 15, 12, 24], [24, 24, 4, 40], [11, 40, 10, 42], [1, 0]])
        self.appendDatas('3', '阿尔托莉雅·潘德拉贡(Alter)', 'Altria Pendragon(Alter)', [[4, 1], [10, 1], [4, 8], [10, 8, 3, 40], [4, 15, 5, 40], [10, 15, 10, 24], [20, 24, 10, 25], [30, 25, 8, 41], [1, 0]])
        self.appendDatas('4', '阿尔托莉雅·潘德拉贡(Lily)', 'Altria Pendragon(Lily)', [[4, 1], [10, 1], [4, 8], [10, 8, 10, 24], [4, 15, 20, 24], [10, 15, 12, 22], [24, 22, 3, 40], [9, 40, 8, 42], [1, 0]])
        self.appendDatas('5', '尼禄·克劳狄乌斯', 'Nero Claudius', [[4, 1], [10, 1], [4, 8], [10, 8, 4, 33], [4, 15, 7, 33], [10, 15, 4, 31], [8, 31, 12, 24], [36, 24, 20, 34], [1, 0]])
        self.appendDatas('6', '齐格弗里德', 'Siegfried', [[4, 1], [10, 1], [4, 8], [10, 8, 5, 29], [4, 15, 10, 29], [10, 15, 10, 24], [20, 24, 2, 41], [6, 41, 8, 42], [1, 0]])
        self.appendDatas('7', '盖乌斯·尤里乌斯·凯撒', 'Gaius Julius Caesar', [[4, 1], [8, 1], [4, 8], [8, 8, 4, 34], [4, 15, 7, 34], [8, 15, 10, 22], [20, 22, 4, 37], [12, 37, 10, 40], [1, 0]])
        self.appendDatas('8', '阿提拉', 'Artila', [[5, 1], [12, 1], [5, 8], [12, 8, 3, 40], [5, 15, 6, 40], [12, 15, 10, 25], [20, 25, 18, 23], [54, 23, 10, 41], [1, 0]])
        self.appendDatas('9', '吉尔·德·雷', 'Gilles de Rais', [[4, 1], [8, 1], [4, 8], [8, 8, 7, 25], [4, 15, 13, 25], [8, 15, 10, 22], [20, 22, 4, 30], [12, 30, 7, 41], [1, 0]])
        self.appendDatas('10', '骑士迪昂', 'Chevalier D\'Eon', [[4, 1], [10, 1], [4, 8], [10, 8, 5, 29], [4, 15, 10, 29], [10, 15, 12, 22], [24, 22, 5, 35], [15, 35, 16, 32], [1, 0]])
        self.appendDatas('11', '卫宫', 'Emiya', [[4, 2], [10, 2], [4, 9], [10, 9, 4, 34], [4, 16, 8, 34], [10, 16, 12, 22], [24, 22, 4, 33], [12, 33, 40, 25], [1, 0]])
        self.appendDatas('12', '吉尔伽美什', 'Gilgamesh', [[5, 2], [12, 2], [5, 9], [12, 9, 15, 22], [5, 16, 29, 22], [12, 16, 4, 32], [8, 32, 12, 25], [36, 25, 10, 41], [1, 0]])
        self.appendDatas('13', '罗宾汉', 'Robin Hood', [[4, 2], [8, 2], [4, 9], [8, 9, 3, 32], [4, 16, 6, 32], [8, 16, 4, 29], [8, 29, 4, 33], [10, 33, 32, 25], [1, 0]])
        self.appendDatas('14', '阿塔兰忒', 'Atalanta', [[4, 2], [10, 2], [4, 9], [10, 9, 10, 24], [4, 16, 20, 24], [10, 16, 4, 33], [7, 33, 10, 25], [30, 25, 24, 29], [1, 0]])
        self.appendDatas('15', '尤瑞艾莉', 'Euryale', [[4, 2], [8, 2], [4, 9], [8, 9, 2, 42], [4, 16, 3, 42], [8, 16, 3, 32], [6, 32, 3, 40], [8, 40, 7, 41], [1, 0]])
        self.appendDatas('16', '阿拉什', 'Arash', [[2, 2], [4, 2], [2, 9], [4, 9, 5, 22], [2, 16, 10, 22], [4, 16, 2, 29], [4, 29, 2, 36], [6, 36, 16, 25], [1, 0]])
        self.appendDatas('17', '库·丘林', 'Cu Chulainn', [[4, 3], [8, 3], [4, 10], [8, 10, 4, 29], [4, 17, 8, 29], [8, 17, 2, 40], [4, 40, 12, 22], [36, 22, 13, 33], [1, 0]])
        self.appendDatas('18', '伊丽莎白·巴陶里', 'Erzsebet Bathory', [[4, 3], [10, 3], [4, 10], [10, 10, 2, 42], [4, 17, 4, 42], [10, 17, 10, 24], [20, 24, 5, 35], [15, 35, 16, 33], [1, 0]])
        self.appendDatas('19', '武藏坊弁庆', 'Musashibou Benkei', [[3, 3], [6, 3], [3, 10], [6, 10, 3, 29], [3, 17, 6, 29], [6, 17, 8, 23], [15, 23, 6, 25], [42, 25], [1, 0]])
        self.appendDatas('20', '库·丘林(Prototype)', 'Cu Chulainn(Prototype)', [[4, 3], [8, 3], [4, 10], [8, 10, 4, 29], [4, 17, 8, 29], [8, 17, 7, 25], [13, 25, 12, 22], [36, 22, 16, 31], [1, 0]])
        self.appendDatas('21', '列奥尼达斯一世', 'Leonidas I', [[3, 3], [6, 3], [3, 10], [6, 10, 5, 25], [3, 17, 10, 25], [6, 17, 2, 40], [3, 40, 3, 32], [8, 32, 36, 23], [1, 0]])
        self.appendDatas('22', '罗穆路斯', 'Romulus', [[4, 3], [8, 3], [4, 10], [8, 10, 3, 33], [4, 17, 6, 33], [8, 17, 4, 31], [7, 31, 4, 34], [12, 34, 32, 25], [1, 0]])
        self.appendDatas('23', '美杜莎', 'Medusa', [[4, 4], [8, 4], [4, 11], [8, 11, 7, 25], [4, 18, 13, 25], [8, 18, 3, 32], [6, 32, 2, 41], [5, 41, 13, 33], [1, 0]])
        self.appendDatas('24', '圣乔治', 'Georgius', [[3, 4], [6, 4], [3, 11], [6, 11, 2, 33], [3, 18, 4, 33], [6, 18, 8, 22], [15, 22, 3, 34], [9, 34, 12, 37], [1, 0]])
        self.appendDatas('25', '爱德华·蒂奇', 'Edward Teach', [[3, 4], [6, 4], [3, 11], [6, 11, 3, 31], [3, 18, 5, 31], [6, 18, 8, 23], [15, 23, 3, 36], [9, 36, 12, 30], [1, 0]])
        self.appendDatas('26', '布狄卡', 'Boudica', [[4, 4], [8, 4], [4, 11], [8, 11, 10, 23], [4, 18, 20, 23], [8, 18, 3, 33], [6, 33, 4, 32], [10, 32, 32, 25], [1, 0]])
        self.appendDatas('27', '牛若丸', 'Ushiwakamaru', [[4, 4], [8, 4], [4, 11], [8, 11, 4, 37], [4, 18, 7, 37], [8, 18, 10, 22], [20, 22, 4, 34], [12, 34, 16, 31], [1, 0]])
        self.appendDatas('28', '亚历山大', 'Alexander', [[4, 4], [8, 4], [4, 11], [8, 11, 4, 31], [4, 18, 7, 31], [8, 18, 4, 37], [7, 37, 3, 40], [8, 40, 48, 22], [1, 0]])
        self.appendDatas('29', '玛丽·安托瓦内特', 'Marie Antoinette', [[4, 4], [10, 4], [4, 11], [10, 11, 4, 32], [4, 18, 7, 32], [10, 18, 4, 33], [7, 33, 2, 41], [6, 41, 20, 34], [1, 0]])
        self.appendDatas('30', '玛尔达', 'Marthe', [[4, 4], [10, 4], [4, 11], [10, 11, 5, 29], [4, 18, 10, 29], [10, 18, 10, 24], [20, 24, 4, 33], [12, 33, 8, 42], [1, 0]])
        self.appendDatas('31', '美狄亚', 'Medea', [[4, 5], [8, 5], [4, 12], [8, 12, 7, 25], [4, 19, 13, 25], [8, 19, 8, 24], [16, 24, 4, 30], [12, 30, 16, 35], [1, 0]])
        self.appendDatas('32', '吉尔·德·雷', 'Gilles de Rais', [[4, 5], [8, 5], [4, 12], [8, 12, 4, 36], [4, 19, 7, 36], [8, 19, 4, 30], [7, 30, 8, 25], [24, 25, 7, 41], [1, 0]])
        self.appendDatas('', '', '', [[], [], [], [], [], [], [], [], [1, 0]])
        self.appendDatas('', '', '', [[], [], [], [], [], [], [], [], [1, 0]])
        self.appendDatas('', '', '', [[], [], [], [], [], [], [], [], [1, 0]])
        self.appendDatas('', '', '', [[], [], [], [], [], [], [], [], [1, 0]])
