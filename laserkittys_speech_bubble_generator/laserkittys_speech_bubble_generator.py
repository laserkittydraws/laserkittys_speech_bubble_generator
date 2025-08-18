from PyQt5.QtGui import QColor, QFontMetrics, QFontMetricsF, QIcon, QPixmap, QResizeEvent
from PyQt5.QtWidgets import QApplication, QCheckBox, QColorDialog, QFontComboBox, QGroupBox, QLabel, QMainWindow, QPushButton, QRadioButton, QSlider, QSpinBox, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QScrollBar, QSizePolicy
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, QRect, QSize

from krita import Krita, DockWidget, DockWidgetFactory, DockWidgetFactoryBase

from math import cos, sin, acos, asin, sqrt, pi
import xml.etree.ElementTree as ET
from datetime import datetime

import logging
logger = logging.getLogger('lsbg')
LSBG_DEBUG = 15 ; logging.addLevelName(LSBG_DEBUG, 'LSBG_DEBUG')
logging.basicConfig(
    filename=f'{Krita.getAppDataLocation()}/pykrita/laserkittys_speech_bubble_generator/logs/lsbg_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log',
    format='%(asctime)s: %(name)s - [%(levelname)s] - %(message)s',
    level=LSBG_DEBUG
)
logger.info(f'Krita version: {Application.version()}')
LSBG_PLUGIN_VERSION = '0.0.1' ; logger.info(f'LSBG version: {LSBG_PLUGIN_VERSION}')

MAINLAYOUT_CONTENTS_MARGINS = 10
MAINLAYOUT_MIN_WIDTH = 352

