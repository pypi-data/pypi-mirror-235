# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FingerprintingOptionsPage(object):
    def setupUi(self, FingerprintingOptionsPage):
        FingerprintingOptionsPage.setObjectName("FingerprintingOptionsPage")
        FingerprintingOptionsPage.resize(371, 408)
        self.verticalLayout = QtWidgets.QVBoxLayout(FingerprintingOptionsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fingerprinting = QtWidgets.QGroupBox(FingerprintingOptionsPage)
        self.fingerprinting.setCheckable(False)
        self.fingerprinting.setObjectName("fingerprinting")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fingerprinting)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.disable_fingerprinting = QtWidgets.QRadioButton(self.fingerprinting)
        self.disable_fingerprinting.setObjectName("disable_fingerprinting")
        self.verticalLayout_3.addWidget(self.disable_fingerprinting)
        self.use_acoustid = QtWidgets.QRadioButton(self.fingerprinting)
        self.use_acoustid.setObjectName("use_acoustid")
        self.verticalLayout_3.addWidget(self.use_acoustid)
        self.verticalLayout.addWidget(self.fingerprinting)
        self.acoustid_settings = QtWidgets.QGroupBox(FingerprintingOptionsPage)
        self.acoustid_settings.setObjectName("acoustid_settings")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.acoustid_settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ignore_existing_acoustid_fingerprints = QtWidgets.QCheckBox(self.acoustid_settings)
        self.ignore_existing_acoustid_fingerprints.setObjectName("ignore_existing_acoustid_fingerprints")
        self.verticalLayout_2.addWidget(self.ignore_existing_acoustid_fingerprints)
        self.save_acoustid_fingerprints = QtWidgets.QCheckBox(self.acoustid_settings)
        self.save_acoustid_fingerprints.setObjectName("save_acoustid_fingerprints")
        self.verticalLayout_2.addWidget(self.save_acoustid_fingerprints)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.acoustid_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.fpcalc_threads = QtWidgets.QSpinBox(self.acoustid_settings)
        self.fpcalc_threads.setMinimum(1)
        self.fpcalc_threads.setMaximum(9)
        self.fpcalc_threads.setObjectName("fpcalc_threads")
        self.horizontalLayout_3.addWidget(self.fpcalc_threads)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label = QtWidgets.QLabel(self.acoustid_settings)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.acoustid_fpcalc = QtWidgets.QLineEdit(self.acoustid_settings)
        self.acoustid_fpcalc.setObjectName("acoustid_fpcalc")
        self.horizontalLayout_2.addWidget(self.acoustid_fpcalc)
        self.acoustid_fpcalc_browse = QtWidgets.QPushButton(self.acoustid_settings)
        self.acoustid_fpcalc_browse.setObjectName("acoustid_fpcalc_browse")
        self.horizontalLayout_2.addWidget(self.acoustid_fpcalc_browse)
        self.acoustid_fpcalc_download = QtWidgets.QPushButton(self.acoustid_settings)
        self.acoustid_fpcalc_download.setObjectName("acoustid_fpcalc_download")
        self.horizontalLayout_2.addWidget(self.acoustid_fpcalc_download)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.acoustid_fpcalc_info = QtWidgets.QLabel(self.acoustid_settings)
        self.acoustid_fpcalc_info.setText("")
        self.acoustid_fpcalc_info.setObjectName("acoustid_fpcalc_info")
        self.verticalLayout_2.addWidget(self.acoustid_fpcalc_info)
        self.label_2 = QtWidgets.QLabel(self.acoustid_settings)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acoustid_apikey = QtWidgets.QLineEdit(self.acoustid_settings)
        self.acoustid_apikey.setObjectName("acoustid_apikey")
        self.horizontalLayout.addWidget(self.acoustid_apikey)
        self.acoustid_apikey_get = QtWidgets.QPushButton(self.acoustid_settings)
        self.acoustid_apikey_get.setObjectName("acoustid_apikey_get")
        self.horizontalLayout.addWidget(self.acoustid_apikey_get)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.acoustid_settings)
        spacerItem1 = QtWidgets.QSpacerItem(181, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(FingerprintingOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(FingerprintingOptionsPage)

    def retranslateUi(self, FingerprintingOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.fingerprinting.setTitle(_("Audio Fingerprinting"))
        self.disable_fingerprinting.setText(_("Do not use audio fingerprinting"))
        self.use_acoustid.setText(_("Use AcoustID"))
        self.acoustid_settings.setTitle(_("AcoustID Settings"))
        self.ignore_existing_acoustid_fingerprints.setText(_("Ignore existing AcoustID fingerprints"))
        self.save_acoustid_fingerprints.setText(_("Save AcoustID fingerprints to file tags"))
        self.label_3.setText(_("Maximum threads to use for calculator:"))
        self.label.setText(_("Fingerprint calculator:"))
        self.acoustid_fpcalc_browse.setText(_("Browse…"))
        self.acoustid_fpcalc_download.setText(_("Download…"))
        self.label_2.setText(_("API key:"))
        self.acoustid_apikey_get.setText(_("Get API key…"))
