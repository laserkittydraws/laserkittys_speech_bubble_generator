from PyQt5.QtGui import QColor, QFontMetrics, QFontMetricsF, QFont, QFontInfo, QIcon, QPixmap, QResizeEvent
from PyQt5.QtWidgets import QApplication, QColorDialog, QFontComboBox, QGroupBox, QLabel, QMainWindow, QPushButton, QRadioButton, QCheckBox, QComboBox, QSlider, QSpinBox, QDoubleSpinBox, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QScrollBar, QSizePolicy
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, QRect, QSize

from krita import Krita, DockWidget, DockWidgetFactory, DockWidgetFactoryBase

from math import cos, sin, acos, asin, sqrt, pi
from datetime import datetime

from laserkittys_speech_bubble_generator import Shapes
from laserkittys_speech_bubble_generator.Shapes import *
from laserkittys_speech_bubble_generator.config import *

import logging
logger = logging.getLogger('lsbg')
logging.addLevelName(LSBG_DEBUG_VERBOSE, 'LSBG_DEBUG')
logging.addLevelName(LSBG_DEBUG_MINIMAL, 'LSBG_DEBUG')
logging.basicConfig(
    filename=f'{Krita.getAppDataLocation()}/pykrita/laserkittys_speech_bubble_generator/logs/lsbg_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log',
    format='[%(levelname)s]: %(name)s - %(message)s',
    level=LSBG_DEBUG_VERBOSE if LSBG_LOGGING_LEVEL == 'VERBOSE' else LSBG_DEBUG_MINIMAL
)
logging.captureWarnings(True)
for bType in Shapes.__all__: getattr(Shapes,bType)._logger = logger.getChild(getattr(Shapes,bType).__name__)
logger.info(f'Krita version: {Application.version()}')
LSBG_PLUGIN_VERSION = '0.3.0' ; logger.info(f'LSBG version: {LSBG_PLUGIN_VERSION}')

MAINLAYOUT_CONTENTS_MARGINS = 10
MAINLAYOUT_MIN_WIDTH = 352

