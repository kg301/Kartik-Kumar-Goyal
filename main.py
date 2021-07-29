# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from newWindow import Ui_NewWindow
from openWindow import Ui_OpenWindow
from evaluateWindow import Ui_EvaluateWindow
from score import cal_score
from openTeam import Ui_OpenTeam
from editWindow import Ui_EditWindow

import sqlite3
myteam=sqlite3.connect('cricket.db')
curteams=myteam.cursor()


class Ui_MainWindow(object):
    def __init__(self):
        self.newDialog=QtWidgets.QMainWindow()
        self.new_screen=Ui_NewWindow()
        self.new_screen.setupUi(self.newDialog)

        self.openDialog=QtWidgets.QMainWindow()
        self.open_screen=Ui_OpenWindow()
        self.open_screen.setupUi(self.openDialog)

        self.evalDialog=QtWidgets.QMainWindow()
        self.eval_screen=Ui_EvaluateWindow()
        self.eval_screen.setupUi(self.evalDialog)

        self.teamDialog=QtWidgets.QMainWindow()
        self.team_screen=Ui_OpenTeam()
        self.team_screen.setupUi(self.teamDialog)

        self.editDialog=QtWidgets.QMainWindow()
        self.edit_screen=Ui_EditWindow()
        self.edit_screen.setupUi(self.editDialog)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 39, 741, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bat = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bat.setFont(font)
        self.bat.setObjectName("bat")
        self.horizontalLayout.addWidget(self.bat)
        self.batcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.batcount.setFont(font)
        self.batcount.setText("")
        self.batcount.setObjectName("batcount")
        self.horizontalLayout.addWidget(self.batcount)
        self.bowl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bowl.setFont(font)
        self.bowl.setObjectName("bowl")
        self.horizontalLayout.addWidget(self.bowl)
        self.bowlcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bowlcount.setFont(font)
        self.bowlcount.setText("")
        self.bowlcount.setObjectName("bowlcount")
        self.horizontalLayout.addWidget(self.bowlcount)
        self.alr = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.alr.setFont(font)
        self.alr.setObjectName("alr")
        self.horizontalLayout.addWidget(self.alr)
        self.alrcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.alrcount.setFont(font)
        self.alrcount.setText("")
        self.alrcount.setObjectName("alrcount")
        self.horizontalLayout.addWidget(self.alrcount)
        self.wk = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.wk.setFont(font)
        self.wk.setObjectName("wk")
        self.horizontalLayout.addWidget(self.wk)
        self.wkcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.wkcount.setFont(font)
        self.wkcount.setText("")
        self.wkcount.setObjectName("wkcount")
        self.horizontalLayout.addWidget(self.wkcount)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(70, 220, 271, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(429, 220, 261, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 120, 621, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.points_available = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.points_available.setFont(font)
        self.points_available.setText("")
        self.points_available.setObjectName("points_available")
        self.horizontalLayout_2.addWidget(self.points_available)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.points_used = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.points_used.setFont(font)
        self.points_used.setText("")
        self.points_used.setObjectName("points_used")
        self.horizontalLayout_2.addWidget(self.points_used)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(69, 179, 271, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rb1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb1.setFont(font)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_3.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb2.setFont(font)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_3.addWidget(self.rb2)
        self.rb3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb3.setFont(font)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_3.addWidget(self.rb3)
        self.rb4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb4.setFont(font)
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_3.addWidget(self.rb4)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(429, 180, 261, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.team_name = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.team_name.setFont(font)
        self.team_name.setText("")
        self.team_name.setObjectName("team_name")
        self.horizontalLayout_4.addWidget(self.team_name)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(334, 510, 111, 31))
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.actionNEW_team.setFont(font)
        self.actionNEW_team.setObjectName("actionNEW_team")
        self.actionOPEN_team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_team.setObjectName("actionOPEN_team")
        self.actionEDIT_team = QtWidgets.QAction(MainWindow)
        self.actionEDIT_team.setObjectName("actionEDIT_team")
        self.actionSAVE_team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_team.setObjectName("actionSAVE_team")
        self.actionEVALUATE_team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_team.setObjectName("actionEVALUATE_team")
        self.menuManage_Teams.addAction(self.actionNEW_team)
        self.menuManage_Teams.addAction(self.actionOPEN_team)
        self.menuManage_Teams.addAction(self.actionEDIT_team)
        self.menuManage_Teams.addAction(self.actionSAVE_team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        #self.team_name.setText("kg")                     

        self.rb1.clicked.connect(self.populate_list)    #rb1 is name of BAT radio button
        self.rb2.clicked.connect(self.populate_list)    #rb2 is name of BOWL radio button
        self.rb3.clicked.connect(self.populate_list)    #rb3 is name of ALR radio button
        self.rb4.clicked.connect(self.populate_list)    #rb4 is name of WK radio button

        self.exit.clicked.connect(self.exitapp)              #to exit the application

        # functioning of menu buttons
        self.actionNEW_team.triggered.connect(self.NEW_button)  #functioning of new menu button

        self.actionSAVE_team.triggered.connect(self.SAVE_button)  #to save our team

        self.actionOPEN_team.triggered.connect(self.OPEN_button)  #to open a team

        self.actionEVALUATE_team.triggered.connect(self.EVALUATE_button)   #to open evaluate window

        self.actionEDIT_team.triggered.connect(self.EDIT_button)   #to edit a team

        #functioning of different windows
        self.new_screen.ok_btn.clicked.connect(self.teamname)   #display team name

        self.open_screen.ok_btn.clicked.connect(self.openteam)  #open a team

        self.eval_screen.calScore.clicked.connect(self.evaluateteam)  #to evaluate score of a team

        self.edit_screen.ok_btn.clicked.connect(self.editteam)
                                               
        #to remove items from lists
        self.listWidget.itemDoubleClicked.connect(self.removelist1)        
        self.listWidget_2.itemDoubleClicked.connect(self.removelist2)

        #defining variables
        self.batsman_cnt=0
        self.wicketkeeper_cnt=0
        self.bowler_cnt=0
        self.allrounder_cnt=0
        self.credits_avl=1000
        self.credits_used=0
        self.total_players=self.batsman_cnt+self.bowler_cnt+self.allrounder_cnt+self.wicketkeeper_cnt 
       
        #to display initial points used and points available
        self.points_available.setText(str(self.credits_avl))
        self.points_used.setText(str(self.credits_used))
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bat.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.bowl.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.alr.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.wk.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_4.setText(_translate("MainWindow", "Points Available"))
        self.label_3.setText(_translate("MainWindow", "Points Used"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOW"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.label_7.setText(_translate("MainWindow", "Team Name"))
        self.exit.setText(_translate("MainWindow", "EXIT"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_team.setText(_translate("MainWindow", "NEW team"))
        self.actionNEW_team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOPEN_team.setText(_translate("MainWindow", "OPEN team"))
        self.actionOPEN_team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionEDIT_team.setText(_translate("MainWindow", "EDIT team"))
        self.actionEDIT_team.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))
        self.actionSAVE_team.setText(_translate("MainWindow", "SAVE team"))
        self.actionSAVE_team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEVALUATE_team.setText(_translate("MainWindow", "EVALUATE team"))
        self.actionEVALUATE_team.setShortcut(_translate("MainWindow", "Ctrl+E"))



    def teamname(self):
        self.actions()
        self.batsman_cnt=0
        self.wicketkeeper_cnt=0
        self.bowler_cnt=0
        self.allrounder_cnt=0
        self.credits_avl=1000
        self.credits_used=0
        name=self.new_screen.new_team.text()
        self.new_screen.new_team.clear()
        teams=[]
        curteams.execute("SELECT * FROM teams")
        record=curteams.fetchall()
        for i in record:
            teams.append(i[0])
        if name in teams:
            self.showMessageBox("Can not create team","The team name exists already.")
        else:
            self.team_name.setText(name)
            curteams.execute("SELECT * FROM match")
            record=curteams.fetchall()
            for i in record:
                self.listWidget.addItem(i[0])            
            self.newDialog.close()

    def openteam(self):
        self.actions()
        bat=0
        bowl=0
        alr=0
        wk=0
        self.teamDialog.show()
        self.team_screen.list.clear()
        teamname=self.open_screen.teamsList.currentText()
        self.team_screen.team_name.setText(teamname)
        sql="SELECT * FROM teams WHERE name='"+teamname+"'"
        curteams.execute(sql)
        record=curteams.fetchone()
        players_chosen=record[1].split(', ')
        self.team_screen.list.addItems(players_chosen)
        for i in range(self.team_screen.list.count()):
            player_name=self.team_screen.list.item(i).text()
            sql2="SELECT * FROM stats WHERE player='"+player_name+"' "
            curteams.execute(sql2)
            record=curteams.fetchone()
            ctgr=record[6]
            if ctgr=='BAT':
                bat+=1
            if ctgr=='BWL':
                bowl+=1
            if ctgr=='AR':
                alr+=1
            if ctgr=='WK':
                wk+=1
        self.team_screen.batcount.setText(str(bat))
        self.team_screen.bowlcount.setText(str(bowl))
        self.team_screen.alrcount.setText(str(alr))
        self.team_screen.wkcount.setText(str(wk))        
        self.openDialog.close()


    def editteam(self):
        self.actions()
        bat=0
        bowl=0
        alr=0
        wk=0
        teamname=self.edit_screen.teamsList.currentText()
        self.team_name.setText(teamname)
        sql="SELECT * FROM teams WHERE name='"+teamname+"'"
        curteams.execute(sql)
        record=curteams.fetchone()
        players_chosen=record[1].split(', ')
        self.listWidget_2.addItems(players_chosen)
        self.points_used.setText(str(record[2]))
        self.points_available.setText(str(1000-record[2]))
        self.credits_avl=1000-record[2]
        self.credits_used=record[2]
        for i in range(self.listWidget_2.count()):
            player_name=self.listWidget_2.item(i).text()
            sql2="SELECT * FROM stats WHERE player='"+player_name+"' "
            curteams.execute(sql2)
            record=curteams.fetchone()
            ctgr=record[6]
            
            if ctgr=='BAT':
                bat+=1
            if ctgr=='BWL':
                bowl+=1
            if ctgr=='AR':
                alr+=1
            if ctgr=='WK':
                wk+=1
        self.batcount.setText(str(bat))
        self.bowlcount.setText(str(bowl))
        self.alrcount.setText(str(alr))
        self.wkcount.setText(str(wk))
        self.batsman_cnt=bat
        self.bowler_cnt=bowl
        self.allrounder_cnt=alr
        self.wicketkeeper_cnt=wk
        self.total_players=bat+bowl+alr+wk
        self.editDialog.close()



    def evaluateteam(self):
        teamname=self.eval_screen.teamsList.currentText()
        sql="SELECT * FROM teams WHERE name='"+teamname+"' "
        if teamname=="SELECT TEAM":
            self.showMessageBox("Select a team ")
        else:
            curteams.execute(sql)
            record=curteams.fetchone()
            players=record[1].split(', ')
            self.eval_screen.list1.addItems(players)
            self.total_points=0
            
            for i in range(self.eval_screen.list1.count()):
                name=self.eval_screen.list1.item(i).text()
                sql2="SELECT * FROM match WHERE Player= '"+name+"'"
                curteams.execute(sql2)
                record1=curteams.fetchone()
                player_score=cal_score(record1)
                self.total_points+=player_score
                self.eval_screen.list2.addItem(str(player_score))
            self.eval_screen.total_score.setText(str(self.total_points))
            
        

    def populate_list(self):
        
        if self.team_name.text()=='':
            self.showMessageBox("Enter your team name first")

        elif self.rb1.isChecked()==True:
            self.listWidget.clear()
            sql="SELECT * FROM stats WHERE ctg=='BAT'"
            curteams.execute(sql)
            players=curteams.fetchall()
            list2_items=[]
            for index in range(self.listWidget_2.count()):
                list2_items.append(self.listWidget_2.item(index).text())
            for i in players:
                if i[0] not in list2_items:
                    self.listWidget.addItem(i[0])
                  

        elif self.rb2.isChecked()==True:
            self.listWidget.clear()
            sql="SELECT * FROM stats WHERE ctg=='BWL'"
            curteams.execute(sql)
            players=curteams.fetchall()
            list2_items=[]
            for index in range(self.listWidget_2.count()):
                list2_items.append(self.listWidget_2.item(index).text())
            for i in players:
                if i[0] not in list2_items:
                    self.listWidget.addItem(i[0])

                    
        elif self.rb3.isChecked()==True:
            self.listWidget.clear()
            sql="SELECT * FROM stats WHERE ctg=='AR'"
            curteams.execute(sql)
            players=curteams.fetchall()
            list2_items=[]
            for index in range(self.listWidget_2.count()):
                list2_items.append(self.listWidget_2.item(index).text())
            for i in players:
                if i[0] not in list2_items:
                    self.listWidget.addItem(i[0])

                    
        elif self.rb4.isChecked()==True:
            self.listWidget.clear()
            sql="SELECT * FROM stats WHERE ctg=='WK'"
            curteams.execute(sql)
            players=curteams.fetchall()
            list2_items=[]
            for index in range(self.listWidget_2.count()):
                list2_items.append(self.listWidget_2.item(index).text())
            for i in players:
                if i[0] not in list2_items:
                    self.listWidget.addItem(i[0])
                    

    def removelist1(self,item):
        sql="SELECT * FROM stats WHERE player='"+item.text()+"'"
        curteams.execute(sql)
        record=curteams.fetchone()
        ctgr=record[6]
        credit=record[5]
        if ctgr=='BAT':
            self.batsman_cnt+=1
            self.error()
            if self.countbt==1:
                self.batsman_cnt-=1
            else:
                self.credits_avl-=credit
                if self.credits_avl<0:
                    self.batsman_cnt-=1
                    self.credits_avl+=credit
                    self.showMessageBox("Not enough credits","You can't use more than given credits")
                else:
                    self.credits_used+=credit
                    self.points_available.setText(str(self.credits_avl))
                    self.points_used.setText(str(self.credits_used))
                    self.listWidget.takeItem(self.listWidget.row(item))
                    self.batcount.setText(str(self.batsman_cnt))
                    self.listWidget_2.addItem(item.text())
                
       
        if ctgr=='BWL':
            self.bowler_cnt+=1
            self.error()
            if self.countbl==1:
                self.bowler_cnt-=1
            else:
                self.credits_avl-=credit
                if self.credits_avl<0:
                    self.bowler_cnt-=1
                    self.credits_avl+=credit
                    self.showMessageBox("Not enough credits","You can't use more than given credits")
                else:
                    self.credits_used+=credit
                    self.points_available.setText(str(self.credits_avl))
                    self.points_used.setText(str(self.credits_used))
                    self.listWidget.takeItem(self.listWidget.row(item))
                    self.bowlcount.setText(str(self.bowler_cnt))
                    self.listWidget_2.addItem(item.text())
            

        if ctgr=='AR':
            self.allrounder_cnt+=1
            self.error()
            if self.countar==1:
                self.allrounder_cnt-=1
            else:
                self.credits_avl-=credit
                if self.credits_avl<0:
                    self.allrounder_cnt-=1
                    self.credits_avl+=credit
                    self.showMessageBox("Not enough credits","You can't use more than given credits")
                else:
                    self.credits_used+=credit
                    self.points_available.setText(str(self.credits_avl))
                    self.points_used.setText(str(self.credits_used))
                    self.listWidget.takeItem(self.listWidget.row(item))
                    self.alrcount.setText(str(self.allrounder_cnt))
                    self.listWidget_2.addItem(item.text())
            

        if ctgr=='WK':
             self.wicketkeeper_cnt+=1
             self.error()
             if self.countwk==1:
                self.wicketkeeper_cnt-=1
             else:
                self.credits_avl-=credit
                if self.credits_avl<0:
                    self.wicketkeeper_cnt-=1
                    self.credits_avl+=credit
                    self.showMessageBox("Not enough credits","You can't use more than given credits")
                else:
                    self.credits_used+=credit
                    self.points_available.setText(str(self.credits_avl))
                    self.points_used.setText(str(self.credits_used))
                    self.listWidget.takeItem(self.listWidget.row(item))
                    self.wkcount.setText(str(self.wicketkeeper_cnt))
                    self.listWidget_2.addItem(item.text())
        self.total_players=self.batsman_cnt+self.bowler_cnt+self.allrounder_cnt+self.wicketkeeper_cnt
        if self.total_players>11:
            self.showMessageBox("player limit exceeded","Team can't have more than 11 players. Please remove  player.")

        
    def removelist2(self,item):
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        sql="SELECT * FROM stats WHERE player='"+item.text()+"'"
        curteams.execute(sql)
        record=curteams.fetchone()
        ctgr=record[6]
        credit=record[5]
        self.credits_avl+=credit
        self.credits_used-=credit
        self.points_available.setText(str(self.credits_avl))
        self.points_used.setText(str(self.credits_used))
        if ctgr=='BAT':
            self.batsman_cnt-=1
            self.batcount.setText(str(self.batsman_cnt))
            if self.rb1.isChecked()==True:
                self.listWidget.addItem(item.text())

        if ctgr=='BWL':
            self.bowler_cnt-=1
            self.bowlcount.setText(str(self.bowler_cnt))
            if self.rb2.isChecked()==True:
                self.listWidget.addItem(item.text())

        if ctgr=='AR':
            self.allrounder_cnt-=1
            self.alrcount.setText(str(self.allrounder_cnt))
            if self.rb3.isChecked()==True:
                self.listWidget.addItem(item.text())

        if ctgr=='WK':
            self.wicketkeeper_cnt-=1
            self.wkcount.setText(str(self.wicketkeeper_cnt))
            if self.rb4.isChecked()==True:
                self.listWidget.addItem(item.text()) 
            
        self.total_players=self.batsman_cnt+self.bowler_cnt+self.allrounder_cnt+self.wicketkeeper_cnt       
        
    def NEW_button(self):
        self.newDialog.show()
        
    def OPEN_button(self):
        self.openDialog.show()
        self.open_screen.teamsList.clear()
        sql="SELECT * FROM teams"
        curteams.execute(sql)
        record=curteams.fetchall()
        for i in record:
            self.open_screen.teamsList.addItem(i[0])

    def EDIT_button(self):
        self.editDialog.show()
        self.edit_screen.teamsList.clear()
        sql="SELECT * FROM teams"
        curteams.execute(sql)
        record=curteams.fetchall()
        for i in record:
            self.edit_screen.teamsList.addItem(i[0])
        
    def SAVE_button(self,d):
        if self.team_name.text()=="":
            self.showMessageBox("Team can't be saved","Create a team first.")
        if self.total_players==0:
            self.showMessageBox("Team can't be saved","Not enough players .Please select some more players to take total players count to 11")
        if self.total_players<11:
            self.showMessageBox("Team can't be saved","Not enough players .Please select some more players to take total players count to 11")
            
        elif self.total_players>11:
            self.showMessageBox("Team can't be saved" ,"player limit exceeded. Please remove some players to take total players count to 11")
            
        elif self.batsman_cnt<3:
            self.showMessageBox("Team can't be saved","The team must contain atleast 3 batsmen ")
            
        elif self.bowler_cnt<3:
            self.showMessageBox("Team can't be saved","The team must contain atleast 3 bowlers ")
            
        elif self.allrounder_cnt<1:
            self.showMessageBox("Team can't be saved","The team must contain atleast 1 all rounder ")
            
        elif self.wicketkeeper_cnt<1:
            self.showMessageBox("Team can't be saved","The team must contain atleast 1 wicket keeper ")
            
        else:
            players_chosen=""
            for i in range(self.listWidget_2.count()):
                players_chosen+=self.listWidget_2.item(i).text()
                if i< self.listWidget_2.count()-1:
                    players_chosen+= ", "
            a=self.team_name.text()
            b=players_chosen
            c=self.points_used.text()
            teams=[]
            curteams.execute("SELECT * FROM teams")
            record=curteams.fetchall()
            for i in record:
                teams.append(i[0])
            if a in teams:
                curteams.execute("DELETE FROM teams WHERE name='"+a+"'")
            sql="INSERT INTO teams (name,players,value) VALUES ('"+a+"','"+b+"','"+c+"');"
            curteams.execute(sql)
            myteam.commit()
            self.showMessageBox2("Your team is saved successfully","Now you can evaluate your team's score and can also make a new team","Congrats!!!")
            self.actions()


    def EVALUATE_button(self):
        self.actions()
        self.evalDialog.show()
        self.eval_screen.matchList.addItem('Match 1')
        self.eval_screen.matchList.addItem('Match 2')
        self.eval_screen.matchList.addItem('Match 3')
        self.eval_screen.matchList.addItem('Match 4')
        self.eval_screen.teamsList.clear()
        self.eval_screen.teamsList.addItem("SELECT TEAM")
        sql="SELECT * FROM teams "
        curteams.execute(sql)
        record=curteams.fetchall()
        for i in record:
            self.eval_screen.teamsList.addItem(i[0])
        
        

    def actions(self):
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.batcount.setText('0')
        self.bowlcount.setText('0')
        self.alrcount.setText('0')
        self.wkcount.setText('0')
        self.points_used.setText('0')
        self.points_available.setText('0')
        self.team_name.setText("")
        self.eval_screen.list1.clear()
        self.eval_screen.list2.clear()
        self.eval_screen.total_score.setText('')

    
    def error(self):
        self.countbt=0
        self.countbl=0
        self.countar=0
        self.countwk=0
        if self.batsman_cnt>5 :
            self.countbt+=1
            self.showMessageBox("Batsman can not be more than 5")
        if self.bowler_cnt>4:
            self.countbl+=1
            self.showMessageBox("You can't select more than 5 bowlers")
        if self.allrounder_cnt>3:
            self.countar+=1
            self.showMessageBox("You can't select more than 3 all rounders")
        if self.wicketkeeper_cnt>1:
            self.countwk+=1
            self.showMessageBox("You can't select more than 1 wicket-keeper")

               

    def showMessageBox(self,message,det_message="Please bind by game rules. Pick your team wisely."):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setDetailedText(det_message)                        
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

    def showMessageBox2(self,message,det_message,tit):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setDetailedText(det_message)                        
        msg.setWindowTitle(tit)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

    def exitapp(self):
        self.showMessageBox2("Thank you for visiting my application","","Hurrah!!")
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
