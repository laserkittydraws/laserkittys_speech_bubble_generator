from PyQt5.QtGui import QColor, QFontMetrics, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QCheckBox, QColorDialog, QFontComboBox, QGroupBox, QLabel, QMainWindow, QPushButton, QRadioButton, QSlider, QSpinBox, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt
from krita import *



class BubbleCoordinates():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class LSBGDocker(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("LaserKitty's speech bubble generator")
        mainLayout = QVBoxLayout()

        self.addOnPage = QPushButton("Add on Page")
        mainLayout.addWidget(self.addOnPage)

        previewLabel = QLabel("Preview")
        mainLayout.addWidget(previewLabel)

        self.preview = QSvgWidget(self)
        self.preview.setMinimumHeight(200)
        mainLayout.addWidget(self.preview)



        # MARK: bubble params
        bubbleTypes = QGroupBox()
        bubbleTypes.setTitle("Bubble type")
        bubbleTypesLayout = QHBoxLayout()

        self.roundBubble = QRadioButton(self)
        self.roundBubble.setText("Round")
        self.roundBubble.setChecked(True)
        bubbleTypesLayout.addWidget(self.roundBubble)

        self.squareBubble = QRadioButton(self)
        self.squareBubble.setText("Square")
        bubbleTypesLayout.addWidget(self.squareBubble)

        #MARK: >>TODO<<
        # TODO: Add other bubble types
        
        # self.squircleBubble = QRadioButton(self)
        # self.squircleBubble.setText("Squircle")
        # bubbleTypesLayout.addWidget(self.squircleBubble)

        bubbleTypes.setLayout(bubbleTypesLayout)

        self.bubbleColorButton = QPushButton(self)
        self.bubbleColor = QColor("white")
        bubbleColorImage = QPixmap(32,32)
        bubbleColorImage.fill(self.bubbleColor)
        bubbleColorIcon = QIcon(bubbleColorImage)
        self.bubbleColorButton.setIcon(bubbleColorIcon)
        self.bubbleColorButton.setFixedWidth(self.bubbleColorButton.height())
        bubbleTypesLayout.addWidget(self.bubbleColorButton)

        mainLayout.addWidget(bubbleTypes)



        # MARK:outline params
        outlineSize = QGroupBox("Outline")
        bOutlineThicknessLayout = QHBoxLayout()

        self.bOutlineThicknessSlider = QSlider(self)
        self.bOutlineThicknessSlider.setMinimum(0)
        self.bOutlineThicknessSlider.setMaximum(10)
        self.bOutlineThicknessSlider.setValue(3)
        self.bOutlineThicknessSlider.setOrientation(Qt.Orientation.Horizontal)
        bOutlineThicknessLayout.addWidget(self.bOutlineThicknessSlider)

        self.bOutlineThicknessSpinBox = QSpinBox(self)
        self.bOutlineThicknessSpinBox.setMinimum(0)
        self.bOutlineThicknessSpinBox.setValue(3)
        bOutlineThicknessLayout.addWidget(self.bOutlineThicknessSpinBox)

        self.bOutlineColorButton = QPushButton(self)
        self.outlineColor = QColor("black")
        outlineColorImage = QPixmap(32,32)
        outlineColorImage.fill(self.outlineColor)
        outlineColorIcon = QIcon(outlineColorImage)
        self.bOutlineColorButton.setIcon(outlineColorIcon)
        self.bOutlineColorButton.setFixedWidth(self.bOutlineColorButton.height())
        bOutlineThicknessLayout.addWidget(self.bOutlineColorButton)

        outlineSize.setLayout(bOutlineThicknessLayout)
        mainLayout.addWidget(outlineSize)



        # MARK:text params
        speechGroup = QGroupBox("Speech")
        speechGroupLayout = QVBoxLayout()

        fontRow = QHBoxLayout()

        self.speechFont = QFontComboBox(self) 
        fontRow.addWidget(self.speechFont)

        self.speechFontSize = QSpinBox(self)
        self.speechFontSize.setValue(14)
        self.speechFontSize.setMinimum(1)
        fontRow.addWidget(self.speechFontSize)

        self.currentFontColorButton = QPushButton(self)
        self.speechFontColor = QColor("black")
        fontColorImage = QPixmap(32,32)
        fontColorImage.fill(self.speechFontColor)
        fontColorIcon = QIcon(fontColorImage)
        self.currentFontColorButton.setIcon(fontColorIcon)
        self.currentFontColorButton.setFixedWidth(self.currentFontColorButton.height())
        fontRow.addWidget(self.currentFontColorButton)

        speechGroupLayout.addLayout(fontRow)



        # MARK: misc
        self.bubbleText = QTextEdit("Rogudator's speech bubble generator!")
        speechGroupLayout.addWidget(self.bubbleText)

        self.autocenter = QCheckBox(self)
        self.autocenter.setText("Center automatically")
        self.autocenter.setChecked(True)
        speechGroupLayout.addWidget(self.autocenter)

        self.averageLineLength = QGroupBox()
        averageLineLengthSliderAndSpinBox = QHBoxLayout()
        self.averageLineLengthSlider = QSlider(self)
        self.averageLineLengthSlider.setMinimum(0)
        self.averageLineLengthSlider.setMaximum(100)
        self.averageLineLengthSlider.setOrientation(Qt.Orientation.Horizontal)
        averageLineLengthSliderAndSpinBox.addWidget(self.averageLineLengthSlider)

        self.averageLineLengthSpinBox = QSpinBox(self)
        self.averageLineLengthSpinBox.setMinimum(0)
        averageLineLengthSliderAndSpinBox.addWidget(self.averageLineLengthSpinBox)
        self.averageLineLength.setLayout(averageLineLengthSliderAndSpinBox)
        self.averageLineLength.setDisabled(True)
        speechGroupLayout.addWidget(self.averageLineLength)

        speechGroup.setLayout(speechGroupLayout)
        mainLayout.addWidget(speechGroup)



        # MARK:bubble tail params
        tailSize = QGroupBox()
        tailSize.setTitle("Tail size")
        tailSliderAndSpinBox = QHBoxLayout()
        self.tailSizeSlider = QSlider(self)
        self.tailSizeSlider.setMinimum(0)
        self.tailSizeSlider.setMaximum(self.speechFontSize.value()*10)
        self.tailSizeSlider.setOrientation(Qt.Orientation.Horizontal)
        tailSliderAndSpinBox.addWidget(self.tailSizeSlider)

        self.tailSpinBox = QSpinBox(self)
        self.tailSpinBox.setMinimum(0)
        self.tailSpinBox.setMaximum(self.speechFontSize.value()*10)
        tailSliderAndSpinBox.addWidget(self.tailSpinBox)
        tailSize.setLayout(tailSliderAndSpinBox)
        mainLayout.addWidget(tailSize)

        #MARK:>>TODO<<
        # TODO: change to angle input, options for 90 degree movements CW and CCW as well as 180 flip

        self.tailPositions = QGroupBox()
        self.tailPositions.setTitle("Tail position")
        tailPositionsLayout = QHBoxLayout()

        self.tailPosition = []
        for i in range(8):
            self.tailPosition.append(QRadioButton(self))
            self.tailPosition[i].setText(str(i + 1))
            self.tailPosition[i].clicked.connect(self.updatePreview)
            tailPositionsLayout.addWidget(self.tailPosition[i])
        
        # self.tailPositionSlider = QSlider(self)
        # self.tailPositionSlider.setMinimum(0)
        # self.tailPositionSlider.setMaximum(360)
        # self.tailPositionSlider.setValue(45)
        # self.tailPositionSlider.setOrientation(Qt.Orientation.Horizontal)
        # tailPositionsLayout.addWidget(self.tailPositionSlider)
        
        # self.tailPositionSpinBox = QSpinBox(self)
        # self.tailPositionSpinBox.setMinimum(0)
        # self.tailPositionSpinBox.setMaximum(360)
        # self.tailPositionSpinBox.setValue(45)
        # tailPositionsLayout.addWidget(self.tailPositionSpinBox)
        
        self.tailPositions.setLayout(tailPositionsLayout)
        self.tailPositions.setDisabled(True)

        mainLayout.addWidget(self.tailPositions)

        self.updatePreview()



        # MARK:signal connections

        self.addOnPage.clicked.connect(self.addOnPageShape)
        
        # bubble type signals
        self.squareBubble.clicked.connect(self.updatePreview)
        self.roundBubble.clicked.connect(self.updatePreview)
        # self.squircleBubble.clicked.connect(self.updatePreview)

        # bubble outline param signals
        self.bubbleColorButton.clicked.connect(self.changeBubbleColor)
        self.bOutlineThicknessSlider.valueChanged.connect(self.outlineSpinBoxUpdate)
        self.bOutlineThicknessSpinBox.valueChanged.connect(self.outlineSliderUpdate)
        self.bOutlineColorButton.clicked.connect(self.changeOutlineColor)

        # bubble text param signals
        self.bubbleText.textChanged.connect(self.updatePreview)
        self.speechFontSize.valueChanged.connect(self.tailSliderUpdateMaximum)
        self.currentFontColorButton.clicked.connect(self.changeFontColor)
        self.speechFont.currentFontChanged.connect(self.updatePreview)
        self.autocenter.stateChanged.connect(self.enableAverageLineLength)
        self.averageLineLengthSlider.valueChanged.connect(self.averageLineLengthSpinBoxUpdate)
        self.averageLineLengthSpinBox.valueChanged.connect(self.averageLineLengthSliderUpdate)

        # bubble tail param signals
        self.tailSizeSlider.valueChanged.connect(self.tailSpinBoxUpdate)
        self.tailSpinBox.valueChanged.connect(self.tailSliderUpdate)



        self.scrollMainLayout = QScrollArea(self)
        self.scrollMainLayout.setWidgetResizable(True)
        self.scrollMainLayout.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        widget = QWidget()
        widget.setLayout(mainLayout)
        self.scrollMainLayout.setWidget(widget)
        self.setWidget(self.scrollMainLayout)
        self.show()



    # MARK:functions

    def changeFontColor(self):
        self.speechFontColor = QColorDialog.getColor(self.speechFontColor)
        colorImage = QPixmap(32,32)
        colorImage.fill(self.speechFontColor)
        colorIcon = QIcon(colorImage)
        self.currentFontColorButton.setIcon(colorIcon)
        self.updatePreview()

    def tailSliderUpdateMaximum(self):
        self.tailSizeSlider.setMaximum(self.speechFontSize.value()*10)
        self.tailSpinBox.setMaximum(self.speechFontSize.value()*10)
        self.updatePreview()

    def changeBubbleColor(self):
        self.bubbleColor = QColorDialog.getColor(self.bubbleColor)
        colorImage = QPixmap(32,32)
        colorImage.fill(self.bubbleColor)
        colorIcon = QIcon(colorImage)
        self.bubbleColorButton.setIcon(colorIcon)
        self.updatePreview()

    def changeOutlineColor(self):
        self.outlineColor = QColorDialog.getColor(self.outlineColor)
        colorImage = QPixmap(32,32)
        colorImage.fill(self.outlineColor)
        colorIcon = QIcon(colorImage)
        self.bOutlineColorButton.setIcon(colorIcon)
        self.updatePreview()

    def outlineSpinBoxUpdate(self):
        self.bOutlineThicknessSpinBox.setValue(self.bOutlineThicknessSlider.value())

    def outlineSliderUpdate(self):
        if self.bOutlineThicknessSpinBox.value() < 51:
            self.bOutlineThicknessSlider.setValue(self.bOutlineThicknessSpinBox.value())
        self.updatePreview()

    def tailSpinBoxUpdate(self):
        self.tailSpinBox.setValue(self.tailSizeSlider.value())
        if self.tailSizeSlider.value() == 0:
            self.tailPositions.setDisabled(True)
        else:
            self.tailPositions.setDisabled(False)

    def tailSliderUpdate(self):
        if self.tailSpinBox.value()<101:
            self.tailSizeSlider.setValue(self.tailSpinBox.value())
        self.updatePreview()

    def enableAverageLineLength(self):
        if self.autocenter.isChecked():
            self.averageLineLength.setDisabled(True)
        else:
            self.averageLineLength.setDisabled(False)
        self.updatePreview()

    def averageLineLengthSpinBoxUpdate(self):
        self.averageLineLengthSpinBox.setValue(self.averageLineLengthSlider.value())

    def averageLineLengthSliderUpdate(self):
        if self.averageLineLengthSpinBox.value()<101:
            self.averageLineLengthSlider.setValue(self.averageLineLengthSpinBox.value())
        self.updatePreview()

    def getSpeechLines(self, text, lineLength):
        size = 0
        speach = ""
        lines = []
        if (lineLength>0):
            words = text.split(" ")
            for word in words:
                speach += word
                size += len(word)
                if size < lineLength:
                    speach += " "
                else:
                    size = 0
                    lines.append(speach)
                    speach = ""
            if (speach != "") and (speach != " "):
                lines.append(speach.strip())
        else:
            lines = text.split("\n")

        return lines

    def getPreview(self):

        # ----- calculate text geometry -----
        lineLength = int((pow((len(self.bubbleText.toPlainText())), 1/2)) * 1.8)
        if not(self.autocenter.isChecked()):
            lineLength = self.averageLineLengthSpinBox.value()
        lines = self.getSpeechLines(self.bubbleText.toPlainText(), lineLength)

        biggestLine = ""
        for line in lines:
            if (len(line) > len(biggestLine)):
                biggestLine = line

        #Calculate text box size
        font = self.speechFont.currentFont()
        font.setPixelSize(int(self.speechFontSize.value()*1.3))
        fontSize = self.speechFontSize.value()
        textHeight = int(fontSize * (len(lines)) - (fontSize - QFontMetrics(font).capHeight()))
        textWidth = QFontMetrics(font).width(biggestLine)
        tailLength = self.tailSpinBox.value()

        tailPadding = tailLength
        bubblePadding = int(fontSize*1.5)

        textTag = "<text x=\"{}\" y=\"{}\" style=\"font-size:{};font-family:{};fill:{};text-anchor:middle\" >{}</text>"
        text = ""
        textStartX = fontSize + tailPadding + bubblePadding + (int(textWidth/2))
        textStartY = fontSize + tailPadding + bubblePadding + QFontMetrics(font).capHeight()

        for line in lines:
            text += textTag.format(textStartX, textStartY, fontSize, font.family(), self.speechFontColor.name(), line)
            textStartY += fontSize


        # ----- calculate bubble geometry -----

        #              bCoordsX0      bCoordsXHalf     bCoordsX1 
        #                  |               |               |
        #     bCoordsY0 -> +---------------+---------------+
        #                  |                               |
        #                  |                               |
        #  bCoordsYHalf -> +                               +
        #                  |                               |
        #                  |                               |
        #     bCoordsY1 -> +---------------+---------------+

        bCoordsX0    = fontSize + tailPadding
        bCoordsY0    = fontSize + tailPadding
        bCoordsXHalf = fontSize + tailPadding + bubblePadding + (int(textWidth/2))
        bCoordsYHalf = fontSize + tailPadding + bubblePadding + (int(textHeight/2))
        bCoordsX1    = fontSize + tailPadding + bubblePadding + textWidth + bubblePadding
        bCoordsY1    = fontSize + tailPadding + bubblePadding + textHeight + bubblePadding
        bubbleCoordinates = [
            BubbleCoordinates(bCoordsXHalf, bCoordsY0     ),
            BubbleCoordinates(bCoordsX1,    bCoordsY0     ),
            BubbleCoordinates(bCoordsX1,    bCoordsYHalf  ),
            BubbleCoordinates(bCoordsX1,    bCoordsY1     ),
            BubbleCoordinates(bCoordsXHalf, bCoordsY1     ),
            BubbleCoordinates(bCoordsX0,    bCoordsY1     ),
            BubbleCoordinates(bCoordsX0,    bCoordsYHalf  ),
            BubbleCoordinates(bCoordsX0,    bCoordsY0     )
        ]

        bCoordsString = 'M'
        bubbleCoordinatesStringEnd = f'{bCoordsXHalf},{bCoordsY0}Z'
        for i in range(8):
            if (self.roundBubble.isChecked()):

                if (self.tailSpinBox.value() > 0):
                    #for coordinates in center (even)
                    textWidth01 = int(pow(textWidth,1/2.8))
                    textHeight01 = int(pow(textHeight,1/2))
                    #for coordinates in the corner (odd)
                    x04 = int((bCoordsX1 - bCoordsXHalf)*0.4)
                    x06 = int((bCoordsX1 - bCoordsXHalf)*0.6)
                    y04 = int((bCoordsYHalf - bCoordsY0)*0.4)
                    y06 = int((bCoordsYHalf - bCoordsY0)*0.6)
                    if i == 0 and self.tailPosition[i].isChecked():
                        bCoordsString += f'{bCoordsXHalf - textWidth01},{bCoordsY0} L{bCoordsXHalf},{bCoordsY0 - tailLength} {bCoordsXHalf + textWidth01},{bCoordsY0} Z'

                        bubbleCoordinatesStringEnd = ''.join(
                            str(bCoordsXHalf - textWidth01), ",",
                            str(bCoordsY0), "Z")

                    elif i == 2 and self.tailPosition[i].isChecked():
                        bCoordsString += str(bCoordsX1) + "," + str(bCoordsYHalf - textHeight01) + " L" + str(bCoordsX1 + tailLength) + "," + str(bCoordsYHalf) + " " + str(bCoordsX1) + "," + str(bCoordsYHalf + textHeight01) + " "
                    elif i == 4 and self.tailPosition[i].isChecked():
                        bCoordsString += str(bCoordsXHalf + textWidth01) + "," + str(bCoordsY1) + " L" + str(bCoordsXHalf) + "," + str(bCoordsY1 + tailLength) + " " + str(bCoordsXHalf - textWidth01) + "," + str(bCoordsY1) + " "
                    elif i == 6 and self.tailPosition[i].isChecked():
                        bCoordsString += str(bCoordsX0) + "," + str(bCoordsYHalf + textHeight01) + " L" + str(bCoordsX0 - tailLength) + "," + str(bCoordsYHalf) + " " + str(bCoordsX0) + "," + str(bCoordsYHalf - textHeight01) + " "

                    elif i == 1 and self.tailPosition[i].isChecked():
                        bCoordsString += "Q" + str(bCoordsX1 - x06) + "," + str(bCoordsY0) + " " + str(int((bCoordsX1 + bCoordsX1 - x06)/2)) + "," + str(int((bCoordsY0 + y04 + bCoordsY0)/2)) + " L" + str(bCoordsX1 + tailLength) + "," + str(bCoordsY0 - tailLength) + " " + str(int((bCoordsX1 + bCoordsX1 - x04)/2)) + "," + str(int((bCoordsY0 + y06 + bCoordsY0)/2)) + " Q"  + str(bCoordsX1) + "," + str(bCoordsY0 + y06) + " "
                    elif i == 3 and self.tailPosition[i].isChecked():
                        bCoordsString += "Q" + str(bCoordsX1) + "," + str(bCoordsY1 - y06) + " " + str(int((bCoordsX1 + bCoordsX1 - x04)/2)) + "," + str(int((bCoordsY1 - y06 + bCoordsY1)/2)) + " L" + str(bCoordsX1 + tailLength) + "," + str(bCoordsY1 + tailLength) + " " + str(int((bCoordsX1 + bCoordsX1 - x06)/2)) + "," + str(int((bCoordsY1 - y04 + bCoordsY1)/2)) + " Q" + str(bCoordsX1 - x06) + "," + str(bCoordsY1) + " "
                    elif i == 5 and self.tailPosition[i].isChecked():
                        bCoordsString += "Q" + str(bCoordsX0 + x06) + "," + str(bCoordsY1) + " " + str(int((bCoordsX0 + bCoordsX0 + x06)/2)) + "," + str(int((bCoordsY1 - y04 + bCoordsY1)/2)) + " L" + str(bCoordsX0 - tailLength) + "," + str(bCoordsY1 + tailLength) + " " + str(int((bCoordsX0 + bCoordsX0 + x04)/2)) + "," + str(int((bCoordsY1 - y06 + bCoordsY1)/2)) + " Q"  + str(bCoordsX0) + "," + str(bCoordsY1 - y06) + " "
                    elif i == 7 and self.tailPosition[i].isChecked():
                        bCoordsString += "Q" + str(bCoordsX0) + "," + str(bCoordsY0 + y06) + " " + str(int((bCoordsX0 + bCoordsX0 + x04)/2)) + "," + str(int((bCoordsY0 + y06 + bCoordsY0)/2)) + " L" + str(bCoordsX0 - tailLength) + "," + str(bCoordsY0 - tailLength) + " " + str(int((bCoordsX0 + bCoordsX0 + x06)/2)) + "," + str(int((bCoordsY0 + y04 + bCoordsY0)/2)) + " Q" + str(bCoordsX0 + x06) + "," + str(bCoordsY0) + " "
                    else:
                        if (i % 2 == 0):
                            bCoordsString += str(bubbleCoordinates[i].x) + "," + str(bubbleCoordinates[i].y) + " "
                        else:
                            bCoordsString += "Q" +  str(bubbleCoordinates[i].x) + "," + str(bubbleCoordinates[i].y) + " "
                else:
                        if (i % 2 == 0):
                            bCoordsString += str(bubbleCoordinates[i].x) + "," + str(bubbleCoordinates[i].y) + " "
                        else:
                            bCoordsString += "Q" +  str(bubbleCoordinates[i].x) + "," + str(bubbleCoordinates[i].y) + " "
            elif (self.squareBubble.isChecked()):
                bCoordsString += str(bubbleCoordinates[i].x) + "," + str(bubbleCoordinates[i].y) + " "

        bCoordsString += bubbleCoordinatesStringEnd
        pathStyle = "style=\"fill:{};stroke:{};stroke-width:{};stroke-linejoin:round\"".format(self.bubbleColor.name(),self.outlineColor.name(),self.bOutlineThicknessSpinBox.value())
        bubble = "<path " +  pathStyle  + " d=\"" +  bCoordsString  + "\"/>"

        frameWidth = fontSize + tailPadding + bubblePadding + textWidth + bubblePadding + tailPadding + fontSize
        frameHeight = fontSize + tailPadding + bubblePadding + textHeight + bubblePadding + tailPadding + fontSize

        result = "<svg width=\"{}\" height=\"{}\" >{}{}</svg>".format(frameWidth, frameHeight, bubble, text)

        return result

    def updatePreview(self):
        result = self.getPreview()
        resultBytes = bytearray(result,encoding='utf-8')
        self.preview.renderer().load(resultBytes)

    def addOnPageShape(self):
        result = self.getPreview()
        d = Krita.instance().activeDocument()
        root = d.rootNode()
        l3 = d.createVectorLayer(self.bubbleText.toPlainText()[:16])
        root.addChildNode(l3, None)
        l3.addShapesFromSvg(result)




    def canvasChanged(self, canvas):
        pass

Krita.instance().addDockWidgetFactory(DockWidgetFactory("Laserkitty's Speech Bubble Generator", DockWidgetFactoryBase.DockRight, LSBGDocker))