class LSBGDocker(DockWidget):

    _bAspectRatio: float = 1

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
        self.previewBoxLayout = QHBoxLayout()
        self.previewBoxLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.previewBox.setLayout(self.previewBoxLayout)
        self.preview = QSvgWidget(self)
        self.preview.renderer().setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        self.preview.setFixedSize(300,200)
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
        self.bubbleTypesLayout.addWidget(self.squareBubble)

        self.squircleBubble = QRadioButton(self)
        self.squircleBubble.setText("Squircle")
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
        # self.bubbleType = QComboBox()
        # for bubble in Shapes.__all__:
        #     self.bubbleType.addItem(bubble)
        # self.bubbleTypesLayout.addWidget(self.bubbleType)

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

        self.bOutlineThicknessSpinBox = QDoubleSpinBox(self)
        self.bOutlineThicknessSpinBox.setMinimum(0)
        self.bOutlineThicknessSpinBox.setMaximum(20)
        self.bOutlineThicknessSpinBox.setValue(3)
        self.bOutlineThicknessSpinBox.setDecimals(1)
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
        self.speechFontSize.setMaximum(144)
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

        self.bubbleText = QTextEdit("Laserkitty's speech\nbubble generator!")
        self.speechGroupLayout.addWidget(self.bubbleText)

        self.speechGroup.setLayout(self.speechGroupLayout)
        self.mainLayout.addWidget(self.speechGroup)



        # MARK:bubble tail params
        self.tailSize = QGroupBox()
        self.tailSize.setTitle("Tail size")
        self.tLenWidth = QVBoxLayout()


        self.tLenSliderAndSpinBox = QHBoxLayout()
        self.tLengthLabel = QLabel("Tail Length:")
        self.tLenSliderAndSpinBox.addWidget(self.tLengthLabel)

        DEFAULT_TAIL_LENGTH_VALUE = 10
        self.tLengthSlider = QSlider(self)
        self.tLengthSlider.setMinimum(0)
        self.tLengthSlider.setMaximum(self.speechFontSize.value()*10)
        self.tLengthSlider.setSingleStep(1)
        self.tLengthSlider.setValue(DEFAULT_TAIL_LENGTH_VALUE)
        self.tLengthSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tLenSliderAndSpinBox.addWidget(self.tLengthSlider)

        self.tLengthSpinBox = QDoubleSpinBox(self)
        self.tLengthSpinBox.setMinimum(0)
        self.tLengthSpinBox.setMaximum(self.speechFontSize.value()*10)
        self.tLengthSpinBox.setSingleStep(0.1)
        self.tLengthSpinBox.setValue(DEFAULT_TAIL_LENGTH_VALUE)
        self.tLenSliderAndSpinBox.addWidget(self.tLengthSpinBox)
        self.tLenWidth.addLayout(self.tLenSliderAndSpinBox)


        self.tWidthSliderAndSpinBox = QHBoxLayout()
        self.tWidthLabel = QLabel("Tail Width:")
        self.tWidthSliderAndSpinBox.addWidget(self.tWidthLabel)

        DEFAULT_TAIL_WIDTH_VALUE = 10
        self.tWidthSlider = QSlider(self)
        self.tWidthSlider.setMinimum(0)
        self.tWidthSlider.setMaximum(self.speechFontSize.value()*10)
        self.tWidthSlider.setSingleStep(1)
        self.tWidthSlider.setValue(DEFAULT_TAIL_WIDTH_VALUE)
        self.tWidthSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tWidthSliderAndSpinBox.addWidget(self.tWidthSlider)

        self.tWidthSpinBox = QDoubleSpinBox(self)
        self.tWidthSpinBox.setMinimum(0)
        self.tWidthSpinBox.setMaximum(self.speechFontSize.value()*10)
        self.tWidthSpinBox.setSingleStep(0.1)
        self.tWidthSpinBox.setValue(DEFAULT_TAIL_WIDTH_VALUE)
        self.tWidthSliderAndSpinBox.addWidget(self.tWidthSpinBox)
        self.tLenWidth.addLayout(self.tWidthSliderAndSpinBox)

        self.tailSize.setLayout(self.tLenWidth)
        self.mainLayout.addWidget(self.tailSize)

        self.tailPositions = QGroupBox()
        self.tailPositions.setTitle("Tail position")
        self.tailPositionsLayout = QHBoxLayout()

        DEFAULT_TAIL_ANGLE_VALUE = 45
        self.tAnglePosSlider = QSlider(self)
        self.tAnglePosSlider.setMinimum(0)
        self.tAnglePosSlider.setMaximum(360)
        self.tAnglePosSlider.setValue(DEFAULT_TAIL_ANGLE_VALUE)
        self.tAnglePosSlider.setSliderPosition(DEFAULT_TAIL_ANGLE_VALUE)
        self.tAnglePosSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tailPositionsLayout.addWidget(self.tAnglePosSlider)
        
        self.tAnglePosSpinBox = QDoubleSpinBox(self)
        self.tAnglePosSpinBox.setMinimum(0)
        self.tAnglePosSpinBox.setMaximum(360)
        self.tAnglePosSpinBox.setSingleStep(0.1)
        self.tAnglePosSpinBox.setValue(DEFAULT_TAIL_ANGLE_VALUE)
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
        # https://invent.kde.org/graphics/krita/-/tree/master/libs/libkis?ref_type=heads
        # https://api.kde.org/krita/html/classAngleSelector.html

        self.tailPositions.setLayout(self.tailPositionsLayout)
        self.mainLayout.addWidget(self.tailPositions)



        # MARK:signal connections

        self.addOnPage.clicked.connect(self.addOnPageShape)
        
        # bubble type signals
        
        # self.bubbleType.currentIndexChanged.connect(self.updatePreview) # TODO: passes new index to updatePreview
        
        self.roundBubble.clicked.connect(self.updatePreview)
        self.squareBubble.clicked.connect(self.updatePreview)
        self.squircleBubble.clicked.connect(self.updatePreview)
        # self.thoughtBubble.clicked.connect(self.updatePreview)
        # self.shoutBubble.clicked.connect(self.updatePreview)

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

        # bubble tail param signals
        self.tLengthSlider.valueChanged.connect(self.tLengthSpinBoxUpdate)
        self.tLengthSpinBox.valueChanged.connect(self.tLengthSliderUpdate)
        self.tWidthSlider.valueChanged.connect(self.tWidthSpinBoxUpdate)
        self.tWidthSpinBox.valueChanged.connect(self.tWidthSliderUpdate)
        self.tAnglePosSlider.valueChanged.connect(self.tailPositionSpinBoxUpdate)
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
        if self.bOutlineThicknessSpinBox.value() <= self.bOutlineThicknessSpinBox.maximum(): self.bOutlineThicknessSlider.setValue(int(self.bOutlineThicknessSpinBox.value()))
        self.updatePreview()

    def tLengthSpinBoxUpdate(self):
        logger.log(LSBG_DEBUG_VERBOSE, f'tail length updated from {self.tLengthSpinBox.value()} to {self.tLengthSlider.value()}')
        self.tLengthSpinBox.setValue(self.tLengthSlider.value())
        self.tailPositions.setEnabled(self.tLengthSlider.value() > 0)

    def tLengthSliderUpdate(self):
        if self.tLengthSpinBox.value() <= self.tLengthSpinBox.maximum(): self.tLengthSlider.setValue(int(self.tLengthSpinBox.value()))
        self.updatePreview()

    def tWidthSpinBoxUpdate(self):
        logger.log(LSBG_DEBUG_VERBOSE, f'tail width updated from {self.tWidthSpinBox.value()} to {self.tWidthSlider.value()}')
        self.tWidthSpinBox.setValue(self.tWidthSlider.value())
        self.tailPositions.setEnabled(self.tWidthSlider.value() > 0)

    def tWidthSliderUpdate(self):
        if self.tWidthSpinBox.value() <= self.tWidthSpinBox.maximum(): self.tWidthSlider.setValue(int(self.tWidthSpinBox.value()))
        self.updatePreview()

    def tailPositionSpinBoxUpdate(self):
        logger.log(LSBG_DEBUG_VERBOSE, f'tail angle position updated from {self.tAnglePosSpinBox.value()} to {self.tAnglePosSlider.value()}')
        self.tAnglePosSpinBox.setValue(self.tAnglePosSlider.value())
        self.updatePreview()

    def tailPositionSliderUpdate(self):
        if self.tAnglePosSpinBox.value() <= self.tAnglePosSpinBox.maximum(): self.tAnglePosSlider.setValue(int(self.tAnglePosSpinBox.value()))
        self.updatePreview()

    def flipAngleH_f(self):
        currAngle = self.tAnglePosSpinBox.value()
        if currAngle <= 180: self.tAnglePosSpinBox.setValue(180 - currAngle)
        else: self.tAnglePosSpinBox.setValue(540 - currAngle)
        logger.log(LSBG_DEBUG_VERBOSE, f'tail angle position updated from {currAngle} to {self.tAnglePosSpinBox.value()}')
        self.updatePreview()

    def flipAngleV_f(self):
        logger.log(LSBG_DEBUG_VERBOSE, f'tail angle position updated from {self.tAnglePosSpinBox.value()} to {360 - self.tAnglePosSpinBox.value()}')
        self.tAnglePosSpinBox.setValue(360 - self.tAnglePosSpinBox.value())
        self.updatePreview()

    def flipAngleHV_f(self):
        logger.log(LSBG_DEBUG_VERBOSE, f'tail angle position updated from {self.tAnglePosSpinBox.value()} to {(self.tAnglePosSpinBox.value() + 180) % 360}')
        self.tAnglePosSpinBox.setValue((self.tAnglePosSpinBox.value() + 180) % 360)
        self.updatePreview()

    def getPreview(self) -> str:

        #Calculate text box size
        font = self.speechFont.currentFont()
        font.setPointSize(self.speechFontSize.value())
        fontSize = self.speechFontSize.value()
        textWidth = 0
        lines = self.bubbleText.toPlainText().split('\n')
        for line in lines: textWidth = QFontMetricsF(font).width(line) if QFontMetricsF(font).width(line) > textWidth else textWidth
        textHeight = QFontMetrics(font).capHeight() + QFontMetricsF(font).lineSpacing()*max(len(lines)-1,0)
        logger.log(LSBG_DEBUG_VERBOSE, f'text width, height: {textWidth} {textHeight}')
        bTailLength = self.tLengthSpinBox.value()
        bTailWidth = self.tWidthSpinBox.value()
        logger.log(LSBG_DEBUG_VERBOSE, f'tail length, width: {bTailLength} {bTailWidth}')
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
        logger.log(LSBG_DEBUG_VERBOSE, f'bubble width, height: {bWidth} {bHeight}')
        frameWidth  = bTailLength + bPadding + textWidth  + bPadding + bTailLength
        frameHeight = bTailLength + bPadding + textHeight + bPadding + bTailLength
        self._bAspectRatio = frameHeight/frameWidth

        text = ''
        textStartX = bTailLength + bPadding + (textWidth  / 2)
        textStartY = bTailLength + bPadding + QFontMetrics(font).capHeight()

        logger.log(LSBG_DEBUG_VERBOSE, f'text font, font size: {QFontInfo(font).family()} {fontSize},\ntext start x,y: {textStartX} {textStartY}')

        for line in lines:
            text += f'<text x=\"{textStartX}\" y=\"{textStartY}\" style=\"font-size:{fontSize};font-family:{font.family()};fill:{self.speechFontColor.name()};text-anchor:middle\" >{line}</text>'
            textStartY += QFontMetricsF(font).lineSpacing()


        bubblePath: str = ''
        # MARK: round
        if self.roundBubble.isChecked():

            logger.log(logging.INFO, f'bubble type: round')

            self.tWidthSlider.setMaximum(self.speechFontSize.value()*10)

            Shapes.RoundBubble.setup(
                width=bWidth,
                height=bHeight,
                tailAnglePosition=self.tAnglePosSpinBox.value() * (2*pi) / 360,
                tailWidth=bTailWidth,
                tailLength=bTailLength
            )
            bubblePath = Shapes.RoundBubble.getPreview()

        # MARK: square
        if self.squareBubble.isChecked():

            logger.log(logging.INFO, f'bubble type: square')

            horizontalAngleBound = 180*(bWidth /2)/(2*(bWidth/2) + 2*(bHeight/2))
            verticalAngleBound   = 180*(bHeight/2)/(2*(bWidth/2) + 2*(bHeight/2))
            self.tWidthSlider.setMaximum(int(min(horizontalAngleBound, verticalAngleBound)))

            Shapes.SquareBubble.setup(
                width=bWidth,
                height=bHeight,
                tailAnglePosition=self.tAnglePosSpinBox.value(),
                tailWidth=bTailWidth,
                tailLength=bTailLength
            )
            bubblePath = Shapes.SquareBubble.getPreview()

        # MARK: squircle
        if self.squircleBubble.isChecked():

            logger.log(logging.INFO, f'bubble type: Squircle')
            
            self.tWidthSlider.setMaximum(180)
            self.tWidthSpinBox.setMaximum(180)

            Shapes.SquircleBubble.setup(
                width=bWidth,
                height=bHeight,
                tailAnglePosition=self.tAnglePosSpinBox.value(),
                tailWidth=self.tWidthSpinBox.value(),
                tailLength=self.tLengthSpinBox.value()
            )

            bubblePath = SquircleBubble.getPreview()

            # logger.log(LSBG_DEBUG_VERBOSE, f'squircle bubble path: {bubblePath}')

        # if self.thoughtBubble.isChecked(): pass
        # if self.shoutBubble.isChecked(): pass

        logger.log(LSBG_DEBUG_VERBOSE, f'frame width, height: {frameWidth} {frameHeight},\nbubble fill, outline color: {self.bubbleColor.name()} {self.outlineColor.name()},\nbubble outline thickness: {self.bOutlineThicknessSpinBox.value()}')

        bubble = f'<path style="fill:{self.bubbleColor.name()};stroke:{self.outlineColor.name()};stroke-width:{self.bOutlineThicknessSpinBox.value()};stroke-linejoin:round\" d=\"{bubblePath}"/>'
        posFixRect = f'<rect x="0" y="0" width="{frameWidth}" height="{frameHeight}" fill="#000000" fill-opacity="0%" stroke="#000000" stroke-width="0" stroke-opacity="0%" />'
        self.preview.setFixedSize(self.preview.width(), int(self.preview.width()*self._bAspectRatio))
        return f'<svg keepaspectratio="xMidYMid meet" width="{frameWidth}" height="{frameHeight}" ><g>{posFixRect}{bubble}{text}</g></svg>'

    def updatePreview(self):
        result = self.getPreview()
        resultBytes = bytearray(result,encoding='utf-8')
        self.preview.renderer().load(resultBytes)

    def addOnPageShape(self):
        result = self.getPreview()
        activeDoc = Krita.instance().activeDocument()
        activeLayer = activeDoc.activeNode()
        if activeLayer.type() == 'vectorlayer':
            activeLayer.addShapesFromSvg(result)
        else:
            root = activeDoc.rootNode()
            vecLayer = activeDoc.createVectorLayer(self.bubbleText.toPlainText()[:16])
            root.addChildNode(vecLayer, None)
            vecLayer.addShapesFromSvg(result)

    def resizeEvent(self, ev: QResizeEvent):
        sameSize = (ev.oldSize().width() == ev.size().width()) and (ev.oldSize().height() == ev.size().height())
        if not sameSize:
            scrollBarWidth = 9999
            for c in self.widget().children(): scrollBarWidth = c.width() if c.width() < scrollBarWidth else scrollBarWidth
            if ev.size().width() >= MAINLAYOUT_MIN_WIDTH+(2*MAINLAYOUT_CONTENTS_MARGINS):
                newWidth = ev.size().width()-(4*scrollBarWidth)-(2*MAINLAYOUT_CONTENTS_MARGINS)
                logger.log(LSBG_DEBUG_VERBOSE, f'svg widget width updated from {self.preview.width()} to {int(newWidth)}')
                self.preview.setFixedSize(int(newWidth), int(newWidth*self._bAspectRatio))

    def canvasChanged(self, canvas): pass

Krita.instance().addDockWidgetFactory(DockWidgetFactory("Laserkitty's Speech Bubble Generator", DockWidgetFactoryBase.DockRight, LSBGDocker))