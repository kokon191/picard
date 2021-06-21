# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileEditorPage(object):
    def setupUi(self, ProfileEditorPage):
        ProfileEditorPage.setObjectName("ProfileEditorPage")
        ProfileEditorPage.resize(605, 551)
        self.vboxlayout = QtWidgets.QVBoxLayout(ProfileEditorPage)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.user_profiles_groupbox = QtWidgets.QGroupBox(ProfileEditorPage)
        self.user_profiles_groupbox.setCheckable(False)
        self.user_profiles_groupbox.setObjectName("user_profiles_groupbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.user_profiles_groupbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.profile_editor_splitter = QtWidgets.QSplitter(self.user_profiles_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_editor_splitter.sizePolicy().hasHeightForWidth())
        self.profile_editor_splitter.setSizePolicy(sizePolicy)
        self.profile_editor_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.profile_editor_splitter.setChildrenCollapsible(False)
        self.profile_editor_splitter.setObjectName("profile_editor_splitter")
        self.profile_list = ProfileListWidget(self.profile_editor_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_list.sizePolicy().hasHeightForWidth())
        self.profile_list.setSizePolicy(sizePolicy)
        self.profile_list.setMinimumSize(QtCore.QSize(120, 0))
        self.profile_list.setObjectName("profile_list")
        self.settings_tree = QtWidgets.QTreeWidget(self.profile_editor_splitter)
        self.settings_tree.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.settings_tree.setColumnCount(1)
        self.settings_tree.setObjectName("settings_tree")
        self.settings_tree.headerItem().setText(0, "1")
        self.settings_tree.header().setVisible(True)
        self.verticalLayout.addWidget(self.profile_editor_splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.move_up_button = QtWidgets.QToolButton(self.user_profiles_groupbox)
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-up.png")
        self.move_up_button.setIcon(icon)
        self.move_up_button.setObjectName("move_up_button")
        self.horizontalLayout.addWidget(self.move_up_button)
        self.move_down_button = QtWidgets.QToolButton(self.user_profiles_groupbox)
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-down.png")
        self.move_down_button.setIcon(icon)
        self.move_down_button.setObjectName("move_down_button")
        self.horizontalLayout.addWidget(self.move_down_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.settings_status = QtWidgets.QLabel(self.user_profiles_groupbox)
        self.settings_status.setText("")
        self.settings_status.setObjectName("settings_status")
        self.horizontalLayout.addWidget(self.settings_status)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.vboxlayout.addWidget(self.user_profiles_groupbox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.make_it_so = QtWidgets.QPushButton(ProfileEditorPage)
        self.make_it_so.setObjectName("make_it_so")
        self.horizontalLayout_2.addWidget(self.make_it_so)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.buttonbox = QtWidgets.QDialogButtonBox(ProfileEditorPage)
        self.buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.NoButton)
        self.buttonbox.setObjectName("buttonbox")
        self.horizontalLayout_2.addWidget(self.buttonbox)
        self.vboxlayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ProfileEditorPage)
        QtCore.QMetaObject.connectSlotsByName(ProfileEditorPage)

    def retranslateUi(self, ProfileEditorPage):
        _translate = QtCore.QCoreApplication.translate
        self.user_profiles_groupbox.setTitle(_("User Profile(s)"))
        self.move_up_button.setToolTip(_("Move script up"))
        self.move_down_button.setToolTip(_("Move script down"))
        self.make_it_so.setText(_("Make It So!"))
from picard.ui.widgets.profilelistwidget import ProfileListWidget
