iconPath = './res/'

colDict = {'accentCol': '#0FA7F0',
           'darkAccent': '#006682',
           'midAccent': '#87D3F8',
           'lightAccent': '#DBEDFF',
           'dullAccent': '#B2E1EE',
           'backgroundCol': '#FFFFFF',
           'white': '#FFFFFF',
           'lightBackground': '#C0C0C0',
           'midBackground': '#808080',
           'darkBackground': '#404040',
           'black': '#000000'}

# STYLE APPLICATION
def setStyleSheet(QObject, styleFilePath):
    """ Set style sheet and replace certain fields"""
    myFile = open(styleFilePath, mode='r')
    styleData = myFile.read()
    for color in colDict:
        styleData = styleData.replace(color, colDict[color])
    QObject.setStyleSheet(styleData)
    myFile.close()