class LSBGDocker(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("LaserKitty's speech bubble generator")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(
            MAINLAYOUT_CONTENTS_MARGINS,
            MAINLAYOUT_CONTENTS_MARGINS,
            MAINLAYOUT_CONTENTS_MARGINS,
            MAINLAYOUT_CONTENTS_MARGINS
        )

        self.addOnPageLayout = QHBoxLayout()
        self.addOnPageLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.addOnPage = QPushButton("Add on Page")
        self.addOnPage.setFixedWidth(100)
        self.addOnPageLayout.addWidget(self.addOnPage)
        self.mainLayout.addLayout(self.addOnPageLayout)

        self.previewBox = QGroupBox()
        self.previewBox.setTitle("Preview")
        self.previewBoxLayout = QVBoxLayout()
        self.previewBox.setLayout(self.previewBoxLayout)
        self.preview = QSvgWidget(self)
        self.preview.setFixedSize(300,200)
        self.preview.renderer().setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        self.previewBoxLayout.addWidget(self.preview)
        self.mainLayout.addWidget(self.previewBox)

        # MARK: bubble params
        self.bubbleTypes = QGroupBox()
        self.bubbleTypes.setTitle("Bubble type")
        self.bubbleTypesLayout = QHBoxLayout()

        self.roundBubble = QRadioButton(self)
        self.roundBubble.setText("Round")
        self.roundBubble.setChecked(True)
        self.bubbleTypesLayout.addWidget(self.roundBubble)

        self.squareBubble = QRadioButton(self)
        self.squareBubble.setText("Square")
        self.squareBubble.setDisabled(True)
        self.bubbleTypesLayout.addWidget(self.squareBubble)

        self.squircleBubble = QRadioButton(self)
        self.squircleBubble.setText("Squircle")
        self.squircleBubble.setDisabled(True)
        self.bubbleTypesLayout.addWidget(self.squircleBubble)

        # self.thoughtBubble = QRadioButton(self)
        # self.thoughtBubble.setText("Thought")
        # self.thoughtBubble.setDisabled(True)
        # self.bubbleTypesLayout.addWidget(self.thoughtBubble)

        # self.shoutBubble = QRadioButton(self)
        # self.shoutBubble.setText("Shout")
        # self.shoutBubble.setDisabled(True)
        # self.bubbleTypesLayout.addWidget(self.shoutBubble)

        # TODO: change bubble type selection to a dropdown

        self.bubbleColorButton = QPushButton(self)
        self.bubbleColor = QColor("white")
        self.bubbleColorImage = QPixmap(32,32)
        self.bubbleColorImage.fill(self.bubbleColor)
        self.bubbleColorIcon = QIcon(self.bubbleColorImage)
        self.bubbleColorButton.setIcon(self.bubbleColorIcon)
        self.bubbleColorButton.setFixedWidth(self.bubbleColorButton.height())
        self.bubbleTypesLayout.addWidget(self.bubbleColorButton)

        self.bubbleTypes.setLayout(self.bubbleTypesLayout)
        self.mainLayout.addWidget(self.bubbleTypes)



        # MARK:outline params
        self.outlineSize = QGroupBox("Outline")
        self.bOutlineThicknessLayout = QHBoxLayout()

        self.bOutlineThicknessSlider = QSlider(self)
        self.bOutlineThicknessSlider.setMinimum(0)
        self.bOutlineThicknessSlider.setMaximum(10)
        self.bOutlineThicknessSlider.setValue(3)
        self.bOutlineThicknessSlider.setOrientation(Qt.Orientation.Horizontal)
        self.bOutlineThicknessLayout.addWidget(self.bOutlineThicknessSlider)

        self.bOutlineThicknessSpinBox = QSpinBox(self)
        self.bOutlineThicknessSpinBox.setMinimum(0)
        self.bOutlineThicknessSpinBox.setValue(3)
        self.bOutlineThicknessLayout.addWidget(self.bOutlineThicknessSpinBox)

        self.bOutlineColorButton = QPushButton(self)
        self.outlineColor = QColor("black")
        self.outlineColorImage = QPixmap(32,32)
        self.outlineColorImage.fill(self.outlineColor)
        self.outlineColorIcon = QIcon(self.outlineColorImage)
        self.bOutlineColorButton.setIcon(self.outlineColorIcon)
        self.bOutlineColorButton.setFixedWidth(self.bOutlineColorButton.height())
        self.bOutlineThicknessLayout.addWidget(self.bOutlineColorButton)

        self.outlineSize.setLayout(self.bOutlineThicknessLayout)
        self.mainLayout.addWidget(self.outlineSize)



        # MARK:text params
        self.speechGroup = QGroupBox("Speech")
        self.speechGroupLayout = QVBoxLayout()

        self.fontRow = QHBoxLayout()

        self.speechFont = QFontComboBox(self)
        self.fontRow.addWidget(self.speechFont)

        self.speechFontSize = QSpinBox(self)
        self.speechFontSize.setValue(14)
        self.speechFontSize.setMinimum(1)
        self.fontRow.addWidget(self.speechFontSize)

        self.currentFontColorButton = QPushButton(self)
        self.speechFontColor = QColor("black")
        self.fontColorImage = QPixmap(32,32)
        self.fontColorImage.fill(self.speechFontColor)
        self.fontColorIcon = QIcon(self.fontColorImage)
        self.currentFontColorButton.setIcon(self.fontColorIcon)
        self.currentFontColorButton.setFixedWidth(self.currentFontColorButton.height())
        self.fontRow.addWidget(self.currentFontColorButton)

        self.speechGroupLayout.addLayout(self.fontRow)



        # MARK: misc
        self.bubbleText = QTextEdit("Laserkitty's speech bubble generator!")
        self.speechGroupLayout.addWidget(self.bubbleText)

        self.autocenter = QCheckBox(self)
        self.autocenter.setText("Center automatically")
        self.autocenter.setChecked(True)
        self.speechGroupLayout.addWidget(self.autocenter)


        self.averageLineLength = QGroupBox()
        self.avgLineLenSliderAndSpinBox = QHBoxLayout()

        self.averageLineLengthSlider = QSlider(self)
        self.averageLineLengthSlider.setMinimum(0)
        self.averageLineLengthSlider.setMaximum(100)
        self.averageLineLengthSlider.setOrientation(Qt.Orientation.Horizontal)
        self.avgLineLenSliderAndSpinBox.addWidget(self.averageLineLengthSlider)

        self.averageLineLengthSpinBox = QSpinBox(self)
        self.averageLineLengthSpinBox.setMinimum(0)
        self.avgLineLenSliderAndSpinBox.addWidget(self.averageLineLengthSpinBox)
        
        self.averageLineLength.setLayout(self.avgLineLenSliderAndSpinBox)
        self.averageLineLength.setDisabled(True)
        self.speechGroupLayout.addWidget(self.averageLineLength)

        self.speechGroup.setLayout(self.speechGroupLayout)
        self.mainLayout.addWidget(self.speechGroup)



        # MARK:bubble tail params
        self.tailSize = QGroupBox()
        self.tailSize.setTitle("Tail size")
        self.tLenWidth = QVBoxLayout()


        self.tLenSliderAndSpinBox = QHBoxLayout()
        self.tLengthLabel = QLabel("Tail Length:")
        self.tLenSliderAndSpinBox.addWidget(self.tLengthLabel)

        self.tLengthSlider = QSlider(self)
        self.tLengthSlider.setMinimum(0)
        self.tLengthSlider.setMaximum(self.speechFontSize.value()*10)
        self.tLengthSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tLenSliderAndSpinBox.addWidget(self.tLengthSlider)

        self.tLengthSpinBox = QSpinBox(self)
        self.tLengthSpinBox.setMinimum(0)
        self.tLengthSpinBox.setMaximum(self.speechFontSize.value()*10)
        self.tLengthSpinBox.setValue(10)
        self.tLenSliderAndSpinBox.addWidget(self.tLengthSpinBox)
        self.tLenWidth.addLayout(self.tLenSliderAndSpinBox)


        self.tWidthSliderAndSpinBox = QHBoxLayout()
        self.tWidthLabel = QLabel("Tail Width:")
        self.tWidthSliderAndSpinBox.addWidget(self.tWidthLabel)

        self.tWidthSlider = QSlider(self)
        self.tWidthSlider.setMinimum(0)
        self.tWidthSlider.setMaximum(self.speechFontSize.value()*10)
        self.tWidthSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tWidthSliderAndSpinBox.addWidget(self.tWidthSlider)

        self.tWidthSpinBox = QSpinBox(self)
        self.tWidthSpinBox.setMinimum(0)
        self.tWidthSpinBox.setMaximum(self.speechFontSize.value()*10)
        self.tWidthSpinBox.setValue(10)
        self.tWidthSliderAndSpinBox.addWidget(self.tWidthSpinBox)
        self.tLenWidth.addLayout(self.tWidthSliderAndSpinBox)

        self.tailSize.setLayout(self.tLenWidth)
        self.mainLayout.addWidget(self.tailSize)

        self.tailPositions = QGroupBox()
        self.tailPositions.setTitle("Tail position")
        self.tailPositionsLayout = QHBoxLayout()

        self.tailAnglePositionSlider = QSlider(self)
        self.tailAnglePositionSlider.setMinimum(0)
        self.tailAnglePositionSlider.setMaximum(360)
        self.tailAnglePositionSlider.setValue(45)
        self.tailAnglePositionSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tailPositionsLayout.addWidget(self.tailAnglePositionSlider)
        
        self.tAnglePosSpinBox = QSpinBox(self)
        self.tAnglePosSpinBox.setMinimum(0)
        self.tAnglePosSpinBox.setMaximum(360)
        self.tAnglePosSpinBox.setValue(45)
        self.tailPositionsLayout.addWidget(self.tAnglePosSpinBox)

        self.flipAngleH = QPushButton()
        self.flipAngleH.setIcon(QIcon(Krita.instance().icon('flip_angle_h')))
        self.tailPositionsLayout.addWidget(self.flipAngleH)
        self.flipAngleV = QPushButton()
        self.flipAngleV.setIcon(QIcon(Krita.instance().icon('flip_angle_v')))
        self.tailPositionsLayout.addWidget(self.flipAngleV)
        self.flipAngleHV = QPushButton()
        self.flipAngleHV.setIcon(QIcon(Krita.instance().icon('flip_angle_hv')))
        self.tailPositionsLayout.addWidget(self.flipAngleHV)

        # TODO: change tail position angle selector to AngleSelector when krita 5.3 or 5.2.12 releases
        # self.angleSelector = AngleSelector()
        # tailPositionsLayout.addWidget(self.angleSelector)

        self.tailPositions.setLayout(self.tailPositionsLayout)
        self.mainLayout.addWidget(self.tailPositions)



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
        self.averageLineLengthSlider.valueChanged.connect(self.avgLineLenSpinBoxUpdate)
        self.averageLineLengthSpinBox.valueChanged.connect(self.avgLineLenSliderUpdate)

        # bubble tail param signals
        self.tLengthSlider.valueChanged.connect(self.tLengthSpinBoxUpdate)
        self.tLengthSpinBox.valueChanged.connect(self.tLengthSliderUpdate)
        self.tWidthSlider.valueChanged.connect(self.tWidthSpinBoxUpdate)
        self.tWidthSpinBox.valueChanged.connect(self.tWidthSliderUpdate)
        self.tailAnglePositionSlider.valueChanged.connect(self.tailPositionSpinBoxUpdate)
        self.tAnglePosSpinBox.valueChanged.connect(self.tailPositionSliderUpdate)
        self.flipAngleH.clicked.connect(self.flipAngleH_f)
        self.flipAngleV.clicked.connect(self.flipAngleV_f)
        self.flipAngleHV.clicked.connect(self.flipAngleHV_f)



        self.scrollMainLayout = QScrollArea(self)
        self.scrollMainLayout.setWidgetResizable(True)
        self.scrollMainLayout.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.qw = QWidget()
        self.qw.setLayout(self.mainLayout)
        self.scrollMainLayout.setWidget(self.qw)
        self.setWidget(self.scrollMainLayout)
        self.show()
        self.updatePreview()



    # MARK:functions

    def changeFontColor(self):
        self.speechFontColor = QColorDialog.getColor(self.speechFontColor)
        colorImage = QPixmap(32,32)
        colorImage.fill(self.speechFontColor)
        colorIcon = QIcon(colorImage)
        self.currentFontColorButton.setIcon(colorIcon)
        self.updatePreview()

    def tailSliderUpdateMaximum(self):
        self.tLengthSlider.setMaximum(self.speechFontSize.value()*10)
        self.tLengthSpinBox.setMaximum(self.speechFontSize.value()*10)
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
        self.updatePreview()

    def outlineSliderUpdate(self):
        if self.bOutlineThicknessSpinBox.value() < 51: self.bOutlineThicknessSlider.setValue(self.bOutlineThicknessSpinBox.value())
        self.updatePreview()

    def tLengthSpinBoxUpdate(self):
        self.tLengthSpinBox.setValue(self.tLengthSlider.value())
        self.tailPositions.setEnabled(self.tLengthSlider.value() > 0)

    def tLengthSliderUpdate(self):
        if self.tLengthSpinBox.value() < 101: self.tLengthSlider.setValue(self.tLengthSpinBox.value())
        self.updatePreview()

    def tWidthSpinBoxUpdate(self):
        self.tWidthSpinBox.setValue(self.tWidthSlider.value())
        self.tailPositions.setEnabled(self.tWidthSlider.value() > 0)

    def tWidthSliderUpdate(self):
        if self.tWidthSpinBox.value() < 101: self.tWidthSlider.setValue(self.tWidthSpinBox.value())
        self.updatePreview()

    def tailPositionSpinBoxUpdate(self):
        self.tAnglePosSpinBox.setValue(self.tailAnglePositionSlider.value())
        self.updatePreview()

    def tailPositionSliderUpdate(self):
        if self.tAnglePosSpinBox.value() < 360: self.tailAnglePositionSlider.setValue(self.tAnglePosSpinBox.value())
        self.updatePreview()

    def flipAngleH_f(self):
        currAngle = self.tAnglePosSpinBox.value()
        if currAngle <= 180: self.tAnglePosSpinBox.setValue(180 - currAngle)
        else: self.tAnglePosSpinBox.setValue(540 - currAngle)
        self.updatePreview()

    def flipAngleV_f(self):
        self.tAnglePosSpinBox.setValue(360 - self.tAnglePosSpinBox.value())
        self.updatePreview()

    def flipAngleHV_f(self):
        self.tAnglePosSpinBox.setValue((self.tAnglePosSpinBox.value() + 180) % 360)
        self.updatePreview()

    def enableAverageLineLength(self):
        self.averageLineLength.setDisabled(self.autocenter.isChecked())
        self.updatePreview()

    def avgLineLenSpinBoxUpdate(self):
        self.averageLineLengthSpinBox.setValue(self.averageLineLengthSlider.value())
        self.updatePreview()

    def avgLineLenSliderUpdate(self):
        if self.averageLineLengthSpinBox.value() < 101: self.averageLineLengthSlider.setValue(self.averageLineLengthSpinBox.value())
        if not self.autocenter.isChecked(): self.updatePreview()

    def getSpeechLines(self, text: str, lineLength: int) -> list[str]:
        size = 0
        speech = ''
        lines = []
        if lineLength > 0:
            for word in text.split(' '):
                speech += word
                size += len(word)
                if size < lineLength: speech += ' '
                else:
                    size = 0
                    lines.append(speech.rstrip())
                    speech = ''
            if speech not in ['', ' ']: lines.append(speech.rstrip())
            return lines
        return text.split('\n')

    def getPreview(self) -> str:

        # ----- calculate text geometry -----
        lineLength = int((pow((len(self.bubbleText.toPlainText())), 1/2)) * 1.8) if self.autocenter.isChecked() else self.averageLineLengthSpinBox.value()
        lines = self.getSpeechLines(self.bubbleText.toPlainText(), lineLength)

        #Calculate text box size
        font = self.speechFont.currentFont()
        font.setPointSize(self.speechFontSize.value())
        fontSize = self.speechFontSize.value()
        textWidth = 0
        for line in lines: textWidth = QFontMetricsF(font).width(line) if QFontMetricsF(font).width(line) > textWidth else textWidth
        textHeight = QFontMetrics(font).capHeight() + QFontMetricsF(font).lineSpacing()*(len(lines)-1)
        tailLength = self.tLengthSpinBox.value()
        tailWidth = self.tWidthSpinBox.value()
        bPadding = int(fontSize*1.5)

        #  +--------------------------------------------------------------------------------> X
        #  |          tailLength
        #  |   <-------->
        #  |                                 padding           (  theta = 0 starts  )
        #  |                              <---->               ( at the pos x-axis, )
        #  |            <---- bubbleWidth  ---->               ( theta increases CW )
        #  |                 <-textWidth ->
        #  |   +----------------------------------------+                                  /|\
        #  |   |                                        |                                   |
        #  |   |                                        |                                   |
        #  |   |        +----------------------+        | /|\             /|\               | frameHeight
        #  |   |        |                      |        |  | padding       |                |
        #  |   |        |                      |        | \|/              |                |
        #  |   |        |    +------------+    |        | /|\              | bubbleHeight   |
        #  |   |        |    |            |    |        |  |               |                |
        #  |   |        |    |    text    |    |        |  | textHeight    |                |
        #  |   |        |    |            |    |        |  |               |                |
        #  |   |        |    +------------+    |        | \|/              |                |
        #  |   |        |                      |        |                  |                |
        #  |   |        |                      |        |                  |                |
        #  |   |        +----------------------+        | /|\             \|/               |
        #  |   |          \    /                        |  | tailLength                     |
        #  |   |           \  /                         |  |                                |
        # \|/  +----------------------------------------+ \|/                              \|/
        #  Y

        bWidth  = bPadding + textWidth  + bPadding
        bHeight = bPadding + textHeight + bPadding
        frameWidth  = tailLength + bPadding + textWidth  + bPadding + tailLength
        frameHeight = tailLength + bPadding + textHeight + bPadding + tailLength

        text = ''
        textStartX = tailLength + bPadding + (textWidth  / 2)
        textStartY = tailLength + bPadding + QFontMetrics(font).capHeight()
        for line in lines:
            text += f'<text x=\"{textStartX}\" y=\"{textStartY}\" \
                style=\"font-size:{fontSize};font-family:{font.family()}; \
                fill:{self.speechFontColor.name()};text-anchor:middle\" >{line}</text>'
            textStartY += QFontMetricsF(font).lineSpacing()

        theta = self.tAnglePosSpinBox.value() * (2*pi) / 360

        if self.roundBubble.isChecked():
            if tailLength > 0 and tailWidth > 0:
                fourASqr = 4*(bWidth/2)*(bWidth/2)
                fourBSqr = 4*(bHeight/2)*(bHeight/2)
                thetaD = asin(tailWidth / sqrt( (fourASqr + fourBSqr)*sin(theta)*sin(theta) + fourBSqr ))

                tailPointX0 = ((bWidth  / 2)*cos(theta - thetaD)) + (frameWidth  / 2)
                tailPointY0 = ((bHeight / 2)*sin(theta - thetaD)) + (frameHeight / 2)
                tailPointX1 = ((bWidth  / 2)*cos(theta + thetaD)) + (frameWidth  / 2)
                tailPointY1 = ((bHeight / 2)*sin(theta + thetaD)) + (frameHeight / 2)

                dX = (bWidth  / 2) * sin(theta) * -1
                dY = (bHeight / 2) * cos(theta)
                tailEndX = (bWidth  / 2) * cos(theta) + (frameWidth  / 2) + (max(tailLength,1) * (dY / sqrt(dX*dX + dY*dY)))
                tailEndY = (bHeight / 2) * sin(theta) + (frameHeight / 2) - (max(tailLength,1) * (dX / sqrt(dX*dX + dY*dY)))

                bubblePath = f'M {tailPointX0} {tailPointY0} A {bWidth/2} {bHeight/2} \
                    0 1 0 {tailPointX1} {tailPointY1} L {tailEndX} {tailEndY} Z'

            else:
                ellipsePX = (bWidth/2) + (frameWidth/2)
                ellipsePY = frameHeight/2
                bubblePath = f'M {ellipsePX} {ellipsePY} \
                    A {bWidth/2} {bHeight/2} 0 1 0 {ellipsePX-bWidth} {ellipsePY} \
                    A {bWidth/2} {bHeight/2} 0 1 0 {ellipsePX} {ellipsePY} Z'

        if self.squareBubble.isChecked(): pass
        if self.squircleBubble.isChecked(): pass
        # if self.thoughtBubble.isChecked(): pass
        # if self.shoutBubble.isChecked(): pass

        bubble = f'<path style="fill:{self.bubbleColor.name()};stroke:{self.outlineColor.name()};\
            stroke-width:{self.bOutlineThicknessSpinBox.value()};stroke-linejoin:round\" d=\"{bubblePath}"/>'
        posFixRect = f'<rect x="0" y="0" width="{frameWidth}" height="{frameHeight}" fill="#000000" \
            fill-opacity="0%" stroke="#000000" stroke-width="0" stroke-opacity="0%" />'
        self.preview.renderer().setViewBox(QRect(0,0,int(frameWidth), int((frameHeight))))
        return f'<svg keepaspectratio="xMidYMid meet" ><g>{posFixRect}{bubble}{text}</g></svg>'

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

    def _isSameSize(self, oldSize: QSize, newSize: QSize) -> bool:
        return (oldSize.width() == newSize.width()) and (oldSize.height() == newSize.height())

    def resizeEvent(self, ev: QResizeEvent):
        if not self._isSameSize(ev.oldSize(), ev.size()):
            self.getPreview()
            # logger.log(LSBG_DEBUG, f'{self.scrollMainLayout.widget().width()}')
            scrollBarWidth = 9999
            for c in self.widget().children(): scrollBarWidth = c.width() if c.width() < scrollBarWidth else scrollBarWidth
            if ev.size().width() >= MAINLAYOUT_MIN_WIDTH+(2*MAINLAYOUT_CONTENTS_MARGINS):
                newWidth = ev.size().width()-(4*scrollBarWidth)-MAINLAYOUT_CONTENTS_MARGINS
                self.preview.setFixedSize(int(newWidth), int(newWidth*0.667))

    def canvasChanged(self, canvas): pass

Krita.instance().addDockWidgetFactory(DockWidgetFactory("Laserkitty's Speech Bubble Generator", DockWidgetFactoryBase.DockRight, LSBGDocker))