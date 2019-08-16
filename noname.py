# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer5.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()
		self.m_statusBar5 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.MyMenuBar = wx.MenuBar( 0 )
		self.openting = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.openting, wx.ID_ANY, u"建立新檔", wx.EmptyString, wx.ITEM_NORMAL )
		self.openting.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.openting, wx.ID_ANY, u"開啟舊檔", wx.EmptyString, wx.ITEM_NORMAL )
		self.openting.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.openting, wx.ID_ANY, u"儲存檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.openting.Append( self.m_menuItem4 )

		self.m_menuItem5 = wx.MenuItem( self.openting, wx.ID_ANY, u"結束程式", wx.EmptyString, wx.ITEM_NORMAL )
		self.openting.Append( self.m_menuItem5 )

		self.MyMenuBar.Append( self.openting, u"開啟" )

		self.SetMenuBar( self.MyMenuBar )

		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.BD, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.OP, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.SV, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.CL, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_TIMER, self.timeout, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def BD( self, event ):
		event.Skip()

	def OP( self, event ):
		event.Skip()

	def SV( self, event ):
		event.Skip()

	def CL( self, event ):
		event.Skip()

	def timeout( self, event ):
		event.Skip()


