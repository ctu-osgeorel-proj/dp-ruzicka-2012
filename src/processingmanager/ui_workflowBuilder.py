# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/czenda/piskoviste/qgis_PF_cze/qgis/python/plugins/processingmanager/workflowBuilder.ui'
#
# Created: Wed May  2 18:27:22 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_workflowBuilder(object):
    def setupUi(self, workflowBuilder):
        workflowBuilder.setObjectName(_fromUtf8("workflowBuilder"))
        workflowBuilder.resize(754, 480)
        self.verticalLayout = QtGui.QVBoxLayout(workflowBuilder)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphicsView = GraphicsView(workflowBuilder)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout.addWidget(self.graphicsView)
        self.dockWidget = QtGui.QDockWidget(workflowBuilder)
        self.dockWidget.setMaximumSize(QtCore.QSize(350, 524287))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.item = QtGui.QLabel(self.dockWidgetContents)
        self.item.setObjectName(_fromUtf8("item"))
        self.verticalLayout_4.addWidget(self.item)
        self.toolBox = QtGui.QToolBox(self.dockWidgetContents)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.ioput = QtGui.QWidget()
        self.ioput.setEnabled(True)
        self.ioput.setGeometry(QtCore.QRect(0, 0, 332, 236))
        self.ioput.setObjectName(_fromUtf8("ioput"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.ioput)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.ioput)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.mandatoryTab = QtGui.QWidget()
        self.mandatoryTab.setObjectName(_fromUtf8("mandatoryTab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.mandatoryTab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.mandatoryScroll = QtGui.QScrollArea(self.mandatoryTab)
        self.mandatoryScroll.setFrameShape(QtGui.QFrame.NoFrame)
        self.mandatoryScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mandatoryScroll.setWidgetResizable(True)
        self.mandatoryScroll.setObjectName(_fromUtf8("mandatoryScroll"))
        self.mandatoryWidget = QtGui.QWidget()
        self.mandatoryWidget.setGeometry(QtCore.QRect(0, 0, 292, 167))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mandatoryWidget.sizePolicy().hasHeightForWidth())
        self.mandatoryWidget.setSizePolicy(sizePolicy)
        self.mandatoryWidget.setObjectName(_fromUtf8("mandatoryWidget"))
        self.mandatoryForm = QtGui.QFormLayout(self.mandatoryWidget)
        self.mandatoryForm.setObjectName(_fromUtf8("mandatoryForm"))
        self.mandatoryScroll.setWidget(self.mandatoryWidget)
        self.verticalLayout_5.addWidget(self.mandatoryScroll)
        self.tabWidget.addTab(self.mandatoryTab, _fromUtf8(""))
        self.optionalTab = QtGui.QWidget()
        self.optionalTab.setObjectName(_fromUtf8("optionalTab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.optionalTab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.optionalScroll = QtGui.QScrollArea(self.optionalTab)
        self.optionalScroll.setFrameShape(QtGui.QFrame.NoFrame)
        self.optionalScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.optionalScroll.setWidgetResizable(True)
        self.optionalScroll.setObjectName(_fromUtf8("optionalScroll"))
        self.optionalWidget = QtGui.QWidget()
        self.optionalWidget.setGeometry(QtCore.QRect(0, 0, 292, 167))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionalWidget.sizePolicy().hasHeightForWidth())
        self.optionalWidget.setSizePolicy(sizePolicy)
        self.optionalWidget.setObjectName(_fromUtf8("optionalWidget"))
        self.optionalForm = QtGui.QFormLayout(self.optionalWidget)
        self.optionalForm.setObjectName(_fromUtf8("optionalForm"))
        self.optionalScroll.setWidget(self.optionalWidget)
        self.verticalLayout_6.addWidget(self.optionalScroll)
        self.tabWidget.addTab(self.optionalTab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.toolBox.addItem(self.ioput, _fromUtf8(""))
        self.description = QtGui.QWidget()
        self.description.setGeometry(QtCore.QRect(0, 0, 102, 102))
        self.description.setObjectName(_fromUtf8("description"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.description)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textEditDesc = QtGui.QTextBrowser(self.description)
        self.textEditDesc.setObjectName(_fromUtf8("textEditDesc"))
        self.verticalLayout_3.addWidget(self.textEditDesc)
        self.toolBox.addItem(self.description, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.toolBox)
        self.buttonLayout = QtGui.QGridLayout()
        self.buttonLayout.setObjectName(_fromUtf8("buttonLayout"))
        self.executeButton = QtGui.QPushButton(self.dockWidgetContents)
        self.executeButton.setToolTip(_fromUtf8(""))
        self.executeButton.setObjectName(_fromUtf8("executeButton"))
        self.buttonLayout.addWidget(self.executeButton, 0, 0, 1, 1)
        self.cancelButton = QtGui.QPushButton(self.dockWidgetContents)
        self.cancelButton.setToolTip(_fromUtf8(""))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.buttonLayout.addWidget(self.cancelButton, 1, 0, 1, 1)
        self.saveButton = QtGui.QPushButton(self.dockWidgetContents)
        self.saveButton.setToolTip(_fromUtf8(""))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.buttonLayout.addWidget(self.saveButton, 0, 1, 1, 1)
        self.clearButton = QtGui.QPushButton(self.dockWidgetContents)
        self.clearButton.setToolTip(_fromUtf8(""))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.buttonLayout.addWidget(self.clearButton, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.buttonLayout)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dockWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.statusBar = QtGui.QStatusBar(workflowBuilder)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.verticalLayout.addWidget(self.statusBar)

        self.retranslateUi(workflowBuilder)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(workflowBuilder)

    def retranslateUi(self, workflowBuilder):
        workflowBuilder.setWindowTitle(QtGui.QApplication.translate("workflowBuilder", "Workflow Builder 0.01", None, QtGui.QApplication.UnicodeUTF8))
        self.item.setText(QtGui.QApplication.translate("workflowBuilder", "Item", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mandatoryTab), QtGui.QApplication.translate("workflowBuilder", "Mandatory", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionalTab), QtGui.QApplication.translate("workflowBuilder", "Optional", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.ioput), QtGui.QApplication.translate("workflowBuilder", "Input/Output", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.description), QtGui.QApplication.translate("workflowBuilder", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.executeButton.setText(QtGui.QApplication.translate("workflowBuilder", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("workflowBuilder", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("workflowBuilder", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("workflowBuilder", "Clear", None, QtGui.QApplication.UnicodeUTF8))

from gui import GraphicsView
import processing_rc
